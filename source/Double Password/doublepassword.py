def count_valid_sequences(password1, password2):
    n = 4
    count = 0
    
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    # Check if any digit matches in at least one position
                    if (i == password1[0] or i == password2[0]) and \
                       (j == password1[1] or j == password2[1]) and \
                       (k == password1[2] or k == password2[2]) and \
                       (l == password1[3] or l == password2[3]):
                        count += 1
                        
    return count

# Read input
password1 = input().strip()
password2 = input().strip()

# Calculate and print the result
print(count_valid_sequences(password1, password2))