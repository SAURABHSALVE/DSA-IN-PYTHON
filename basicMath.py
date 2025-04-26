"""
# This code checks if a number is a palindrome or not.
# A palindrome is a number that remains the same when its digits are reversed. """ 

"""def palindrome(num):
    rev = 0
    temp = num
    n = len(str(num))
    for i in range(n):
        digit = temp%10
        rev = rev*10 + digit
        temp = temp//10
    return num

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if palindrome(num):
        print(f"{num} is a palindrome number")
    else:
        print(f"{num} is not a palindrome number")  """
        
        
## code to check if a number is prime or not
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
        
  
   """
   
   ## code to find the factorial of a number   
# The factorial of a number n is the product of all positive integers less than or equal to n.
# It is denoted by n! and is defined as:
# n! = n * (n-1) * (n-2) * ... * 1
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120 
# The factorial of 0 is defined to be 1.
# Factorial can be calculated using recursion or iteration.
# Here is a simple recursive implementation of factorial in Python:

"""def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")"""


## code to find the sum of digits of a number
# The sum of digits of a number is the sum of all its individual digits.
# For example, the sum of digits of 123 is 1 + 2 + 3 = 6.
# The sum of digits can be calculated using a loop or recursion.
# Here is a simple implementation of sum of digits in Python:
    
"""def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = sum_of_digits(num)
    print(f"The sum of digits of {num} is {result}")"""
        