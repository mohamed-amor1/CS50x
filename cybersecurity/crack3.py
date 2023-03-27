# Import the necessary modules and constants
from string import ascii_letters, digits, punctuation
from itertools import product

# Generate all possible combinations of 8 characters using letters, digits, and punctuation
for passcode in product(ascii_letters + digits + punctuation, repeat=8):

    # Print the current passcode
    # The * operator unpacks the tuple into separate arguments for the print function
    print(*passcode)
