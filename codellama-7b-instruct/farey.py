for _ in range(int(input())):
    n = int(input())
    cnt = 1
    for i in range(2,n):
        if(i % 6 == 0 or i % 3 == 0):
            continue
        else:
            cnt += 1
    print(f"{n} {cnt}")
# Generator time: 6.8576 seconds