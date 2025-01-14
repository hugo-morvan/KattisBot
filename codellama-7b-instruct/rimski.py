def rearrange(roman_numeral):
    result = ''
    for i, ch in enumerate(roman_numeral):
        if i % 2 == 0:
            result += ch
    return ''.join(sorted(result))

if __name__ == '__main__':
    print(rearrange(input()))
# Generator time: 4.1444 seconds