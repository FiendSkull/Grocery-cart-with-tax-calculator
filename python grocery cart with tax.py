# Grocery items with tax calculator

foods = []
quantities = []
prices = []
print("Your Grocery Cart🛒")
while True:
    food = input("Enter the name of the food (to checkout type 'done'): ")
    if food.lower() == "done":
        break
    else:
        quantity = int(input(f"Enter the quantity of '{food}': x"))
        price = float(input(f"Enter the price of '{food}': $"))
        foods.append(food)
        quantities.append(quantity)
        prices.append(price)

tax = float(input("Enter the amount of Tax: "))
print("________________________")
print("_______Your Items_______")

for food, quantity, price in zip(foods, quantities, prices):
    total = quantity * price
    print(f"{food:<12} x{quantity:<8} ${price:>2.2f}  ${total:>2.2f}")

print("________________________")
subtotal = sum(quantity * price for quantity, price in zip(quantities, prices))
tax1 = subtotal * (tax / 100)
total1 = subtotal + tax1

print(f"Subtotal: {f"${subtotal:.2f}":>12}")
print(f"Tax({tax}%):{f"${tax1:.2f}":>12}")
print(f"Total:    {f"${total1:.2f}":>12}")
