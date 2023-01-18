positive_count = 0
negative_count = 0
odd_count = 0
even_count = 0
zero_count = 0

for i in range(20):
    num = int(input("Enter an integer: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    elif num == 0:
        zero_count +=1
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Odd numbers:", odd_count)
print("Even numbers:", even_count)
print("Zeros:", zero_count)
