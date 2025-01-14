N = int(input())
A = input().split(", ")
B = input().split(", ")

print(len(set(A).intersection(B)))
# Generator time: 3.5523 seconds