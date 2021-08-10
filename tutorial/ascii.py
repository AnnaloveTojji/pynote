# ascii: American Standard Code For Information Interchange
# represents English characters as numbers

# print ascii number of letters
print(ord('a'))
print(ord('z'))

# ascii() method
normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

# ex
randomList = ['Python', 'Pythön', 5]
print(ascii(randomList))