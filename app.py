import sqlite3
con = sqlite3.connect("tp.db")

cur = con.cursor()

# Select rubrique from table Article
res = cur.execute("SELECT rubrique FROM Article")
print(res.fetchone())

# Insert journaliste into table
cur.execute("INSERT INTO Journaliste VALUES (100, 'Jean', 'Dupont')")
con.commit()
