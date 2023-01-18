string = input("Enter a string: ")

lower_count = 0
upper_count = 0
digit_count = 0
symbol_count = 0

for char in string:
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1
        
print("Lowercase letters: ", lower_count)
print("Uppercase letters: ", upper_count)
print("Digits: ", digit_count)
print("Special symbols: ", symbol_count)
