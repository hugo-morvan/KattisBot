import sys

def calculate_yarn_needed(n, m, recipe):
    yarn_costs = {
        '.': 20,
        'O': 10,
        '/': 25,
        '\\': 25,
        'A': 35,
        '^': 5,
        'v': 22
    }
    
    total_yarn = 0
    for row in recipe:
        for char in row:
            total_yarn += yarn_costs[char]
    
    return total_yarn

if __name__ == "__main__":
    n, m = map(int, input().split())
    recipe = [input().strip() for _ in range(n)]
    
    yarn_needed = calculate_yarn_needed(n, m, recipe)
    print(yarn_needed)