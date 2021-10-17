# WHILE LOOPS
# num = 0
# while num <= 100:
#     print(num)
#     num += 10

# guess = None
# target = 81

# while guess != target:
#     guess = input("\nEnter your guess: ")
#     guess = int(guess)
#     if guess > target:
#         print("Your guess is too high. Guess again!")
#     elif guess < target:
#         print("Your guess is too low. Guess again!")
    

# print("You got it! Great guessing!")





# FOR LOOPS

# snacks = ['candy corn', 'apple', 'grapes', 'popcorn']

# for snack in snacks:
#     print("I ate a", snack)


# # RANGES

# for num in range(10):
#     print(num)

# numbers = list(range(2,11,2))
# print(numbers)

#FUNCTIONS

# def is_even(num):
#     if num % 2 == 0:
#         print(f"{num} is even!")
#     else:
#         print(f"{num} is odd!")

# given_number = input("Please give me a number: ")
# given_number = int(given_number)
# is_even(given_number)

def do_math( num1, num2, probelm='+'):
    """Just doing some math with this one. Add, subtract, multipy or divide two numbers."""
    if probelm == '+':
        return num1 + num2
    elif probelm == '-':
        return num1 - num2
    elif probelm == '*':
        return num1 * num2
    elif probelm == '/':
        return num1 / num2
# Can put the arguments in out of order, as long as you define them
print(do_math(probelm="*", num2=3, num1=5))

# You can have the arguments in a function default to something so that you can leave the argument out of the function call. Default items cannot be first, have to be last. See line 53.

# Use dir() to see all methods and attributes available on a particular object. 
# syntax is : dir([object])

# Line 54 is an example of how to write documentation for functions we make up. Call help() on any function to see this information about it.
