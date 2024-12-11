# Read the input string
s = input()

# Find the index of the first occurrence of 'a'
index_a = s.find('a')

# Output the suffix starting from the index of 'a' to the end of the string
print(s[index_a:])