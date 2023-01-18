my_list = []
n=int(input("Enter the number of elements in the list:- "))
for i in range(n):
    num = int(input("Enter an integer: "))
    my_list.append(num)

largest = max(my_list)
smallest = min(my_list)

print("Largest element:", largest)
print("Smallest element:", smallest)
