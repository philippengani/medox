import _sqlite3


connexion = _sqlite3.connect("Musann.db")
curseur = connexion.cursor()

curseur.execute("""CREATE TABLE Docteur 
    (Docteur_id INTEGER NOT NULL PRIMARY KEY ,
    Nom VARCHAR, Prenom VARCHAR,
    Age INTEGER, 
    Type VARCHAR, 
    telephone INTEGER ,
    email VARCHAR , 
    Localite VARCHAR );""")

curseur.execute("""CREATE TABLE Patient
      (patient_id INTEGER NOT NULL PRIMARY KEY ,
        Nom VARCHAR, Prenom VARCHAR, 
        date_naissance DATE ,
        genre_id INTEGER,
        telephone INTEGER,
        email VARCHAR   );""")

curseur.execute("""CREATE TABLE Rendezvous (
    rdv_id INTEGER PRIMARY KEY,
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

import datetime

import mysql


class Erreur:
    pass


class prise_de_rendez_vous:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="Tekawe",
                password="Tekawe2005",
                database="Musann_db"
            )
            self.cursor = self.conn.cursor()
            self.create_tables()
        except Erreur as e:
            print(f"Error connecting to MySQL: {e}")
            exit(1)
    def create_tables(self):
        self.curseur.execute("""CREATE TABLE Docteur 
            (Docteur_id INTEGER NOT NULL PRIMARY KEY ,
            Nom VARCHAR, Prenom VARCHAR,
            Age INTEGER, 
            Type VARCHAR, 
            telephone INTEGER ,
            email VARCHAR , 
            Localite VARCHAR );""")

        self.curseur.execute("""CREATE TABLE Patient
              (patient_id INTEGER NOT NULL PRIMARY KEY ,
                Nom VARCHAR, Prenom VARCHAR, 
                date_naissance DATE ,
                genre_id INTEGER,
                telephone INTEGER,
                email VARCHAR   );""")

        self.curseur.execute("""CREATE TABLE Rendezvous (
            rdv_id INTEGER PRIMARY KEY,
            Docteur_id INTEGER NOT NULL,
            patient_id INTEGER NOT NULL,
            date_heure DATETIME NOT NULL,
            motif TEXT,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (Docteur_id) REFERENCES docteur(Docteur_id) ON DELETE RESTRICT,
            FOREIGN KEY (patient_id) REFERENCES patient(patient_id) ON DELETE CASCADE,
            UNIQUE (Docteur_id, date_heure));""")

        self.connexion.commit()

class Docteur:
    def __init__(self, Nom, Prenom, Age, specialisation, telephone, email, localite  ):
        self.Nom = Nom
        self.Prenom = Prenom
        self.Age = Age
        self.specialisation = specialisation
        self.telephone = telephone
        self.email = email
        self.localite = localite

    def add_docteur(self):
            Nom = input("Entrer le Nom du Docteur: ").strip()
            Prenom = input("Entrer le prenom du Docteur:").strip()
            Age = input("Entrer  l'age :").strip()
            telephone = input("Entrer le numero :").strip()
            email = input(" votre email :").strip()
            localite = input("votre localiter:").strip()
            specialisation = input("Enter specialization: ").strip()
            if not Nom or not specialisation or not Prenom or not Age or not telephone or not email or not localite :
                print("Entrée invalide, Tous les champs doivent être remplis")
                return
            query = """
                    INSERT INTO docteur ( Nom, Prenom,Age, specialisation, telephone, email)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
            self.cursor.execute(query, (Nom, Prenom, specialisation, telephone, email))
            self.conn.commit()
            print("le docteur a ajouté avec succès.")

class Patient(Docteur):
    def __init__(self,Nom, Prenom , Date_naissance , genre_id, telephone, email, patient_id ):
        super().__init__(Nom, Prenom, telephone, email)
        self.patient_id = patient_id
        self.Nom = Nom
        self.Prenom = Prenom
        self.Date_naissance = Date_naissance
        self.genre_id = genre_id
        self.telephone = telephone
        self.email = email

    def add_patient(self):
        Nom = input("Entrer le nom du patient: ").strip()
        try:
            Date_naissance = input("Enter appointment date (YYYY-MM-DD HH:MM): ").strip()
        except ValueError:
            print("age invalide")
            return
        Prenom = input("Entrer le prenom du Docteur:").strip()
        telephone = input("Entrer le numero :").strip()
        email = input(" votre email :").strip()
        genre_id = input("veuiller entrer votre genre :")
        patient_id = input("quelle est votre ID :")
        if not Nom or not Date_naissance or not Prenom or not genre_id or not telephone or not email or not patient_id :
            print("Invalid input.")
            return
        self.cursor.execute(
            "INSERT INTO patients (Nom, Prenom, telephone, email, genre_id, patient_id) VALUES (%s, %s,%s,%s,%s,%s,)",
            (Nom,Prenom, telephone, email, genre_id, patient_id )
        )
        self.conn.commit()
        print("Patient ajouté avec succes.")

class rendez_vous(Docteur):
   def __init__(self, rdv_id, docteur_id, patient_id, date_heure, motif, date_creation):
       self.rdv_id = rdv_id
       self.docteur_id = docteur_id
       self.patient_id = patient_id
       self.date_heure = date_heure
       self.motif = motif
       self.date_creation = date_creation
       try:
           docteur_id = int(input("Entrer le ID du docteur: "))
           patient_id = int(input("Entrer le ID du patient: "))
           date_heure_str = input("Saisissez la date du rendez-vous (YYYY-MM-DD HH:MM): ").strip()
           motif = input("Entrer le motif du rendez-vous :")
           date_creation = input("quelle est la date de creation:")
       except ValueError:
           print("Format d'entrée invalide.")
           return

       self.cursor.execute(
           "INSERT INTO appointments (docteur_id, patient_id, date_heure, motif, date_creation) VALUES (%s, %s, %s,%s,%s)",
           (docteur_id, patient_id, date_heure_str,motif,date_creation)
       )
       self.conn.commit()

   def view_appointments(self):
       self.cursor.execute("""
           SELECT a.id, d.Nom, p.Nom, a.la date du rendez-vous.
           FROM rendez-vous a
           JOIN docteurs d ON a.docteur_id = d.id
           JOIN patients p ON a.patient_id = p.id
           ORDER BY a.la date du rendez-vous.
       """)
       rows = self.cursor.fetchall()
       if not rows:
           print("Aucun rendez-vous trouvé.")
           return
       print("\nrendez-vous:")
       for row in rows:
           print(f"ID: {row[0]}, Docteur: {row[1]}, Patient: {row[2]}, Date: {row[3]}")

       print("Rendez-vous réservé avec succès.")

   def close(self):
       self.cursor.close()
       self.conn.close()