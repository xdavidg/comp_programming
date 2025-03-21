recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
supplies = ["yeast", "flour", "meat"]

set_s = set(supplies)
dict_r = {}

for i in range(len(recipes)):
    dict_r[recipes[i]] = i

new_recipe = True
output = []

while new_recipe and len(output) < len(recipes):
    new_recipe = False
    for r in dict_r:
        if r == -1:
            continue
        all_ing = True
        for ingredient in ingredients[dict_r[r]]:
            if ingredient not in set_s:
                all_ing = False
        if all_ing and r not in set_s:
            output.append(r)
            set_s.add(r)
            dict_r[r] = -1
            new_recipe = True

print(output)

