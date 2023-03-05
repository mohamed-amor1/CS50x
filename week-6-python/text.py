text = "In the great green room"
words = text.split()

# Round 1
print("Round 1")
for word in words:
    print(word)
print()

# Round 2
print("Round 2")
for word in words:
    for c in word:  # prints every caracter except spaces!
        print(c)
print()

# Round 3
print("Round 3")
for word in words:
    if "g" in word:
        print(word)
print()

# Round 4
print("Round 4")
# SLICING: starts from the third element (index 2) and includes all the remaining elements until the end of the sequence.
for word in words[2:4]:  # first number inclusive / last number exclusive
    print(word)
print()

# Round 5
print("Round 5")
for word in words:  # word could be anything e.g. z/_/zebra/....
    print("Goodnight Moon")
print()
