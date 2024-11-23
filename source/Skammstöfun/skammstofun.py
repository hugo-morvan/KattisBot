def generate_abbr():
    n = int(input())
    words = input().split()
    abbr = []
    
    for word in words:
        if word[0].isupper():
            abbr.append(word[0])
    
    print(''.join(abbr))

generate_abbr()