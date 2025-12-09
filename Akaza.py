import _sqlite3


connexion = _sqlite3.connect("Musann.db")
curseur = connexion.cursor()

curseur.execute("""CREATE TABLE Docteur 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom VARCHAR, Prenom VARCHAR,
    Age INTEGER, 
    Type VARCHAR, 
    telephone INTEGER ,
    email VARCHAR , 
    Localite VARCHAR );""")

curseur.execute("""CREATE TABLE Patient
      (id INTEGER PRIMARY KEY AUTOINCREMENT ,
        Nom VARCHAR, Prenom VARCHAR, 
        date_naissance DATE ,
        genre_id INTEGER,
        telephone INTEGER,
        email VARCHAR   );""")

curseur.execute("""CREATE TABLE Rendezvous (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Docteur_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    date_heure DATETIME NOT NULL,
    motif TEXT,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Docteur_id) REFERENCES docteur(Docteur_id) ON DELETE RESTRICT,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id) ON DELETE CASCADE,
    UNIQUE (Docteur_id, date_heure));""")





connexion.commit()
connexion.close()