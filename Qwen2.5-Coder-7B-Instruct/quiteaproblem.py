while True:
    try:
        line = input().strip()
        if 'problem' in line.lower():
            print('yes')
        else:
            print('no')
    except EOFError:
        break
# Generator time: 3.3829 seconds