i = 1
v = 'a'
print("Value at index {0} is {1}".format(i,v))
print("Value at index {} is {}".format(i,v))
print("Value at index %d is %s" % (i,v))

# my favorite way
emp = {'name':'toran', 'age':26, 'mobile':'8602431733'}
print("My name is {name} and I'm {age} years old. You can contact me at {mobile}".format(**emp))