

class Docteur:
    def __init__(self, docteur_id, Nom, Prenom, Age, Type_, telephone, email, localite  ):
        self.docteur_id = docteur_id
        self.Nom = Nom
        self.Prenom = Prenom
        self.Age = Age
        self.Type_ = Type_
        self.telephone = telephone
        self.email = email
        self.localite = localite
    def get_public_record(self):
        return {
             "Docteur_id": self.docteur_id,
            "Nom": self.Nom,
            "Prenom": self.Prenom,
            "Age": self.Age,
            "Type": self.Type_,
            "Telephone": self.telephone,
            "email": self.email,
            "Localite": self.localite
        }

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

    def get_public_record(self):
        return {
            "patient_id": self.patient_id,
            "Nom": self.Nom,
            "Prenom": self.Prenom,
            "Date de naissance": self.Date_naissance,
            "genre_id": self.genre_id,
            "Telephone": self.telephone,
            "Email": self.email
        }    

class Rendez_vous(Docteur):
    def __init__(self, rdv_id, docteur_id, patient_id, date_heure, motif, date_creation=None):
        self.rdv_id = rdv_id
        self.docteur_id = docteur_id
        self.patient_id = patient_id
        self.date_heure = date_heure
        self.motif = motif
        self.date_creation = date_creation

    def get_public_record(self):
        return {
            "rdv_id": self.rdv_id,
            "Doctor_id": self.docteur_id,
            "Patient_id": self.patient_id,
            "Date_heure": self.date_heure,
            "Motif": self.motif,
            "Date_creation": self.date_creation
        }
    def prendre_rendezvous(self, rdv):
        for existant in self.rendezvous:
            if existant.docteur.docteur_id == rdv.docteur.docteur_id and existant.date_heure == rdv.date_heure:
                print(" Ce docteur est deja reserver a  cette date/heure !")
                return False
        self.rendezvous.append(rdv)
        print(" votre rendez-vous a ete accepter !")
        return True
    def annuler_rendezvous(self, rdv_id):
        for rdv in self.rendezvous:
            if rdv.rdv_id == rdv_id:
                self.rendezvous.remove(rdv)
                print("rendez-vous annule.")
                return True
        print(" pas de rendez-vous trouver.")
        return False

    def afficher_rendezvous(self):
        for rdv in self.rendezvous:
            print(rdv)

def create_patient(patient: Patient):
