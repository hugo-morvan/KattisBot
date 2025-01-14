def travel_story(trips, queries):
    ans = []
    for q in queries:
        s = q[0]
        k = q[1]
        ys = [y for (s', y) in trips if s == s']
        ans.append(ys[k-1])
    return ans
# Generator time: 6.2388 seconds