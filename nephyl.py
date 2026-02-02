
from phase1 import PriseDeRendezVous, Docteur, Patient, RendezVous



def main():
    db = PriseDeRendezVous()
    docteur = Docteur(db)
    patient = Patient(db)
    rendezvous = RendezVous(db)

    print("\n=== MENU ===")
    print("1. Ajouter un docteur")
    print("2. Ajouter un patient")
    print("3. Réserver un rendez-vous")
    print("4. Voir les rendez-vous")
    print("5. Quitter")

    while True:
        choix = input("\nVotre choix: ").strip()

        if choix == "1":
            docteur.add_docteur()
        elif choix == "2":
            patient.add_patient()
        elif choix == "3":
            rendezvous.add_rendezvous()
        elif choix == "4":
            rendezvous.view_appointments()
        elif choix == "5":
            print("Fermeture du programme...")
            db.close()
            break
        else:
            print("Choix invalide, réessayez.")

if __name__ == "__main__":
    main()
    db = PriseDeRendezVous()
    docteur = Docteur(db)
    patient = Patient(db)
    rendezvous = RendezVous(db)
    rendezvous.view_appointments()

    db.close()
