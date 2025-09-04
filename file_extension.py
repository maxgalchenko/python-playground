filename = "python_notes.txt"
print(filename)

print(filename.removesuffix(".txt"))


# for number in range(0,10)\
count_list = list(range(10, -1, -1))
# print(count_list)

# for number in count_list:
#     print(f"Current number is {number}")
#     if number == 5:
#         print('"Halfway point reached!"')


counter = 10
while counter >= 0:
    print(f"Current number is {counter}")
    if counter == 5:
        print('"Halfway point reached!"')
    counter -= 1
