"""
Import the reduce function from the functools module.

In the reduce() call, pass a lambda function that takes
two string arguments item1 and item2 and concatenates them;
also pass the list of strings, stark. Assign the result 
to result. 

The first argument to reduce() should be the 
lambda function and the second argument is the list stark.

"""

from functools import reduce 

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2 : item1+item2 ,stark )
 

# Print the result
print(result)