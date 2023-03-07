import csv
import sqlite3

import sqlite3

# Connect to the database
conn = sqlite3.connect('roster.db')

# Create a cursor object
cur = conn.cursor()

# Execute the SQL statement to copy columns from table1 to table2
cur.execute("INSERT INTO houses (house, head) SELECT house, head FROM students")


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
