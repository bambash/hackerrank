
def solve(meal_cost, tip_percent, tax_percent):
    tip = round((meal_cost * tip_percent) / 100)
    tax = round((meal_cost * tax_percent) / 100)
    print(int(round(meal_cost + tip + tax)))


print(solve(10.24, 17, 5))
