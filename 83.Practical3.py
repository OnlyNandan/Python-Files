lst = []

n = int(input("Enter the length of the list: "))

for i in range(n):
    lst.append(int(input("Enter an element: ")))

highest_value = max(lst)

lst.remove(highest_value)

next_highest_value = max(lst)

additive_entity = highest_value - next_highest_value

highest_index = lst.index(next_highest_value)
lst[highest_index] = (next_highest_value, additive_entity)

print("List after splitting the highest value: ", lst)
