T = int(input()) # number of cases
for t in range(T): # for each case
    N = int(input()) # number of contestants
    s = [float(x) for x in input().split()] # point values from judges
    
    # if all points are equal, everyone is safe
    if len(set(s)) == 1:
        print("Case #{}: ".format(t+1), end="")
        for i in range(N):
            print(0.0, end=" ")
        print()
        continue
    
    # get the maximum point value and its index
    s_max = max(s)
    m_max = s_max * 100 / (s_max + 1)
    j_max = s.index(s_max)
    
    # if the max point is greater than 1, everyone is safe
    if s_max > 1:
        print("Case #{}: ".format(t+1), end="")
        for i in range(N):
            print(0.0, end=" ")
        print()
        continue
    
    # sort the contestant points by their fraction of audience votes
    s_sorted = sorted([(x, i) for (i, x) in enumerate(s)], key=lambda z: -z[0])
    
    # get the index of the minimum point value
    j_min = s_sorted[0][1]
    
    # find the minimum percentage required to avoid elimination
    m_min = 0.0
    for i in range(N):
        if i == j_max:
            continue
        m_i = (s[j_min] * 100) / (s[j_min] + s[i])
        if m_i < m_min or m_min == 0.0:
            m_min = m_i
    print("Case #{}: ".format(t+1), end="")
    for i in range(N):
        print(m_min, end=" ")
    print()
# Generator time: 12.5141 seconds