from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")

# the cs50 .execute function returns a list of dictionaries when you're using SELECT
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)

print(rows[0]["n"])