 def hamming_distance(s1, s2): 
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
# Generator time: 3.3631 seconds