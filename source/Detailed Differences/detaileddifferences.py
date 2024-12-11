def main():
    import sys

    def compare_strings(str1, str2):
        result = []
        for char1, char2 in zip(str1, str2):
            if char1 == char2:
                result.append('.')
            else:
                result.append('*')
        return ''.join(result)

    num_tests = int(input())
    for _ in range(num_tests):
        line1 = input()
        line2 = input()
        diff = compare_strings(line1, line2)
        print(line1)
        print(line2)
        print(diff)
        print()

if __name__ == "__main__":
    main()