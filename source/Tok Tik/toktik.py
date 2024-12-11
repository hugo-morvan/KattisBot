from collections import defaultdict

def find_most_popular_tok_tiker():
    n = int(input())
    view_counts = defaultdict(int)
    
    for _ in range(n):
        user, views = input().split()
        views = int(views)
        view_counts[user] += views
    
    most_popular_user = max(view_counts, key=view_counts.get)
    print(most_popular_user)

find_most_popular_tok_tiker()