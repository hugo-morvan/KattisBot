def count_friday_the_13ths(D, M, days_in_months):
    from datetime import date
    
    # Start from the first day of the year which is a Sunday
    start_date = date(0, 1, 1)
    
    friday_count = 0
    current_day = start_date
    
    for month in range(1, M + 1):
        days_in_month = days_in_months[month - 1]
        for day in range(1, days_in_month + 1):
            if day == 13 and current_day.weekday() == 4:  # 4 corresponds to Friday
                friday_count += 1
            current_day += timedelta(days=1)
    
    return friday_count

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        D, M = map(int, input().split())
        days_in_months = list(map(int, input().split()))
        result = count_friday_the_13ths(D, M, days_in_months)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 32.7354 seconds