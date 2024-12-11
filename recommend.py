########### Auto recommendation stuff #################
import os

DIFFICULTY = 0 # 0-1 trivial, 2-3 easy, 4-5 moderate, 6-7 hard
PROG = '.py' # change to desired programming language file extension
INCLUDE_PB_LINK_IN_FILE = False
INCLUDE_PB_LINK_IN_CONSOLE = True
INCLUDE_SUBMIT_COMMAND = False
SOURCE_LOCATION = "source/" #change to desired source directory

def get_problem(kt):
    sug = kt.suggest()

    print(f"\nSelecting problem {sug[DIFFICULTY]['name']} \n")

    if INCLUDE_PB_LINK_IN_CONSOLE:
        print("link: ",sug[DIFFICULTY]["link"],"\n")
    
    path = SOURCE_LOCATION + sug[DIFFICULTY]['name'].strip('?!.')
    file_name = sug[DIFFICULTY]['pid'] + PROG
    print(file_name)
    file_path = os.path.join(path, file_name).replace("\\","/")
    print(file_path)
    clean_path = SOURCE_LOCATION + "'" + sug[DIFFICULTY]['name'] + "'"
    clean_file_path = os.path.join(clean_path, file_name).replace("\\","/")

    if INCLUDE_SUBMIT_COMMAND:
        submit_command = "kattis " + clean_file_path + " -f\n"
        print("Submit problem using:\n")
        print(submit_command)

    if os.path.exists(path):
        print("A directory already exists for this problem !\n")
    else:
        os.makedirs(path)
        print("The new directory is created!\n")
        with open(file_path, 'w') as f: 
            f.write(f'#{sug[0]["link"]}')

    return sug[DIFFICULTY]['pid'],file_path

def get_description(kt, pid):
    data = kt.problem(problem_ids=pid)
    description = data[0]['text']
    return description