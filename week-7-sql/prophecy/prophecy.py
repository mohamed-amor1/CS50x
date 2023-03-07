import csv
import sqlite3

import sqlite3

# Connect to the database
conn = sqlite3.connect('roster.db')

# Create a cursor object
cur = conn.cursor()

house_names = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

# Iterate over the house names and insert records for each student in each house
for house_name in house_names:
    # Get the house ID from the houses table
    cur.execute("SELECT id FROM houses WHERE house = ?", (house_name,))
    house_id = cur.fetchone()[0]

    # Get the list of student names for the current house
    cur.execute(
        "SELECT student_name FROM students WHERE house = ?", (house_name,))
    student_name = [row[0] for row in cur.fetchall()]

    # Insert records for each student in the current house
    for student_name in student_name:
        # Get the student ID from the students table
        cur.execute(
            "SELECT id FROM students WHERE student_name = ?", (student_name,))
        student_id = cur.fetchone()[0]

        # Define the SQL statement
        sql = "INSERT INTO assignments (student_id, house_id) VALUES (?, ?)"

        # Execute the SQL statement with the foreign key values
        cur.execute(sql, (student_id, house_id))


conn.commit()


# Commit the changes
conn.commit()
cur.execute("SELECT * FROM houses")

# Fetch the result set
rows = cur.fetchall()

# Process the data as needed
for row in rows:
    print(row)


# Close the cursor and the connection
# cur.close()
# conn.close()


# with open("students.csv", "r") as file:
#      reader = csv.DictReader(file)
#      for row in reader:

#          print(row)

# # db = SQL("sqlite:///favorites.db")

# # favorite = input("Favorite: ")

# # # the cs50 .execute function returns a list of dictionaries when you're using SELECT
# # rows = db.execute(
# #     "SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)

# # print(rows[0]["n"])
