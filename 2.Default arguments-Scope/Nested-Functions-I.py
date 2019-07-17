"""
Complete the function header of the nested function with the 
function name inner() and a single parameter word.
Complete the return value: each element of the tuple should 
be a call to inner(), passing in the parameters from 
three_shouts() as arguments to each call.
"""

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))