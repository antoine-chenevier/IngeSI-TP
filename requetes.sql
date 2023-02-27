PRAGMA foreign_keys = ON; 

DROP TABLE Travail;
DROP TABLE Journaliste;
DROP TABLE Article;



CREATE TABLE Journaliste (
    id INT NOT NULL,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Article (
    id INT NOT NULL,
    titre VARCHAR(255) NOT NULL,
    rubrique TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Travail (
    id_journaliste INT NOT NULL,
    id_article INT NOT NULL,
    PRIMARY KEY (id_journaliste, id_article),
    FOREIGN KEY (id_journaliste) REFERENCES Journaliste(id)  ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_article) REFERENCES Article(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- CREATE TABLE Articles_tech (
--     id_journaliste INT NOT NULL,
--     id_article INT NOT NULL,
--     PRIMARY KEY (id_journaliste, id_article),
--     FOREIGN KEY (id_journaliste) REFERENCES Journaliste(id)  ON DELETE CASCADE ON UPDATE CASCADE,
--     FOREIGN KEY (id_article) REFERENCES Article(id) ON DELETE CASCADE ON UPDATE CASCADE
-- );


.import articles.csv Article --csv
.import journalistes.csv Journaliste --csv
.import correspondance.csv Travail --csv

SELECT * FROM Travail LIMIT 10;
SELECT * FROM article LIMIT 10;
SELECT * FROM Journaliste LIMIT 10; 

SELECT "-----------------------";
SELECT " print the numbers of articles for each journalist ";

SELECT j.nom, j.prenom, count(t.id_article) as nb_articles
FROM Journaliste j, Travail t
WHERE j.id = t.id_journaliste 
GROUP BY j.nom, j.prenom, j.id;

SELECT "-----------------------";
SELECT " print the numbers of articles for each journalist sort  by number of articles";

SELECT j.nom, j.prenom, count(t.id_article) as nb_articles
FROM Journaliste j, Travail t
WHERE j.id = t.id_journaliste
GROUP BY j.nom, j.prenom
ORDER BY nb_articles DESC;

SELECT "-----------------------";

SELECT " Affichez le nombre d’articles dans la rubrique tech écrit par chaque journaliste (ainsi que ses informations)";
SELECT j.nom, j.prenom, count(t.id_article) as nb_articles
FROM Journaliste j, Travail t, Article a
WHERE j.id = t.id_journaliste AND t.id_article = a.id AND a.rubrique = 'tech'
GROUP BY j.nom, j.prenom
ORDER BY nb_articles DESC;

SELECT "-----------------------";

-- Affichez les informations des journalistes ayant écrits au moins 30 articles dans la catégorie tech
SELECT j.nom, j.prenom, count(t.id_article) as nb_articles
FROM Journaliste j, Travail t, Article a
WHERE j.id = t.id_journaliste AND t.id_article = a.id AND a.rubrique = 'tech'
GROUP BY j.nom, j.prenom
HAVING nb_articles >= 30;

SELECT "-----------------------";

-- Supprimez les articles de la catégorie tech écrits par le journaliste d’identifiant 10
DELETE FROM Travail
WHERE id_journaliste = 10 AND id_article IN (
    SELECT id
    FROM Article
    WHERE rubrique = 'tech'
);

SELECT "-----------------------";

-- Afficher les articles de la catégorie tech écrits par le journaliste d’identifiant 10
SELECT a.titre, a.rubrique
FROM Travail t, Article a
WHERE t.id_article = a.id AND t.id_journaliste = 10 AND a.rubrique = 'tech';

SELECT "-----------------------";

-- Affichez le nombre d’articles écrits par chaque journaliste pour chaque rubrique
SELECT j.nom, j.prenom, a.rubrique, count(t.id_article) as nb_articles
FROM Journaliste j, Travail t, Article a
WHERE j.id = t.id_journaliste AND t.id_article = a.id
GROUP BY j.nom, j.prenom, a.rubrique;

SELECT "-----------------------";

--Pour chaque journaliste, comptez le nombre d’articles que ce journaliste a écrit tout seul (sans co-auteur)
-- SELECT j.nom, j.prenom, count(t.id_article) as nb_articles
-- FROM Journaliste j, Travail t
-- WHERE j.id = t.id_journaliste AND t.id_journaliste NOT IN (
--     SELECT id_journaliste
--     FROM Travail
--     WHERE id_article = t.id_article AND id_journaliste != t.id_journaliste
-- );

-- SELECT "-----------------------";

-- Afficher le nombre d'auteurs par articles
SELECT a.titre, count(t.id_journaliste) as nb_auteurs
FROM Travail t, Article a
WHERE t.id_article = a.id
GROUP BY a.titre;

SELECT "-----------------------";

-- Afficher les articles qui n'ont qu'un seul auteur
SELECT a.titre
FROM Travail t, Article a
WHERE t.id_article = a.id
GROUP BY a.id;
HAVING count(t.id_journaliste) < 2;

-- Afficher pour chaque journaliste le nombre d'articles qu'il a écrit seul
SELECT j.nom, j.prenom, count(t.id_article) as nb_articles
FROM Journaliste j, Travail t
WHERE j.id = t.id_journaliste AND t.id_article NOT IN (
    SELECT id_article
    FROM Travail
    WHERE id_journaliste != t.id_journaliste
);


-- SELECT j.nom,j.prenom, count(t.id_journaliste) as nb_auteurs
-- FROM Travail t, Article a, Journaliste j
-- WHERE t.id_article = a.id AND t.id_journaliste = j.id
-- GROUP BY a.titre;
-- HAVING nb_auteurs < 2;

SELECT "-----------------------";
SELECT " print the numbers of articles for each journalist ";

SELECT j.nom, j.prenom, count(t.id_article) as nb_articles
FROM Journaliste j, Travail t
WHERE j.id = t.id_journaliste 
GROUP BY j.id;