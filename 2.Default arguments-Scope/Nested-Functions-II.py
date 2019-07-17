# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
doble = echo(2)

# Call echo: thrice
triple=echo(3)

# Call doble() and triple() then print
print(doble('hello'), triple('hello'))
##echo(2,('hello'))