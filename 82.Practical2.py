lst = []

for i in range(10):
    lst.append(int(input("Enter an element: ")))

lst = list(set(lst))

print("List after removing all repeated elements: ", lst)
