def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return num*factorial(num-1)
    
number = int(input("Enter number: "))
print(f"Factorial of given number is: {factorial(number)}")