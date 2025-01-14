def find_min_copy(S):
    if len(S) == 0:
        return 0
    
    min_len = 100000000 # arbitrarily large number
    for i in range(len(S)):
        prefix = S[:i]
        suffix = S[i:]
        
        if len(suffix) >= min_len:
            break
        
        if not is_substring_in(T, prefix):
            continue
        
        # check if we can reach the end of T given the current substring
        if len(suffix) == 0 or is_substring_in(T, suffix):
            min_len = i
    
    return min_len
# Generator time: 19.0953 seconds