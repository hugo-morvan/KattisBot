p = int(input())
random_sequence = input()

def search_for_triple_correlation(sequence):
    for i in range(len(sequence) - 2):
        first_value = sequence[i]
        second_value = sequence[i + 1]
        third_value = sequence[i + 2]

        if first_value == 4 and second_value == 4:
            print("4(1)4(3)3")
        elif first_value == 7 and second_value == 7:
            print("7(1)7(3)1")
        elif third_value == 9 and (first_value, second_value) == (5, 0):
            print("5(2)9(2)")
        elif first_value == 5 and second_value == 8:
            print("5(3)8(1)")
        elif third_value == 7 and (first_value, second_value) == (2, 6):
            print("2(1)7(2)")
        else:
            continue

if len(random_sequence) >= 40:
    search_for_triple_correlation(random_sequence)
else:
    print("random sequence")
# Generator time: 8.9434 seconds