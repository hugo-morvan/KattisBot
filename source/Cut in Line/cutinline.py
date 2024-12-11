def main():
    # Read the initial lineup
    N = int(input())
    lineup = input().split()
    
    # Read the number of changes
    C = int(input())
    
    # Process each change
    for _ in range(C):
        event = input().split()
        if event[0] == "cut":
            cut_name, front_name = event[1], event[2]
            lineup.insert(lineup.index(front_name), cut_name)
        elif event[0] == "leave":
            leave_name = event[1]
            lineup.remove(leave_name)
    
    # Output the final lineup
    print("\n".join(lineup))

if __name__ == "__main__":
    main()