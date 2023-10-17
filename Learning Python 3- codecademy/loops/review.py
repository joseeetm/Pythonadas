# 1- Create a list called single_digits that consists of the numbers 0-9 (inclusive).
single_digits=list(range(0,10))
print(single_digits)
# 2-Create a for loop that goes through single_digits and prints out each one.
squares = []
for digit in single_digits:
    print(digit)
    squares.append(digit**2)
print(squares)
# 3-Before the loop, create a list called squares. Assign it to be an empty list to begin with.
# 4-Inside the loop that iterates through single_digits, append the squared value of each element
# of single_digits to the list squares. You can do this before or after printing the element.

# Create the list cubes using a list comprehension on the single_digits list. Each element of cubes
# should be an element of single_digits taken to the third power.
cubes= [digit ** 3 for digit in single_digits]
print(cubes)