books = []  # a list

# Add three books to your shelf
for i in range(3):
    book = dict()
    # to delete spaces and capitalize first letter ==> cleaning up user input
    user_input = input("Title: ").strip().capitalize()
    words = user_input.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    book["title"] = ' '.join(capitalized_words)
    book["author"] = input("Author: ")

    books.append(book)  # Insert the book into the list books

for book in books:
    print(book["title"])
