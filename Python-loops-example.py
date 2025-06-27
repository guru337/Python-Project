# Example 1: For loop over a list
# Iterates over each fruit in the list and prints it
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: While loop with a counter
# Prints the count value until it reaches 3
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# Example 3: For loop with range
# Prints numbers from 0 to 4
for i in range(5):
    print("Number:", i)

# Example 4: Nested loops
# Prints all combinations of i and j for 0 and 1
for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

# Example 5: Looping through a dictionary
# Prints keys and values
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")

# Example 6: List comprehension with loop
# Creates a list of squares from 0 to 4
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# Example 7: Loop with break statement
# Stops loop when number is 3
for num in range(10):
    if num == 3:
        break
    print("Break example:", num)

# Example 8: Loop with continue statement
# Skips printing number 3
for num in range(5):
    if num == 3:
        continue
    print("Continue example:", num)

# Example 9: Enumerate in loop
# Prints index and value from a list
colors = ["red", "green", "blue"]
for idx, color in enumerate(colors):
    print(f"Color {idx}: {color}")

# Example 10: Looping over two lists with zip
# Prints pairs of fruit and color
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "dark red"]
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")

# Example 11: Nested list comprehension
# Creates a multiplication table (2D list)
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication table:", table)

# Example 12: Loop with else clause
# Prints numbers, then prints "Done" after loop ends
for i in range(3):
    print("Else example:", i)
else:
    print("Loop finished!")

# Example 13: Infinite loop with break
# Loops forever until break condition is met
n = 0
while True:
    print("Infinite loop example:", n)
    n += 1
    if n >= 3:
        break

# Example 14: Looping through a string
# Prints each character in the string
for char in "Python":
    print("Char:", char)

# Example 15: Nested loops for pattern printing
# Prints a right-angled triangle of stars
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()