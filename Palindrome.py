def is_palindrome(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Reverse the string
    reversed_str = number_str[::-1]
    
    # Check if the reversed string is equal to the original string
    if number_str == reversed_str:
        return True
    else:
        return False

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(number, "is a palindrome number.")
else:
    print(number, "is not a palindrome number.")
