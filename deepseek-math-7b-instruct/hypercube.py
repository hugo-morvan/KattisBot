 n = int(input())
# define a function to calculate Hamming distance (number of different bits) 
def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
a = input()
b = input()
# calculate the number of vertices between a and b 
num_vertices = hamming_distance(a, '0'*n) + n - 1
# Generator time: 4.9528 seconds