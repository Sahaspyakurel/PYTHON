def is_perfect_square(number):
    sqrt = int(number ** 0.5)
    return sqrt * sqrt == number

def is_fibonacci(number):
    # Check if the number is a perfect square of (5 * n^2 + 4) or (5 * n^2 - 4)
    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is a Fibonacci number
if is_fibonacci(number):
    print(number, "is a Fibonacci number.")
else:
    print(number, "is not a Fibonacci number.")
