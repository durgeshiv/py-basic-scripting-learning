# Here our requirement is to multiply all elements of list and come up with o/p ::

data = [1, 2, 5, 0, 10, 11]
a = 1
for elem in data:
    a = a * elem
print('The value of a is {}'.format(a))  ## This is giving an output = 0 because one of the element
# is 0 and anything multiply by 0, is a 0

# Lets use continue statement here by which we can specify a particular
# condition where execution need to be stopped for particular element
# and continued for further ones
b = 1
for elem in data:
    if elem == 0:
        continue  # Here we have specified that if element =0 execution should continue for next one
    b = b * elem
print('The value of b is {}'.format(b))  ## This is giving an output = 0 because one of the element


#### Break Statement

# Consider a use case where-in we are required to search for a particular value in a list having millions of elements
# Now, our desired element is present at some 4th of 5th position.
# Thus, we would want execution to be stopped then and there in order to get good performance - Hence, we'll use break
#
#considering same list as above
search = 2
for value in data:
    if value == search:
        print('Value is found')
        break

# Thus a break is used to completely stop execution whereas
#    continue is used to stop execution of current iteration only



