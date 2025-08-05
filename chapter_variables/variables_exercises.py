# Exercise #1: Classify the following potential non-constant variable names as idiomatic, non-idiomatic or illegal:

# My try

# index = idiomatic - style is fine 
# CatName = idiomatic - correct use of PascalCase
# lazy_dog = idiomatic - fine
# quick_Fox = non-idiomatic - breaking PascalCase with the whacky caps on Fox
# 1stCharacter = illegal - can't start with a number
# operand2 = idiomatic - fine
# BIG_NUMBER = idiomatic - fine, correct use of SCREAMING_SNAKE_CASE
# pi symbol = illegal - can't have special characters

# graded

# index = idiomatic - correct
# CatName = non-idiomatic - More stupid LS discrepancies, my answer is right per the book. Dissapointing. 
# lazy_dog = idiomatic - correct
# quick_Fox = non-idiomatic - breaking PascalCase with the whacky caps on Fox - correct
# 1stCharacter = illegal - can't start with a number - correct
# operand2 = idiomatic - fine - correct
# BIG_NUMBER = idiomatic - you can user uppercase letters for class names - why are these answers so different than the material presented in the book? Dissapointing.
# pi symbol = illegal - also doesn't track with the book. Seriously? 

# Ok this section is pretty stupid.
# Exercise #2: function names: same. 

# Exercise #3: constant names:

# index = non
# CatName = non
# snake_case = non
# LAZY_DOG3 = idiomatic
# 1ST = illegal
# operand2 = non
# BIG_NUMBER = idiomatic
# pi = non

# Exercise #4: class names:

# index = non
# CatName = idiomatic
# lazy_dog = non  
# 1ST = illegal
# operand2 = non
# BIG_NUMBER = idiomatic
# pi = non

# Exercise #5: Write a program named greeter.py that greets 'Victor' three times. Your program should use a varable and not hardcode hte string value 'Victor' in each greeting. 
name = 'Victor'
print('Good Morning, ' + name + '.')
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')

# Exercise #6: Write a program name age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, 40 years from now. 
age = 22
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# Exercise #7: What happens when you run the following code? Why? 
# It prints out Victor's greetings then Nina's. Constant's aren't real.

# Exercise #8: Math problem - $1k principle, 5% interest, 5 years - whats the balance?
balance = 1000 * (1 + 0.05) ** 5
print(balance)

# Exercise #9: Repeat the math problem w/ augmented assignment process.
balance = 1000
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)

# Exercise #10: Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.
obj = 'ABcd'        # reassign
obj.upper()         # neither
obj = obj.lower()   # reassign
print(len(obj))     # neither
obj = list(obj)     # reassign
obj.pop()           # mutate
obj[2] = 'X'        # mutate
obj.sort()          # mutate
set(obj)            # neither
obj = tuple(obj)    #reassign