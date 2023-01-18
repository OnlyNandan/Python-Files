my_list = []

for i in range(10):
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        my_list.append(num)

print("List of even integers:", my_list)
