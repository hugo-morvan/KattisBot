def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    recipes = []
    index = 1
    
    for i in range(N):
        M = int(data[index])
        ingredients = list(map(int, data[index + 1:index + 1 + M]))
        recipes.append(ingredients)
        index += 1 + M
    
    concocted_count = 0
    used_ingredients = set()
    cauldrons = []
    
    for recipe in recipes:
        can_concoct = True
        
        # Check if the recipe can be concocted with current ingredients and cauldrons
        required_ingredients = set(recipe)
        
        for i, cauldron in enumerate(cauldrons):
            if len(required_ingredients.intersection(cauldron)) == len(cauldron) and len(required_ingredients.difference(cauldron)) > 0:
                continue
            else:
                required_ingredients -= cauldron
        
        if len(required_ingredients & used_ingredients) > 0:
            can_concoct = False
        
        if can_concoct:
            concocted_count += 1
            used_ingredients |= set(recipe)
            new_cauldron = set(recipe)
            
            # Combine cauldrons that are not needed anymore
            combined_cauldrons = []
            for cauldron in cauldrons:
                if len(cauldron & required_ingredients) > 0 and len(cauldron - required_ingredients) == 0:
                    new_cauldron |= cauldron
                else:
                    combined_cauldrons.append(cauldron)
            
            combined_cauldrons.append(new_cauldron)
            cauldrons = combined_cauldrons
    
    print(concocted_count)

if __name__ == "__main__":
    main()
# Generator time: 54.8955 seconds