n = int(input("Enter the number of elements in the series: "))

a, b = 0, 1

print("The Fibonacci series is:")
for i in range(n):
    print(a, end=", ")
    a, b = b, a + b
