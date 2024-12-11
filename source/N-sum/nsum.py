def sum_n_integers():
    N = int(input())
    numbers = list(map(int, input().split()))
    total_sum = sum(numbers)
    print(total_sum)

sum_n_integers()