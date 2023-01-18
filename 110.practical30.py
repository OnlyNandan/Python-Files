my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4)
repeated_items = []
for item in my_tuple:
    if my_tuple.count(item) > 1:
        repeated_items.append(item)
repeated_items = list(set(repeated_items))
print("The repeated items in the tuple are:", repeated_items)
