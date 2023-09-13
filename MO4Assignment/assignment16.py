import csv
import sqlite3

file = open("books.csv", "w", newline="")
writer = csv.writer(file, delimiter=",")

writer.writerow(["author", "book"])
writer.writerow(["J R R Tolkien", "The Hobbit"])
writer.writerow(["Lynne Truss", "'Eats, Shoots & Leaves'"])

file.close()

file = open("books.csv", "r")
reader = csv.DictReader(file)

books = []
for row in reader:
    books.append(row)

file.close()

file = open("books2.csv", "w", newline="")
writer = csv.writer(file, delimiter=",")

writer.writerow(["title", "author", "year"])
writer.writerow(["The Weirdstone of Brisingamen", "Alan Garner", "1960"])
writer.writerow(["Perdido Street Station", "China Miéville", "2000"])
writer.writerow(["Thud!", "Terry Pratchett", "2005"])
writer.writerow(["The Spellman Files", "Lisa Lutz", "2007"])
writer.writerow(["Small Gods", "Terry Pratchett", "1992"])

file.close()

connection = sqlite3.connect("books.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE books (title TEXT, author TEXT, year INTEGER)")
file.open("books2.csv", "r")
reader = csv.DictReader(file)
cursor.executemany("INSERT INTO books(title, author, year) VALUES (?, ?, ?)", [(row["title"], row["author"], row["year"]) for row in reader])
cursor.execute("SELECT title FROM books ORDER BY title DESC")
cursor.execute("SELECT * FROM books")
cursor.execute("SELECT title FROM books ORDER BY title")

print(cursor.fetchall())

connection.commit()



