def calculate_distance():
    while True:
        n = int(input())
        if n == -1:
            break
        
        total_distance = 0
        for _ in range(n):
            speed, time = map(int, input().split())
            total_distance += speed * (time - total_time)
            total_time = time
        
        print(f"{total_distance} miles")

calculate_distance()