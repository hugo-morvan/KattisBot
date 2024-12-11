def is_canadian(sentence):
    # Check if the sentence ends with 'eh?'
    if sentence.endswith('eh?'):
        return "Canadian!"
    else:
        return "Imposter!"

# Read input from the user
input_sentence = input()

# Determine if the suspect is Canadian or an imposter
result = is_canadian(input_sentence)

# Print the result
print(result)