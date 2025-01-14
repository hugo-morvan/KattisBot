def solve(S):
    for i in range (len(S)-1):
        if S[i] == "":
            continue
        for j in range(i+1, len(S)):
            S[i] += S[j]
            S[j] = ""
    return S[-1]
# Generator time: 4.0506 seconds