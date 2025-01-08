def main():
    N = int(input())
    days = set()
    
    for _ in range(N):
        s_i, t_i = map(int, input().split())
        for day in range(s_i, t_i + 1):
            days.add(day)
    
    print(len(days))

if __name__ == "__main__":
    main()
# Generator time: 12.3999 seconds