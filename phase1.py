import mysql.connector

class Erreur(Exception):
    pass

class PriseDeRendezVous:
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
        except mysql.connector.Error as e:
            print(f"Erreur de connexion MySQL: {e}")
            exit(1)

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Docteur (
                Docteur_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                Nom VARCHAR(50),
                Prenom VARCHAR(50),
                Age INTEGER,
                Specialisation VARCHAR(100),
                Telephone VARCHAR(20),
                Email VARCHAR(100),
                Localite VARCHAR(100)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patient (
                Patient_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                Nom VARCHAR(50),
                Prenom VARCHAR(50),
                Date_naissance DATE,
                Genre_id INTEGER,
                Telephone VARCHAR(20),
                Email VARCHAR(100)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Rendezvous (
                Rdv_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                Docteur_id INTEGER NOT NULL,
                Patient_id INTEGER NOT NULL,
                Date_heure DATETIME NOT NULL,
                Motif TEXT,
                Date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (Docteur_id) REFERENCES Docteur(Docteur_id) ON DELETE RESTRICT,
                FOREIGN KEY (Patient_id) REFERENCES Patient(Patient_id) ON DELETE CASCADE,
                UNIQUE (Docteur_id, Date_heure)
            );
        """)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


class Docteur:
    def __init__(self, db):
        self.db = db

    def add_docteur(self):
        Nom = input("Entrer le Nom du Docteur: ").strip()
        Prenom = input("Entrer le prenom du Docteur: ").strip()
        Age = input("Entrer l'age :").strip()
        Telephone = input("Entrer le numero :").strip()
        Email = input("Votre email :").strip()
        Localite = input("Votre localité: ").strip()
        Specialisation = input("Entrer la spécialisation: ").strip()

        if not Nom or not Prenom or not Age or not Telephone or not Email or not Localite or not Specialisation:
            print("Entrée invalide, tous les champs doivent être remplis")
            return

        query = """INSERT INTO Docteur (Nom, Prenom, Age, Specialisation, Telephone, Email, Localite)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        self.db.cursor.execute(query, (Nom, Prenom, Age, Specialisation, Telephone, Email, Localite))
        self.db.conn.commit()
        print("Docteur ajouté avec succès.")


class Patient:
    def __init__(self, db):
        self.db = db

    def add_patient(self):
        Nom = input("Entrer le nom du patient: ").strip()
        Prenom = input("Entrer le prénom du patient: ").strip()
        Date_naissance = input("Entrer la date de naissance (YYYY-MM-DD): ").strip()
        Genre_id = input("Entrer le genre (1=Homme, 2=Femme): ").strip()
        Telephone = input("Entrer le numéro :").strip()
        Email = input("Votre email :").strip()

        if not Nom or not Prenom or not Date_naissance or not Genre_id or not Telephone or not Email:
            print("Entrée invalide, tous les champs doivent être remplis")
            return

        query = """INSERT INTO Patient (Nom, Prenom, Date_naissance, Genre_id, Telephone, Email)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        self.db.cursor.execute(query, (Nom, Prenom, Date_naissance, Genre_id, Telephone, Email))
        self.db.conn.commit()
        print("Patient ajouté avec succès.")


class RendezVous:
    def __init__(self, db):
        self.db = db

    def add_rendezvous(self):
        try:
            Docteur_id = int(input("Entrer l'ID du docteur: "))
            Patient_id = int(input("Entrer l'ID du patient: "))
            Date_heure = input("Saisissez la date du rendez-vous (YYYY-MM-DD HH:MM): ").strip()
            Motif = input("Entrer le motif du rendez-vous :").strip()
        except ValueError:
            print("Format d'entrée invalide.")
            return

        query = """INSERT INTO Rendezvous (Docteur_id, Patient_id, Date_heure, Motif)
                   VALUES (%s, %s, %s, %s)"""
        self.db.cursor.execute(query, (Docteur_id, Patient_id, Date_heure, Motif))
        self.db.conn.commit()
        print("Rendez-vous réservé avec succès.")

    def view_appointments(self):
        self.db.cursor.execute("""
            SELECT r.Rdv_id, d.Nom, p.Nom, r.Date_heure
            FROM Rendezvous r
            JOIN Docteur d ON r.Docteur_id = d.Docteur_id
            JOIN Patient p ON r.Patient_id = p.Patient_id
            ORDER BY r.Date_heure;
        """)
        rows = self.db.cursor.fetchall()
        if not rows:
            print("Aucun rendez-vous trouvé.")
            return
        print("\nListe des rendez-vous:")
        for row in rows:
            print(f"ID: {row[0]}, Docteur: {row[1]}, Patient: {row[2]}, Date: {row[3]}")










