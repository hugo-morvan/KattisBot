import sys
n = int(input())
recipes = []
for i in range(n):
    m, *ingredients = [int(x) for x in input().split()]
    recipes.append([m, ingredients])

def concoct_potions():
    for r in recipes:
        if all(i not in cauldron or i==0 for i in r[1]):
            yield len(cauldron) + 1
        else:
            yield None

cauldron = []
for potion, recipe in enumerate(recipes):
    if next(concoct_potions()) is not None:
        for ingredient in recipe[1]:
            cauldron.append(ingredient)
        print("Concocted", potion+1)
# Generator time: 9.9061 seconds