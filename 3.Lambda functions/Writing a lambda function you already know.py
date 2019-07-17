"""
without lamba function

def echo_word(word1, echo):
    ##Concatenate echo copies of word1.
    words = word1 * echo
    return words
    
"""


"""
with lambda function
"""

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)