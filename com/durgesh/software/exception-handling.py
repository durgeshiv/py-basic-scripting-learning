#Basic structure of a Try-catch block is as below:

try:
    pass
except:
    pass
finally:
    pass

# Lets do an example by calling key from a dictionary
dictionary = {'a':1,'b':2}
try:
    print(dictionary['c'])
except KeyError:
    print('Exception in the code')
finally:
    print('Finally called...')
