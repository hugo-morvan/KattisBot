def tree(N,A_i,B_i,X_i):
    # Write your code here
    for i in range (N-1) :
        A[i] = A_i[i]; B[i] = B_i[i]; X[i] = X_i[i];
    
    MIN = 10**9;
    for i in range(N):
        for j in range (A[i],B[i]+1):
            MIN = min(MIN,X[j]);
    if MIN == 10**9: return -1;
    
    a = 1; b = 1;
    for i in range(N):
        for j in range (A[i],B[i]+1):
            if X[j] == MIN:
                a *= A[i]; b *= B[i]; break;
    
    while b % a != 0:
        a += 1;
        
    return str(a)+'/'+str(b);
# Generator time: 7.3782 seconds