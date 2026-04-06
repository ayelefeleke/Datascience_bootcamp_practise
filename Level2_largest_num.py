print("Enter the list of numbers")
numbers = input()

# Replace commas with spaces, then split into parts
numbers = numbers.replace(",", " ").split()

# Convert each number from string to integer
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Assume the first number is the largest
largest = numbers[0]

# Compare each number with the current largest
for num in numbers:
    if num > largest:
        largest = num

print("The Largest number is:", largest)