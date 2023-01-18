my_list = []

for i in range(10):
    num = int(input("Enter an integer: "))
    my_list.append(num)

my_list = list(set(my_list))

print("List with unique elements:", my_list)
