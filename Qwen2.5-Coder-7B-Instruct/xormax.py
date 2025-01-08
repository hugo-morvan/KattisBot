def max_xor_subset(n, nums):
    result = 0
    for num in nums:
        result |= num
    return result

# Input reading
n = int(input())
nums = list(map(int, input().split()))

# Output the result
print(max_xor_subset(n, nums))
# Generator time: 4.3887 seconds