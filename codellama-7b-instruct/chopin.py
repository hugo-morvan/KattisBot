while True:
    try:
        line = input()
    except EOFError:
        break
    
    note,tonality = line.split()
    if tonality == 'major':
        print('Case 1: {}'.format(note))
    else:
        if note in ['A#','Bb']:
            print('Case 2: A')
        elif note in ['C#','Db']:
            print('Case 3: C')
        elif note in ['D#','Eb']:
            print('Case 4: D')
        elif note in ['F#','Gb']:
            print('Case 5: F')
        elif note in ['G#','Ab']:
            print('Case 6: G')
        else:
            print('Case 7: UNIQUE')
# Generator time: 6.7064 seconds