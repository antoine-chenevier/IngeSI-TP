import random
import datetime
import os

data_dir = "bbc/"
nb_max_articles_by_category = 1000

all_dir = [f.path for f in os.scandir(data_dir) if f.is_dir()] # Chemins parcourus
all_names = [f.name for f in os.scandir(data_dir) if f.is_dir()] # Noms des catégories

titles_by_category = {} # Dictionnaires qui contiendra les catégories et une liste de titres associés

# Récupération de nb_max_articles_by_category titres pour chaque catégorie
for category_dir, category in zip(all_dir, all_names):
  titles = []
  for f in os.scandir(category_dir):
    if f.is_file() and int(f.name[:3]) < nb_max_articles_by_category:
      with open(f.path) as file:
        first_line = file.readline().strip().translate(str.maketrans('','',','))
        titles.append(first_line)
  titles_by_category[category] = titles 


# Création d'un csv pour les articles, à modifier pour correspondre à vos tables
f = open ("articles.csv","w")
id = 0
for rubrique, titres in titles_by_category.items():
  for titre in titres:
    f.write ("{},{},{}\n".format(id, titre, rubrique))
    id = id+1
f.close()
max_article = id


# Création d'un csv pour les journalistes, à modifier pour correspondre à vos tables
journalistes = [("Sarah","Croche"),("Pierre","Feuilleciseaux"),("Alexandre","Porterre"),("Stéphane","Decarottes"),("Alain","Posteur"),("Alphonse","Danslmur"),("Alonso","Balmasque"),("Aude","Javel"),("Annie","versaire"),("Harry","Covert"),("Sophie","Fonfec"),("Mode","Zarela"),("Debbie","Scott"),("Douglas","Alavanille"),("Housama","Lairbon"),("Fabien","Oubien")]

f = open ("journalistes.csv","w")
id = 0
for nom, prenom in journalistes:
  f.write ("{},{},{}\n".format(id, nom, prenom))
  id = id+1
f.close()
max_journaliste = id

# Création d'un csv de correspondances entre les articles et les journalistes auteurs
f = open("correspondance.csv", "w")
for id_article in range(max_article):
  id_journaliste = random.randrange(max_journaliste)
  f.write ("{},{}\n".format(id_journaliste,id_article))
  # Add a second journalist for 10% of articles
  if random.random() > 0.9:
    id_journaliste_2 = id_journaliste
    while id_journaliste == id_journaliste_2:
      id_journaliste_2 = random.randrange(max_journaliste)
    f.write ("{},{}\n".format(id_article, id_journaliste_2))
f.close()