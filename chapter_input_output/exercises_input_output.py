# Exercise #1: Write a program named greeter.py. The program should ask for your name, then output Hello, NAME! Where NAME is the name you entered.
NAME = input("What's your name? ")
print(f'Hello, {NAME}!')

#Exercise #2: Modify the greeter.py program to ask for the user's first and last names separately, then greet the user with their full name. 
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
print(f'Howdy, {first_name} {last_name}!')

# Exercise #3: Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30, and 40 years from now.
age = int(input('How old are you? '))
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')