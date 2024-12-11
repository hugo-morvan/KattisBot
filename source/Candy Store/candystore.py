def main():
    N, Q = map(int, input().split())
    customers = {}
    
    for _ in range(N):
        name = input().split()
        first_name, last_name = name[0], name[1]
        if first_name not in customers:
            customers[first_name] = []
        customers[first_name].append(last_name)
    
    for _ in range(Q):
        initials = input().split()
        first_initial, last_initial = initials[0], initials[1]
        
        if first_initial in customers:
            matching_names = customers[first_initial]
            if len(matching_names) == 1:
                print(matching_names[0])
            elif len(matching_names) > 1:
                print("ambiguous")
            else:
                print("nobody")
        else:
            print("nobody")

if __name__ == "__main__":
    main()