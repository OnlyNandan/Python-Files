my_list = []

for i in range(10):
    num = int(input("Enter an integer: "))
    my_list.append(num)

reverse_list = my_list.copy()
reverse_list.reverse()

print("Original list:", my_list)
print("Reversed list:", reverse_list)
