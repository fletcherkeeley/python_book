# Exercise #1: Use concatenation to create your full name. 

print('Fletcher' + ' ' + 'Keeley')


# Exercise #2: Extract the individual digits of 4936. 

num = '4936'
print(num[3])
print(num[2])
print(num[1])
print(num[0])

# Technically my answer above is wrong but the question doesn't make any sense so I'm going to leave the answer to the question that was asked and ignore the incorrect solution from the curriculum. Dissapointing.


# Exercise #3: What does the following code do? Why?

print('5' + '10') # The code is concatenating two strings and we get the result of '510'


# Exercise #4: Refactor the code from the previous exercise to use coercion to print 15 instead. 

print((int('5'))+int('10'))


# Exercise #5: Will an error occur if you try to access a list element with an index greater than or equal to the list's length?

# foo = ['a', 'b', 'c'] Commented out for the sake of continuing to run without error below. 
# print(foo[3])

# Yes, an error will occur because we only have len = 2 for the list's indexed terms 


# Exercise #6: To what value does the following expression evaluate?

print('foo' == 'Foo')

# This expression evaluates if the string 'foo' is the same as the string 'Foo' - since the boolean statement is caps sensitive the answer will be false. 

# Exercise #7: What does the below code do, and why?

#print(int('3.2415')) Commenting out. 

# The code rasises a ValueError because 3.2415 is not an integer.


#Exercise #8: To what value does the following expression evaluate?

print('12' < '9') 

#The expression evaluates whether the string '12' is greater than or less than the string '9'. It evaluates as True because python will read the string from left to right and compared 1 less than 9 which is true. 