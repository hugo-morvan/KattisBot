def count_correct_answers(sequence, correct):
    return sum(1 for a, b in zip(sequence, correct) if a == b)

def main():
    N = int(input())
    correct_answers = input()
    
    adrian_sequence = "ABC" * (N // 3 + 1)
    bruno_sequence = "BAC" * (N // 3 + 1)
    goran_sequence = "CCA" * (N // 3 + 1)
    
    adrian_correct = count_correct_answers(adrian_sequence, correct_answers)
    bruno_correct = count_correct_answers(bruno_sequence, correct_answers)
    goran_correct = count_correct_answers(goran_sequence, correct_answers)
    
    max_correct = max(adrian_correct, bruno_correct, goran_correct)
    
    print(max_correct)
    
    if max_correct == adrian_correct:
        print("Adrian")
    if max_correct == bruno_correct:
        print("Bruno")
    if max_correct == goran_correct:
        print("Goran")

if __name__ == "__main__":
    main()