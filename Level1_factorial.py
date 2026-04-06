
# Ask the user to enter input
print("Enter a number to compute its factorial:")
n = int(input())  # it try to convert input to integer
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # Multiply factorial by current i

    print("Factorial of" ,n, "is:", factorial)