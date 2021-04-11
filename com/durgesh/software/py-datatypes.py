# Integer
x = 10 # Here, we haven't defined data type explicitly nor with keyword var/val unlike in java or scala
# Float
y = 10.5

# String
    # Can be either single line or multiline -> single quote or double quote can be used
    # For multiline -> triple quote is used and it preserves same structure, even any space which we add

singleQuoteString = 'This is single quote string'
doubleQuoteString = "This is double quote string"

multiLineString = '''
    This
        is 
            multiline
                String

'''
print(singleQuoteString)
print(doubleQuoteString)
print(multiLineString)

x = 'Lets try splitting this string using split function'.split(' ')
print(x.__len__())
print(x)

