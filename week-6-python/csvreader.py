import csv

with open("books.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# the 'with' statement is used to open a file and ensure that it is properly closed after it has been used.
# This is useful because it guarantees that the file will be closed even if an error occurs while the file is being read or written.
