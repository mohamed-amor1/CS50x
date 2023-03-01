#  psets/6/readability/
import math
from cs50 import get_int
from cs50 import get_string

# create function that
# return space count

input = get_string("Text: ")
print(f"Your text is {input}")

c = 0
for i in input:       # i holds each character in String s for every iteration of loop
    if(i.isalpha()):
        c=c+1   # Increment Count by 1
print("Number of Characters =", c)

w = len(input.split())
print(f"Number of words: {w}")
sen = input.count(".") + input.count("!") + input.count("?")
print(f"Number of sentences: {sen}")

L = (c/w)*100
S = (sen/w) *100
index = round((0.0588 * L) - (0.296 * S) - 15.8)
print(f"Grade {index}")
