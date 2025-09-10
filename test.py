shopping_cart: list[str] = []

shopping_cart.append("apple")
shopping_cart.append("banana")
shopping_cart.append("milk")


print("Shopping Cart:")
for item in shopping_cart:
    print(item)


l = [1, 2, 3, 4, 5]
l.clear()
print(l)

diction = {12: 123}

print(diction.get(123321321, 123))


