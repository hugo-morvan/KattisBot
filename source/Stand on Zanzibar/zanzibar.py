def main():
    T = int(input())
    
    for _ in range(T):
        sequence = list(map(int, input().split()))[:-1]
        
        lower_bound = 0
        current_turtles = 1
        
        for i in range(1, len(sequence)):
            if sequence[i] > 2 * current_turtles:
                lower_bound += sequence[i] - 2 * current_turtles
                current_turtles = sequence[i]
            else:
                current_turtles += sequence[i]
        
        print(lower_bound)

if __name__ == "__main__":
    main()