def calculate_sum_of_powers(N):
    total_sum = 0
    for _ in range(N):
        P_i = int(input())
        total_sum += P_i
    print(total_sum)

N = int(input())
calculate_sum_of_powers(N)