################## Auto submit stufff ######################################
# from {source}

import argparse
import configparser
import os
import re
import requests
import sys
import time

from lxml.html import fragment_fromstring

_DEFAULT_CONFIG = './KattisBot/.kattisrc'
_LANGUAGE_GUESS = {
    '.4th': 'Forth',
    '.c': 'C',
    '.c++': 'C++',
    '.cc': 'C++',
    '.c#': 'C#',
    '.cpp': 'C++',
    '.cs': 'C#',
    '.cxx': 'C++',
    '.cbl': 'COBOL',
    '.cob': 'COBOL',
    '.cpy': 'COBOL',
    '.forth': 'Forth',
    '.frt': 'Forth',
    '.fs': 'F#',
    '.fth': 'Forth',
    '.go': 'Go',
    '.hs': 'Haskell',
    '.java': 'Java',
    '.js': 'JavaScript (Node.js)',
    '.ts': 'TypeScript',
    '.kt': 'Kotlin',
    '.lisp': 'Common Lisp',
    '.cl': 'Common Lisp',
    '.m': 'Objective-C',
    '.ml': 'OCaml',
    '.pas': 'Pascal',
    '.php': 'PHP',
    '.pl': 'Prolog',
    '.py': 'Python 3',
    '.pyc': 'Python 3',
    '.rb': 'Ruby',
    '.rkt': 'Racket',
    '.rs': 'Rust',
    '.scala': 'Scala',
    '.f90': 'Fortran',
    '.f': 'Fortran',
    '.for': 'Fortran',
    '.sh': 'Bash',
    '.apl': 'APL',
    '.ss': 'Gerbil',
    '.jl': 'Julia',
    '.vb': 'Visual Basic',
    '.dart': 'Dart',
    '.zig': 'Zig',
    '.swift': 'Swift',
    '.nim': 'Nim',
    '.lua': 'Lua',
    '.pm': 'Perl',
    '.sno': 'SNOBOL',
    '.odin': 'Odin',
    '.a68': 'Algol 68',
    '.cr': 'Crystal',
    '.sim': 'Simula 67',
    '.d': 'D',
    '.mod': 'Modula-2',
    '.st': 'Smalltalk',
    '.adb': 'Ada',
    '.ads': 'Ada',
    '.erl': 'Erlang',
    '.ex': 'Elixir',
}
_GUESS_MAINCLASS = { 'Elixir', 'Erlang', 'Java', 'Kotlin', 'Modula-2', 'Scala' }
_GUESS_MAINFILE = {
    'Ada', 'Algol 68', 'APL', 'Bash', 'Crystal', 'Dart', 'Forth', 'Gerbil', 'JavaScript (Node.js)',
    'JavaScript (SpiderMonkey)', 'Julia', 'Common Lisp', 'Lua', 'Nim', 'Octave', 'Pascal', 'Perl', 'PHP',
	'Python 2', 'Python 3', 'Racket', 'Ruby', 'Rust', 'Simula', 'Smalltalk', 'SNOBOL', 'TypeScript', 'Zig',
}
_HEADERS = { 'User-Agent': 'kattis-cli-submit' } #Change this to include email adress
_RUNNING_STATUS = 5
_COMPILE_ERROR_STATUS = 8
_ACCEPTED_STATUS = 16
_STATUS_MAP = {
    0: 'New', # <invalid value>
    1: 'New',
    2: 'Waiting for compile',
    3: 'Compiling',
    4: 'Waiting for run',
    _RUNNING_STATUS: 'Running',
    6: 'Judge Error',
    # 7: '<invalid value>',
    _COMPILE_ERROR_STATUS: 'Compile Error',
    9: 'Run Time Error',
    10: 'Memory Limit Exceeded',
    11: 'Output Limit Exceeded',
    12: 'Time Limit Exceeded',
    13: 'Illegal Function',
    14: 'Wrong Answer',
    # 15: '<invalid value>',
    _ACCEPTED_STATUS: 'Accepted',
}


class ConfigError(Exception):
        pass


def get_url(cfg, option, default):
    if cfg.has_option('kattis', option):
        return cfg.get('kattis', option)
    else:
        hostname = cfg.get('kattis', 'hostname')
        return f'https://{hostname}/{default}'
    
def guess_language(ext, files):
    if ext == ".C":
        return "C++"
    ext = ext.lower()
    if ext == ".h":
        if any(f.endswith(".c") for f in files):
            return "C"
        else:
            return "C++"
    if ext == ".py":
        return "Python 3"
    return _LANGUAGE_GUESS.get(ext, None)

def guess_mainfile(language, files):
    for filename in files:
        if os.path.splitext(os.path.basename(filename))[0] in ['main', 'Main']:
            return filename
    for filename in files:
        try:
            with open(filename) as f:
                conts = f.read()
                if language in ['Java', 'Rust', 'Scala', 'Kotlin'] and re.search(r' main\s*\(', conts):
                    return filename
                if language == 'Pascal' and re.match(r'^\s*[Pp]rogram\b', conts):
                    return filename
        except IOError:
            pass
    return files[0]

def guess_mainclass(language, files):
    if language in _GUESS_MAINFILE and len(files) > 1:
        return os.path.basename(guess_mainfile(language, files))
    if language in _GUESS_MAINCLASS:
        mainfile = os.path.basename(guess_mainfile(language, files))
        name = os.path.splitext(mainfile)[0]
        if language == 'Kotlin':
            return name[0].upper() + name[1:] + 'Kt'
        return name

def login(login_url, username, password=None, token=None):
    """Log in to Kattis.
    At least one of password or token needs to be provided.
    Returns a requests.Response with cookies needed to be able to submit
    """
    login_args = {'user': username, 'script': 'true'}
    if password:
        login_args['password'] = password
    if token:
        login_args['token'] = token
    return requests.post(login_url, data=login_args, headers=_HEADERS)

def login_from_config(cfg):
    """Log in to Kattis using the access information in a kattisrc file
    Returns a requests.Response with cookies needed to be able to submit
    """
    username = cfg.get('user', 'username')
    password = token = None
    try:
        password = cfg.get('user', 'password')
    except configparser.NoOptionError:
        pass
    try:
        token = cfg.get('user', 'token')
    except configparser.NoOptionError:
        pass
    if password is None and token is None:
        raise ConfigError('''\
Your .kattisrc file appears corrupted. It must provide a token (or a
KATTIS password).
Please download a new .kattisrc file''')
    loginurl = get_url(cfg, 'loginurl', 'login')
    return login(loginurl, username, password, token)

def submit(submit_url, cookies, problem, language, files, mainclass='', tag='', assignment=None, contest=None):
    """Make a submission.
    The url_opener argument is an OpenerDirector object to use (as
    returned by the login() function)
    Returns the requests.Result from the submission
    """
    data = {'submit': 'true',
            'submit_ctr': 2,
            'language': language,
            'mainclass': mainclass,
            'problem': problem,
            'tag': tag,
            'script': 'true'}
    if assignment is not None:
        data['assignment'] = assignment
    if contest is not None:
        data['contest'] = contest
    sub_files = []
    print(os.path.dirname(os.path.realpath(__file__)))
    with open(files, 'rb') as sub_file:
        sub_files.append(('sub_file[]',
                              (os.path.basename(files),
                               sub_file.read(),
                               'application/octet-stream')))
    return requests.post(submit_url, data=data, files=sub_files, cookies=cookies, headers=_HEADERS)

def get_submission_url(submit_response, cfg):
    m = re.search(r'Submission ID: (\d+)', submit_response)
    if m:
        submissions_url = get_url(cfg, 'submissionsurl', 'submissions')
        submission_id = m.group(1)
        return f'{submissions_url}/{submission_id}'

def get_submission_status(submission_url, cookies):
    reply = requests.get(submission_url + '?json', cookies=cookies, headers=_HEADERS)
    return reply.json()

_RED_COLOR = 31
_GREEN_COLOR = 32
def color(s, c):
    return f'\x1b[{c}m{s}\x1b[0m'

def show_judgement(submission_url, cfg):
    print()
    login_reply = login_from_config(cfg)
    while True:
        status = get_submission_status(submission_url, login_reply.cookies)
        status_id = status['status_id']
        testcases_done = status['testcase_index']
        testcases_total = status['row_html'].count('<i') - 1
        status_text = _STATUS_MAP.get(status_id, f'Unknown status {status_id}')
        if status_id < _RUNNING_STATUS:
            print(f'\r{status_text}...', end='')
        else:
            print('\rTest cases: ', end='')
        if status_id == _COMPILE_ERROR_STATUS:
            print(f'\r{color(status_text, _RED_COLOR)}', end='')
            try:
                root = fragment_fromstring(status['feedback_html'], create_parent=True)
                error = root.find('.//pre').text
                print(color(':', _RED_COLOR))
                print(error, end='')
            except:
                pass
        elif status_id < _RUNNING_STATUS:
            print(f'\r{status_text}...', end='')
        else:
            print('\rTest cases: ', end='')
            if testcases_total == 0:
                print('???', end='')
            else:
                s = '.' * (testcases_done - 1)
                if status_id == _RUNNING_STATUS:
                    s += '?'
                elif status_id == _ACCEPTED_STATUS:
                    s += '.'
                else:
                    s += 'x'
                print(f'[{s: <{testcases_total}}]  {testcases_done} / {testcases_total}', end='')
        sys.stdout.flush()
        if status_id > _RUNNING_STATUS:
            # Done
            print()
            success = status_id == _ACCEPTED_STATUS
            try:
                root = fragment_fromstring(status['row_html'], create_parent=True)
                cpu_time = root.find('.//*[@data-type="cpu"]').text
                status_text += " (" + cpu_time + ")"
            except:
                pass
            if status_id != _COMPILE_ERROR_STATUS:
                print(color(status_text, _GREEN_COLOR if success else _RED_COLOR))
            return success
        time.sleep(0.25)

def get_config():
    """Returns a ConfigParser object for the .kattisrc file(s)
    """
    cfg = configparser.ConfigParser()
    if os.path.exists(_DEFAULT_CONFIG):
        cfg.read(_DEFAULT_CONFIG)
    try:
        file = __file__
    except NameError:
        file = sys.argv[0]
    if not cfg.read([os.path.join(os.path.expanduser("~"), '.kattisrc'),
                     os.path.join(os.path.dirname(file), '.kattisrc'),
                     os.path.join(os.path.dirname(os.path.realpath(file)), '.kattisrc')]):
        raise ConfigError('''\
I failed to read in a config file from your home directory or from the
same directory as this script. To download a .kattisrc file please visit
https://<kattis>/download/kattisrc
The file should look something like this:
[user]
username: yourusername
token: *********
[kattis]
hostname: <kattis>
loginurl: https://<kattis>/login
submissionurl: https://<kattis>/submit
submissionsurl: https://<kattis>/submissions''')
    return cfg

def submit_problem(files, problem):
    try:
        cfg = get_config()
    except ConfigError as exc:
        print(exc)
        sys.exit(1)
    problem, ext = problem, '.py'
    language = guess_language(ext, files)
    mainclass = None #guess_mainclass(language, files)
    tag = '-f'
    try:
        login_reply = login_from_config(cfg)
    except ConfigError as exc:
        print(exc)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print('Login connection failed:', err)
        sys.exit(1)
    if not login_reply.status_code == 200:
        print('Login failed.')
        if login_reply.status_code == 403:
            print('Incorrect username or password/token (403)')
        elif login_reply.status_code == 404:
            print('Incorrect login URL (404)')
        else:
            print('Status code:', login_reply.status_code)
        sys.exit(1)
    submit_url = get_url(cfg, 'submissionurl', 'submit')
    print(files)
    try:
        result = submit(submit_url,
                        login_reply.cookies,
                        problem,
                        language,
                        files,
                        mainclass,
                        tag)
    except requests.exceptions.RequestException as err:
        print('Submit connection failed:', err)
        #sys.exit(1)
    if result.status_code != 200:
        print('Submission failed.')
        if result.status_code == 403:
            print('Access denied (403)')
        elif result.status_code == 404:
            print('Incorrect submit URL (404)')
        else:
            print('Status code:', result.status_code)
        #sys.exit(1)
    plain_result = result.content.decode('utf-8').replace('<br />', '\n')
    print(plain_result)
    submission_url = None
    try:
        submission_url = get_submission_url(plain_result, cfg)
    except configparser.NoOptionError:
        pass
    if submission_url:
        print(submission_url)
        if not show_judgement(submission_url, cfg):
            pass
            #sys.exit(1)
    return plain_result