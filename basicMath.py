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
   
   
def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
        
    