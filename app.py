import sqlite3
con = sqlite3.connect("tp.db")

cur = con.cursor()

# Select rubrique from table Article
res = cur.execute("SELECT rubrique FROM Article")
print(res.fetchone())

# Supprimer un journaliste
cur.execute("DELETE FROM Journaliste WHERE id = 101")
cur.execute("DELETE FROM Journaliste WHERE id = 102")

# Insert journaliste into table
cur.execute("INSERT INTO Journaliste VALUES (102, 'Jean', 'Dupont')")
cur.execute("INSERT INTO Journaliste VALUES (101, 'Antoine', 'C')")

con.commit()

# Ajoutez à votre base de donnée une fonction retournant la chaine de caractère "Prénom Nom" à partir du prénom et du nom d’un journaliste. Appliquez cette fonction à tous les journalistes et affichez le résultat
con.create_function("print", 2, lambda x, y: x + " " + y)
for row in con.execute("SELECT print(prenom, nom) FROM Journaliste"):
    print(row)

# Créez une fonction Python qui, à partir d’un identifiant, retourne la chaine de caractère correspondant aux informations du journaliste.
def get_journaliste(id):
    res = cur.execute("SELECT * FROM Journaliste WHERE id = ?", (id,))
    return res.fetchone()

# Affichez le résultat de cette fonction pour l’identifiant 101
print(get_journaliste(101))

# Créez un aggrégat qui calcule la taille de la chaine la plus longue pour une colonne de chaines de caractères.
def max_len(col):
    def step(state, value):
        return max(state, len(value))

    def finalize(state):
        return state

    return step, finalize

# Appliquez cet aggrégat à la colonne rubrique de la table Article et affichez le résultat.
con.create_aggregate("max_len", 1, max_len)

# Créez une fonction Python qui calcule la taille du nom de journaliste le plus long en utilisant en appelant votre aggrégat.
def max_len_journaliste():
    res = cur.execute("SELECT max_len(nom) FROM Journaliste")
    return res.fetchone()[0]


