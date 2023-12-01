# One of the simplest programs
# using "async" (Python 3.5+)

import asyncio
# Methods for working with async code

async def f():
	# "async" function
	print('Hello there!')

asyncio.run(f()) # you need () here