word = input()
if 'b' not in word and 'k' not in word:
    print("none")
elif word.count('b') > word.count('k'):
    print("boba")
elif word.count('k') > word.count('b'):
    print("kiki")
else:
    print("boki")