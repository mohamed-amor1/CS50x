import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

user = input("Who are you looking for?: ")
if user in names:
    print("Found.")
    sys.exit(0)

print("Not found.")
sys.exit(1)