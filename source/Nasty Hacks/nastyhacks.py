def main():
    n = int(input())
    results = []
    
    for _ in range(n):
        r, e, c = map(int, input().split())
        
        if e > r + c:
            results.append("advertise")
        elif e < r + c:
            results.append("do not advertise")
        else:
            results.append("does not matter")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()