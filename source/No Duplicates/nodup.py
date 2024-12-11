def check_repeats(phrase):
    words = phrase.split()
    seen = set()
    for word in words:
        if word in seen:
            return "no"
        seen.add(word)
    return "yes"

# Read input
input_phrase = input()

# Check for repeats and print output
print(check_repeats(input_phrase))