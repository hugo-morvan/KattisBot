def find_smallest_word(word):
    n = len(word)
    min_word = "z" * 51
    
    for i in range(1, n-1):
        for j in range(i+1, n):
            first_part = word[:i][::-1]
            second_part = word[i:j][::-1]
            third_part = word[j:][::-1]
            new_word = first_part + second_part + third_part
            if new_word < min_word:
                min_word = new_word
    
    print(min_word)

# Input the word from Mario
input_word = input()
find_smallest_word(input_word)
# Generator time: 6.0440 seconds