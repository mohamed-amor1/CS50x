# Import the `ascii_letters` string from the `string` module
from string import ascii_letters

# Import the `product` function from the `itertools` module
from itertools import product

# Loop over all possible 4-letter combinations generated by `product(ascii_letters, repeat=4)`
for passcode in product(ascii_letters, repeat=4):
    # Print each passcode tuple using the `print` function and the `*` operator to unpack the tuple
    # The `*` operator is used to print the values in the tuple separated by a space instead of a comma
    print(*passcode)
