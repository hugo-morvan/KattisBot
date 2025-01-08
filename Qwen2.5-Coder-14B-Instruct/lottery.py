from math import comb

def calculate_probability(m, n, t, p):
    if p <= n * t:
        total_ways = comb(m, n)
        ways_to_win_enough_tickets = 0
        
        for i in range(max(0, p - t * (n - 1)), min(p, t) + 1):
            ways_to_choose_winners_with_i_tickets = comb(n, i)
            ways_to_choose_non_winners = comb(m - n, p - i)
            ways_to_win_enough_tickets += ways_to_choose_winners_with_i_tickets * ways_to_choose_non_winners
        
        probability = ways_to_win_enough_tickets / total_ways
    else:
        probability = 0
    
    return probability

m, n, t, p = map(int, input().split())
print(f"{calculate_probability(m, n, t, p):.9f}")
# Generator time: 25.2439 seconds