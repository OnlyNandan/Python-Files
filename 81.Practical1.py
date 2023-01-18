n=int(input("Enter the number of elements in the list:- " ))
lst=[]
for i in range (0,n):
    lst+=[(input("Enter the number:- "))]
    lst[i]=int(lst[i])
if lst == lst[::-1]:
    print("Elements of the list are same when read from front or back.")
else:
    print("Elements of the list are not same when read from front or back.")
