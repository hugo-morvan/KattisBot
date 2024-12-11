def count_unique_cities():
    T = int(input())
    for _ in range(T):
        n = int(input())
        cities = set()
        for _ in range(n):
            city = input()
            cities.add(city)
        print(len(cities))

count_unique_cities()