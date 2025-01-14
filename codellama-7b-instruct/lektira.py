import sys
input_word = input()
if len(input_word) == 1:
    print(input_word)
else:
    words = input_word.split(' ')
    words = [sorted(list(i), reverse=True) for i in words]
    words = ''.join([i[0]+i[1]+i[2] for i in words])
    print(words)
# Generator time: 10.4138 seconds