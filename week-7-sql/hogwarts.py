import csv

houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0,
}

with open("hogwarts.csv", "r") as file:
    reader = csv.DictReader(file) #ignore first line of file
    next(reader) #ignore first line of file
    for row in reader:
        house = row[1]
        houses[house] += 1

for house in houses:
    count = houses[house]
    print(f"{house}: {count}")