
def main():
    N, Q = map(int, input().split())
    customers = {}
    
    # Read customer names
    for _ in range(N):
        name = input().strip()
        initials = name.split()[0][0] + name.split()[1][0]
        if initials in customers:
            customers[initials].append(name)
        else:
            customers[initials] = [name]
    
    # Read queries
    for _ in range(Q):
        initials = input().strip()
        if initials in customers:
            if len(customers[initials]) == 1:
                print(customers[initials][0])
            elif len(customers[initials]) > 1:
                print("ambiguous")
            else:
                print("nobody")
        else:
            print("nobody")

if __name__ == "__main__":
    main()
