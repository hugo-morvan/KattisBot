def verify_deletion(N, original, modified):
    # Check if each bit is switched N times
    for i in range(len(original)):
        if (original[i] == '0' and modified[i] == '1') or (original[i] == '1' and modified[i] == '0'):
            return "Deletion failed"
    return "Deletion succeeded"

# Read input
N = int(input())
original = input()
modified = input()

# Verify deletion
result = verify_deletion(N, original, modified)
print(result)