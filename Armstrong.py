def is_armstrong(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Calculate the number of digits in the number
    num_digits = len(number_str)
    
    # Calculate the sum of the cubes of each digit
    sum_of_cubes = 0
    for digit in number_str:
        sum_of_cubes += int(digit) ** num_digits
    
    # Check if the sum of cubes is equal to the original number
    if sum_of_cubes == number:
        return True
    else:
        return False

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
