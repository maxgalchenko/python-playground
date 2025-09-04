filename = "python_notes.txt"
print(filename)

print(filename.removesuffix(".txt"))

user_input = int(input())
cost = 0
if user_input <= 12:
    price = 8
elif user_input <= 64:
    price = 12
else:
    price = 10

print(f"Price is ${price}")
