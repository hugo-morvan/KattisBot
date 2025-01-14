import sys
input = sys.stdin.readline
def find_all(item, l):
    return [i for i, x in enumerate(l) if x == item]
def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        stations = list(range(1, N+1))
        edges = [tuple(map(int, input().split())) for _ in range(M)]
        distances = {}
        for i in range(N):
            for j in range(i, N):
                if (i == j): distances[(i, i)] = 0
                else:
                    dist = float('inf')
                    for e in edges:
                        if ((e[0] == i and e[1] == j) or (e[0] == j and e[1] == i)): dist = min(dist, int(e[2]))
                    distances[(i,j)] = dist
        
        new_stations = []
        new_edges = []
        for s in stations:
            if len([x for x in find_all(s, [x[0] for x in edges])]) <= 2 and len([x for x in find_all(s, [x[1] for x in edges])]) <= 2: continue
            new_stations.append(s)
        
        for e in edges:
            if (e[0] in new_stations and e[1] in new_stations): new_edges.append(tuple((new_stations.index(x) for x in e)))
            
        print()
        print(len(new_stations))
        for n in new_stations:
            print(n, end=' ')
        
        for e in new_edges:
            print(e[0]+1, e[1]+1, distances[(e[0], e[1])], sep=' ')

if __name__ == '__main__': main()
# Generator time: 12.1341 seconds