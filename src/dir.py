# Listing the methods
# of an object

class C:
	def my_method(x):
		print('my_method(x)')

print(dir(C))
c = C()
print(dir(c))

# dir lists all the methods,
# including those that you
# do not see here