# Exercise #1: What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# We get a name error that 'foo' is not defined. This happens because it is out of the scope of the rest of the code and only defind in the function.


# Exercise #2: Take a look at this code snippet. What does this program print?

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# My answer: it will print qux 
# Wrong! Shadow variable is created in the function itself so we never actually change the variable foo in the global scope. 

# Exercise #3: Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

def multiply(first_number, second_number):
    return first_number * second_number

result = multiply(first_number, second_number)

print(f'{first_number} * {second_number} = {result}')


# Exercise #4: Consider this code:

def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)

# Identify the following items in that code:
# function name - multiply_numbers
# function arguments - 2, 3, 4
# function definition - everything on lines 1-3
# function body - everything indented 
# function parameters - num1, num2, num3
# function invocation - multiply_numbers(2, 3, 4)
# function return value - result or 24
# all identifiers - multiply_numbers, num1, num2, num3, result and product 

# Exercise #5: What does the following code print?

def scream(words):
    return words + '!!!!'

scream('Yipeee')

# Doesn't print anything, there is no print call. 

# Exercise #6: What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# Still prints nothing, the print function is after return so we will have already exited the function before we print anything. 

# Exercise #7: Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# It will give an error because there are not enough arguments when we call the function. 

# Exercise #8: Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# This code will also raise an error as we have too many arguments. 

# Exercise #9: Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# It will print all three of the argument values. 

# Exercise #10: Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# The code will print 42, 3.141592 and 2. 

# Exercise #11: Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# It will print 42, 3, 2. 

# Exercise #12: Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# Raise an error because we are missing the first argument and the parameter doesn't have a default. 

# Exercise #13: Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# This will raise an error because defaults have to be set as the last parameter. 

# Exercise #14: Identify all of the identifiers on each line of the following code. 

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Identifiers = multiply, left, right, get_num, prompt, first_number, second_number, product, float, input and print 

#Exercise #15: Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply - global 
# left - local 
# right - local
# get_num - global
# prompt - local 
# first_number - global
# second_number - global
# product - global
# float - built-in
# input - built-in
# print - built-in

#Exercise #16: In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# function names - multiply (1, 9), gen_num (4, 7, 8), float (5), input (5), print (10)
# parameters - left (1), right (1), prompt (4)

# Exercise #17: Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# function names - say, print, input, max, .upper, .lower
# method names - .upper, .lower
# built in function names - print, input 

# Exercise #18: The following function returns a list of the remainders of dividing the numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6] - # True
numbers_2 = [1, 2, 4, 5] - # True
numbers_3 = [0, 3, 6] - # False
numbers_4 = [] - # False

# Exercise #19: The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
