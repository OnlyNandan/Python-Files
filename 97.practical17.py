user_input = input("Enter a list of numbers, separated by commas: ")
numbers = [int(x) for x in user_input.split(",")]
for number in numbers:
    print(number)
