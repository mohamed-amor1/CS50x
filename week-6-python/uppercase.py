from cs50 import get_string

before = get_string("Before: ")
after = before.upper()
print(f"After:  {after}")

# alternatively:
#   for c in before:
#       print(c.upper(), end="")
#   print()
