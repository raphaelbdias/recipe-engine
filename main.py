import json

with open("recipes.json", "r", encoding="utf-8") as file:
    recipes = json.load(file)
ingred = ",\n ".join(recipes["reYog1"]["ingredients"])
print(f"Name of the recipe: {recipes["reYog1"]["name"]} \n Ingredients: {ingred}"


)          