#  psets/6/readability/
import math
from cs50 import get_string

# Get input string and print it
input_str = get_string("Text: ")
print(f"Your text is: {input_str}")

# Count the number of characters in the input string
char_count = sum(i.isalpha() for i in input_str)
print(f"Number of characters: {char_count}")

# Count the number of words in the input string
word_count = len(input_str.split())
print(f"Number of words: {word_count}")

# Count the number of sentences in the input string
sentence_count = input_str.count(
    ".") + input_str.count("!") + input_str.count("?")
print(f"Number of sentences: {sentence_count}")

# Calculate the average number of letters per 100 words
L = (char_count / word_count) * 100

# Calculate the average number of sentences per 100 words
S = (sentence_count / word_count) * 100

# Calculate the readability index
index = round((0.0588 * L) - (0.296 * S) - 15.8)

# Print the grade
print(f"Grade: {index}")


#Explanation:

#The get_int function from the cs50 library is not used in the code, so it has been removed.
#The variable input has been renamed to input_str for better readability.
#The sum function is used to calculate the number of characters in the input string, replacing the for loop and counter.
#The round function is used to round the result of the readability index calculation to the nearest whole number.
#The string formatting for the print statements has been updated to use f-strings instead of the format method.

