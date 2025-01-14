from itertools import permutations, combinations

def get_difficulties(N, D):
    # Get all unique pairs of difficulty and number of problems
    D = list(combinations(range(1, N+1), 2))
    return D

def get_discarded_problems(Q, D):
    discarded_problems = []
    
    for i in range(Q):
        t, d = map(int, input().split())

        if t == 1: # Find the discarded problem with difficulty strictly greater than d.
            discarded_problems.extend([p[0] for p in D if p[1] > d])
        else: # Find the discarded problem with difficulty not strictly greater than d.
            discarded_problems.extend([p[0] for p in D if p[1] <= d])
    
    return discarded_problems

def main():
    N, Q = map(int, input().split())

    # Get all unique pairs of difficulty and number of problems
    D = get_difficulties(N, D)
    
    # Find the discarded problems
    discarded_problems = get_discarded_problems(Q, D)
    
    # Print the discarded difficulties
    for d in discarded_problems:
        print(d)

if __name__ == '__main__':
    main()
# Generator time: 13.9001 seconds