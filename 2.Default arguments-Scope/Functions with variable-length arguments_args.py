"""

Complete the function header with the function name gibberish. It accepts a single flexible argument *args.
Initialize a variable hodgepodge to an empty string.
Return the variable hodgepodge at the end of the function body.
Call gibberish() with the single string, "luke". Assign the result to one_word.
Hit the Submit button to call gibberish() with multiple arguments and to print the value to the Shell.

"""

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge=""
    hodgepodge=""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)