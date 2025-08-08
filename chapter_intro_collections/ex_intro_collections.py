# Exercise #1: If you have a list named people, how can you determiend the number of entries in that list?

people_list = ['John', 'Jodie', 'Jonas', 'Wout', 'Pogacar']
print(len(people_list))

# Exercise #2: Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?


stuff = ('hello', 'world', 'bye', 'now')
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)


# Exercise #3: Identify at least 2 differences between lists and tuples. Identify at least 2 ways that list and tuples are similar. 
# differences - mutability, syntax 
# similarities - sequences, non-primitive, ordered, hetergeneous (don't need to be the same type)


# Exercise #4: Why can we treat strings as sequences?
# We can treat strings as sequences because strings are an ordered collection of objects that can be indexed by whole numbers.


# Exercise #5: How do the set types differ from the sequence types?
# Sets are unordered and can't be indexed. 


#Exericse #6: Assuming you have the following assignment:

pi = 3.141592

# Write some code that converst he value of pi to a string and assigns it to the varialbe name str_pi. 

str_pi = str(pi)
print(str_pi)
print(type(str_pi))


# Exercise #7: Without running the following code, identify the numbers that are included in each of the following ranges:

range(7) - [0, 1, 2, 3, 4, 5, 6]
range(1, 6) - [1, 2, 3, 4, 5]
range(3, 15, 4) - [3, 7, 11]
range(3, 8, -1) - []
range(8, 3, -1) - [8, 7, 6, 5, 4]


# Exercise #8: How would you print all the numbers in the following range?

r = range(3, 17, 4)
print(list(r))


# Excercise #9: Given the above code, answer the following questions and explain your answers:

# Are the lists assigned to my_list and another_list equal? - Yes
# Are the lists assigned to my_list and another_list the same object? - No
# Are the nested lists at index 3 of my_list and another_list equal? - Yes
# Are the nested lists at index 3 of my_list and another_list the same object? - Yes - Shallow copy example. 


# Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)

# It won't, sets are unordered. 


# Excersize #11: You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

residence = {'Alice': 'USA', 'Francois': 'Canada', 'Inti': 'Peru', 'Monika': 'Germany', 'Sanyu': 'Uganda', 'Yoshitaka': 'Japan'}
inti = residence['Inti']
print(inti)