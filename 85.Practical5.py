string = input("Enter a string: ")

lower_chars = [c for c in string if c.islower()]
upper_chars = [c for c in string if c.isupper()]

sorted_string = ''.join(lower_chars + upper_chars)

print("Sorted string: ", sorted_string)
