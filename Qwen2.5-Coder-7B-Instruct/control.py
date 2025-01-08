def concoct_potions(N):
    recipes = []
    for _ in range(N):
        recipe = list(map(int, input().split()))
        recipes.append(recipe)

    ingredients_used = set()
    cauldron_contents = []

    def can_concoct_recipe(recipe):
        needed_ingredients = set(recipe[1:])
        if needed_ingredients.issubset(ingredients_used):
            return True
        for content in cauldron_contents:
            if needed_ingredients.issubset(content):
                ingredients_used.update(content)
                return True
        return False

    concocted_count = 0
    for recipe in recipes:
        if can_concoct_recipe(recipe):
            concocted_count += 1
            ingredients_used.update(set(recipe[1:]))
            cauldron_contents.append(set(recipe[1:]))

    print(concocted_count)

# Read input and call the function
N = int(input())
concoct_potions(N)
# Generator time: 8.1827 seconds