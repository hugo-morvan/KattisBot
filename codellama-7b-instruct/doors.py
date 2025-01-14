def solve(R, lamda, w): 
    return math.ceil((math.sqrt(w*w + 4*R*R) - w) / (2*lamda))
# Generator time: 3.5834 seconds