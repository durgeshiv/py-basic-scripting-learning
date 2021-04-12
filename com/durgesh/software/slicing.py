x='LetsSliceThisString'
# we have defined a string as above, lets try to slice it and print 'ThisString'
# [] -> is the syntax for slicing
#

slicedString = x[9:] # Here, this starts at index 9 and : means we haven't specified end
# index thus everything until end would be taken

print(slicedString)  # give o/p as 'ThisString

# Lets try end index also
print(x[9:13])

# There is a provision for step size also within slice
# Lets try to print alternate alphabet from above string
print(x[::2]) ## first two index-values, I have assumed to be empty which mean to start from 0 and finish at end and 2 denotes step size

############# Important ::: step can have negative value also but then;
#it will start from end, and will take step size as defined

print(x[::-1])