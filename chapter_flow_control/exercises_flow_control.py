# Exercise #1: To what alues do the following expression evaluate?

# False or (True and False) - False
# True or (1 + 2) - True
# (1 + 2) or True - 3
# True and (1 + 2) - 3
# False and (1 + 2) - False 
# (1 + 2) and True - True
# (32 * 4) >= 129 - False
# False != (not True) - False
# True == 4 - False
# False == (847 == '847') - True

# Exercise #2: Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.
def even_or_odd(number):
   if number % 2 == 0:
      print('even')
   else: print('odd')

even_or_odd(7)

# Exercise #3: Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# It will print Product2 then Product not Found!. It will print 113 because it matches on the string and then it will print not found because the int wont match on the str. 

#Exercise #4: Refactor this code to use a regular if statement instead. 

def baz():
    return('bar' if foo() else qux())

def baz():
    if foo():
        return('bar')
    else:
        return qux()
    
# Exercise #5: What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([]) 

# It will print Empty b/c the empty brackets represent an empty list which is falsy.


# Exercise #6: Write a function that takes a single integer argument and prints a message that describes whether:
# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100 
# the value is less than 0 

def what_value(number_range):
    if number_range < 0:
        print(f'{number_range} is less than 0')
    elif number_range <= 50:
        print(f'{number_range} is between 0 and 50')
    elif number_range <= 100:
        print(f'{number_range} is between 51 and 100')
    else:
        print(f'{number_range} is greater than 100')

what_value(0)
what_value(25)
what_value(50)
what_value(75)
what_value(100)
what_value(101)
what_value(-1)