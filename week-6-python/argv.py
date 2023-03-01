from sys import argv

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")

# print all argument vectors (argv)
for arg in argv:
    print(arg)

# don't print program name "argv.py"
for arg in argv:
    if arg != "argv.py":
        print(arg)

# alt method : don't print program name "argv.py"
# starting the list from [1] not  [0]
# A[1:] Take elements 1 to the end" of the list
for arg in argv[1:]:
    print(arg)

# A[:-1] removes last element of the list
for arg in argv[:-1]:
    print(arg)
