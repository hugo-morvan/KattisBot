from collections import Counter
if __name__ == '__main__':
    #taking input
    s = input()

    #counting characters and creating a counter
    count_dict = Counter(s)

    #finding minimum length of the string
    min_length = 0
    for k, v in count_dict.items():
        if v%2 != 0:
            min_length += 1
        else:
            min_length += v//2

    #finding maximum length of the string
    max_length = sum(count_dict.values())

    print(min_length, max_length)
# Generator time: 5.7002 seconds