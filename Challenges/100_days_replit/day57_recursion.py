def factorial(number):
    if number != 1:
        return number * factorial(number - 1)
    else:
        return number


print("🌟Factorial Finder🌟\n")
number = int(input("Input a number > "))
factorial = factorial(number)

print(f"\nFactorial Result from {number} is {factorial}")
