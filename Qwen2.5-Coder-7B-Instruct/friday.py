from datetime import datetime, timedelta

def count_fridays_the_13th(D, M, d):
    friday_count = 0
    current_day = datetime(2024, 1, 1)  # Start from January 1st of the specified year (assuming it starts on Sunday)
    
    for month in range(M):
        days_in_month = d[month]
        for day in range(1, days_in_month + 1):
            if current_day.day == 13 and current_day.weekday() == 4:  # Check if the day is Friday (weekday() returns 4 for Friday)
                friday_count += 1
            current_day += timedelta(days=1)
    
    return friday_count

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        D, M = map(int, input().split())
        d = list(map(int, input().split()))
        
        result = count_fridays_the_13th(D, M, d)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 9.3236 seconds