# Taking inputs and printing message accordingly
# accordingly

name = input('Please enter your name')
message = 'Hi {}'.format(name)
print(message)

# Problem-2 Lets calculate and print sum of two numbers
number1 = input("Please enter number one")
number2 = input("Please enter number two")
sum = int(number2) + int(number1) ## Type casting string to number using function int()

print('Sum of {} and {} is {}'.format(number1,number2,sum))