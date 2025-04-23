foods = []
quantites = []
prices = []

while True:
    food = input("Enter the name of the food (to checkout type 'done'): ")
    if food.lower() == "done":
        break
    else:
        quantity = int(input(f"Enter the quantity of '{food}': x"))
        price = float(input(f"Enter the price of '{food}': $"))
        foods.append(food)
        quantites.append(quantity)
        prices.append(price)


print("---Restaurant Receipt---")
for food, quantity, price in zip(foods, quantites, prices):
    total = quantity * price
    print(f"{food:<12} {quantity:>8}   {price:>6.2f}   {total:>6.2f}")

print("------------------------")
subtotal = sum(quantity * price for quantity, price in zip(quantites, prices))
tax = subtotal * 0.05
total1 = subtotal + tax

print(f"Subtotal: ${subtotal:>10.2f}")
print(f"Tax (5%): ${tax:>10.2f}")
print(f"Total:    ${total1:>10.2f}")
