# Python program showing how to use
# string modulo operator(%) to print
# fancier output

# print integer and float value
print("programming : %2d, Portal : %5.2f" % (1, 05.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))

# print octal value
print("%7.3o" % (25))

# print exponential value
print("%10.3E" % (356.08977))

# Python program showing
# use of format() method

# using format() method
print('I love {} for "{}!"'.format('ruby', 'programming'))

# using format() method and referring
# a position of the object
print('{0} and {1}'.format('ruby', 'Portal'))

print('{1} and {0}'.format('programming', 'Portal'))


# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.

print(f"I love {'ruby'} for \"{'programming'}!\"")

# using format() method and referring
# a position of the object
print(f"{'ruby'} and {'Portal'}")


# Python program showing
# a use of format() method

# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
	.format('ruby', 'For', other ='ruby'))

# using format() method with number
print("ruby :{0:2d}, Portal :{1:8.2f}".
	format(12, 00.546))

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
	format(47.42, 11))

print("ruby: {a:5d}, Portal: {p:8.2f}".
	format(a = 453, p = 59.058))



# Python program to
# show format () is
# used in dictionary

tab = {'ruby': 4127, 'for': 4098, 'geek': 8637678}

# using format() in dictionary
print('ruby: {0[ruby]:d}; For: {0[for]:d}; '
	'ruby: {0[geek]:d}'.format(tab))

data = dict(fun ="", adj ="Portal")

# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))

# Python program to
# format a output using
# string() method

cstr = "I love programming"

# Printing the center aligned
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))

# Printing the left aligned
# string with "-" padding
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))
