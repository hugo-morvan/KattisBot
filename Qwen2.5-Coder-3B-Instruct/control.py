def can_concoct_recipe(ingredients, used_ingredients):
    for ingredient in ingredients:
        if ingredient not in used_ingredients:
            return False
    return True

def main():
    N = int(input())
    recipes = []
    
    for _ in range(N):
        M = int(input())
        ingredients = set(map(int, input().split()))
        recipes.append((M, ingredients))
    
    used_ingredients = set()
    concocted_count = 0
    
    for M, ingredients in recipes:
        if can_concoct_recipe(ingredients, used_ingredients):
            used_ingredients.update(ingredients)
            concocted_count += 1
    
    print(concocted_count)

if __name__ == "__main__":
    main()
# Generator time: 7.5998 seconds