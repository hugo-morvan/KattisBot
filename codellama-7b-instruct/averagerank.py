n, w = list(map(int, input().split()))
scores = []
for _ in range(w):
    k, *competitors = list(map(int, input().split()))
    for comp in competitors:
        if comp not in scores:
            scores.append(comp)
        else:
            scores[scores.index(comp)] += 1

for i in range(n):
    print((scores.index(i)+1)/(w+1))
# Generator time: 4.8484 seconds