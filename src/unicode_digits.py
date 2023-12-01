# Digits in the Unicode space

# Using regular expressions
import re

for i in range(32, 10_000):
	ch = chr(i) # character with the
				# Unicode code i
	if re.match('\d', ch):
		# if it is a digit
		print(ch, end='')

print('')

# How many digits will pe printed?