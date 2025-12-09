# medox 
## A Python Doctor Appointment Booking System

Welcome! 🎉  

This is your big Python project: a **Doctor Appointment Booking System** that will grow in stages, from a simple console app to a full web application.

---

## 🏥 Project Description

If anybody is ill and wants to visit a doctor for a check-up, he or she needs to visit the hospital and wait until the doctor is available. The patient also waits in a queue while getting an appointment. If the doctor cancels the appointment for some emergency reasons then the patient is not able to know about the cancellation of the appointment unless or until he or she visits the hospital. This becomes tedious for all the involved individuals.

Our Python-Based Doctor Appointment Booking System is designed to overcome the issue of managing and booking appointments. The system provides patients or any user with an easy way of booking a doctor’s appointment online. It also offers an effective solution where users can view various booking slots available and select the preferred date and time.

In this project, the front end involves HTML, CSS and JavaScript and the back end involves Python. The database used is a MySQL Database and Django is used for the framework. The admin can log in using their credentials. They have the access to add, update, delete and view doctors. By using patient IDs and names, they can also see patient details and past treatments. The admin can view the appointment details by filtering the dates. They can also check the feedback given by the patients.

The doctor can log in using their credentials. They can manage their profile and change the password if they want. They can view any appointment details by filtering the dates. If they want to look for any particular patient, they can search for the patient’s name or ID. They can view all the details about the patients and also about their past treatment. They can also add treatments for their patients.

To log into the system, the patient would need to register first. After logging in, the patient can manage their profile and change the password. They can book an appointment with a doctor by choosing the doctor, date and slots. They can view all the appointments in the booking history. They can even cancel bookings any time they want. They can search for doctors by their name, type or locality. They can view the doctor’s details. They can also give feedback to the admin. They can view the treatment details added by the doctors.

⚠️ **Important:** You will **not** build all of this at once.  
You will start with the **core logic in a console application**, and then gradually move toward the full web system.

## 📖 Overview

In traditional hospital settings, patients often face long wait times and uncertainty regarding doctor availability. If a doctor cancels due to an emergency, patients are often unaware until they arrive.

This project solves these issues by digitizing the process. It allows:
* **Patients** to book slots from home and view real-time availability.
* **Doctors** to manage their schedules and view patient history.
* **Admins** to oversee the entire hospital operation.
---

## 🚀 Features

### 👨‍⚕️ For Doctors
* **Secure Login:** Individual credentials and profile management.
* **Schedule Management:** View upcoming appointments filtered by date.
* **Patient History:** Access past treatment records and patient details (Search by ID/Name).
* **Treatment Logging:** Add new treatment details for patients.

### 🤒 For Patients
* **Easy Booking:** Search doctors by locality/specialty and book available time slots.
* **Dashboard:** View booking history and current status.
* **Flexibility:** Cancel appointments and provide feedback.
* **Transparency:** View treatment details added by doctors.

### 🔑 For Admins
* **Master Control:** CRUD (Create, Read, Update, Delete) operations for Doctors.
* **Oversight:** View all appointment logs and patient feedback.
* **Analytics:** Filter data by dates to track hospital activity.

---

## 🛠️ Tech Stack

Across all phases of the project, you will use:

- **Python** – main programming language  
- **MySQL** – database for all persistent data  
- **Object-Oriented Programming (OOP)** – classes like `Doctor`, `Patient`, `Appointment`  
- **Console UI** – text menus for the first phase  
- **Django** – web framework for building the online system  
- **HTML, CSS, JavaScript** – for the web frontend  

---

## 🗺️ Project Roadmap

The project is split into **3 main phases**.  
Right now, you only work on **Phase 1**, but this is where the full journey is going:

---

### Phase 1 – Core Backend (Console Application with Python + MySQL + OOP)

**Goal:**  
Build a complete **console-based** doctor appointment system where all core logic works correctly and all data is stored in **MySQL**.

**What you will do:**

- Design the **database tables** for doctors, patients, and appointments.
- Create Python **classes** to represent these entities (OOP).
- Connect Python to **MySQL** and perform basic operations.
- Implement the **appointment booking logic**:
  - Create doctors and patients
  - Book appointments
  - Prevent double booking for the same doctor/date/time
  - Cancel appointments
- Create **console menus** for:
  - Admin actions (manage doctors, maybe patients)
  - Patient actions (select patient, list doctors, book/cancel appointments, view history)

By the end of Phase 1, you should be able to sit in front of the terminal and:

- Create doctors and patients  
- Book appointments in the database  
- See and cancel those appointments  
- Be confident that the **business rules** are correct.

This phase is about **logic + database**, not about visuals.

Other Details
# Système de Prise de Rendez-vous chez le Médecin (Version Console)

Bienvenue ! 🎉  

Voici ton grand projet Python : un **système de prise de rendez-vous chez le médecin**.

Tu vas commencer par construire une **application console entièrement fonctionnelle**  
(la version dans la “fenêtre noire” / terminal) en utilisant :

- Python  
- MySQL  
- La programmation orientée objet (POO : classes, objets)

---

## 1. Très important : ton objectif (pour l’instant)

> **L’exigence pour l’instant est de construire une application console qui fonctionne complètement.**  
> Si la logique fonctionne dans la fenêtre noire, la mettre plus tard sur un site web sera facile.  
> Si la logique est cassée, le site web ne fonctionnera jamais.

Donc ta mission **en ce moment** :

- Oublie les sites web et le design.
- Concentre-toi sur le fait de rendre la **logique correcte** :
  - Prendre un rendez-vous
  - Empêcher le double booking
  - Annuler un rendez-vous
  - Enregistrer et lire les données depuis la base MySQL

Tu vas construire tout ça **étape par étape**, et tu devrais voir ton système devenir de plus en plus puissant. Essaie d’apprécier les moments où tu te diras :

- « Aujourd’hui, mon programme peut se connecter à la base de données. »
- « Maintenant il peut ajouter des médecins. »
- « Maintenant il peut créer des rendez-vous. »
- « Maintenant il peut les annuler. »

Chaque étape est une vraie réussite. 🏆

---

## 2. Le problème réel

Dans la vraie vie, quand quelqu’un est malade et veut voir un médecin :

- Il doit parfois aller à l’hôpital et **attendre longtemps**.
- Il ne sait pas toujours si le médecin est **disponible**.
- Si le médecin annule un rendez-vous en urgence, le patient découvre souvent l’annulation **uniquement en arrivant sur place**.

C’est une perte de temps et c’est stressant pour tout le monde.

---

## 3. Ce que ton application console va faire

Tu vas construire une application console où :

- Les **patients** peuvent :
  - Être créés dans le système
  - Prendre un rendez-vous avec un médecin
  - Voir leurs rendez-vous
  - Annuler un rendez-vous

- Les **médecins** sont enregistrés avec des informations comme :
  - Nom
  - Spécialité
  - Ville
  - Email / Téléphone

- Les **rendez-vous** font le lien entre :
  - Un médecin
  - Un patient
  - Une date
  - Un créneau horaire
  - Un statut (`SCHEDULED`, `CANCELLED`, éventuellement `COMPLETED`)

Toutes ces informations seront stockées dans une **base de données MySQL**.  
Tu contrôles tout à travers des **menus texte** dans le terminal.

---

## 4. Technologies que tu vas utiliser (pour cette étape)

Pour cette version console, tu vas utiliser :

- **Python** – ton langage principal
- **MySQL** – pour stocker les médecins, patients et rendez-vous
- **Programmation Orientée Objet (POO)** – classes `Doctor`, `Patient`, `Appointment`
- **Interface texte (console)** – menus et saisie utilisateur avec `print()` et `input()`

---

## 5. Étapes du projet (jalons)

Voici les étapes que tu vas réaliser une par une.  
Chaque étape comporte des **questions** (pour réfléchir) et des **tâches** (à réaliser).

---

### Étape 1 – Environnement & Connexion à la base de données

**Questions :**

1. Qu’est-ce qu’une **base de données** et pourquoi l’utilise-t-on plutôt que de simples listes Python ?
2. Quelles informations doit-on **conserver de manière permanente** pour ce système ?

**Tâches :**

- Installer / configurer :
  - MySQL Server
  - Une bibliothèque Python pour MySQL (par ex. `mysql-connector-python` ou `PyMySQL`)
- Créer une base de données, par exemple : `doctor_appointment_db`.
- Créer un fichier `test_connection.py` qui :
  - se connecte à la base de données,
  - affiche `"Connection successful"` si la connexion fonctionne,
  - ferme la connexion.

Tu devrais pouvoir exécuter :

```bash
python test_connection.py
```

et voir un message de succès.

---

### Étape 2 – Concevoir les tables de la base de données

**Questions :**

1. Quelles **entités** as-tu dans ce système ? (au minimum : `Doctor`, `Patient`, `Appointment`)
2. Quels champs (colonnes) chaque entité doit-elle avoir ?

**Tâches :**

- Décider de trois tables :
  - `doctors`
  - `patients`
  - `appointments`
- Pour chaque table, choisir les colonnes et les types. Par exemple :

  **doctors**
  - `id` (PRIMARY KEY, auto-incrément)
  - `name`
  - `specialty`
  - `city`
  - `email`
  - `phone`

  **patients**
  - `id`
  - `name`
  - `email`
  - `phone`
  - `address`

  **appointments**
  - `id`
  - `doctor_id` (référence à `doctors.id`)
  - `patient_id` (référence à `patients.id`)
  - `date` (par ex. `DATE` ou `VARCHAR`)
  - `time_slot` (par ex. `'09:00-09:30'` en texte)
  - `status` (`SCHEDULED`, `CANCELLED`, etc.)
  - `created_at` (timestamp)

- Écrire les requêtes `CREATE TABLE` pour ces tables dans un fichier `schema.sql`.
- Exécuter `schema.sql` dans MySQL pour créer les tables.

---

### Étape 3 – Classes Python (modèle métier)

**Questions :**

1. Comment une classe Python peut-elle représenter la même chose qu’une ligne (row) dans une table ?
2. Pourquoi est-ce utile d’avoir une classe `Doctor` au lieu de manipuler uniquement des dictionnaires ?

**Tâches :**

- Créer un fichier `models.py`.
- Définir trois classes :
  - `Doctor`
  - `Patient`
  - `Appointment`
- Chaque classe doit :
  - avoir une méthode `__init__` avec les bons attributs,
  - avoir une méthode `__str__` ou `__repr__` pour que `print(doctor)` affiche quelque chose de lisible.

- En bas de `models.py`, écrire un petit test :

  ```python
  if __name__ == "__main__":
      d = Doctor(...)
      p = Patient(...)
      a = Appointment(...)
      print(d)
      print(p)
      print(a)
  ```

Exécute le fichier et vérifie que l’affichage des objets est correct.

---

### Étape 4 – Module d’aide pour la base de données (`db.py`)

**Question :**

1. Pourquoi est-ce une bonne idée de centraliser la logique de connexion à la base de données dans un seul fichier au lieu de la copier partout ?

**Tâches :**

- Créer un fichier `db.py`.
- Implémenter une fonction `get_connection()` qui :
  - se connecte à ta base MySQL avec tes identifiants,
  - retourne l’objet connexion.

Exemple (conceptuel) :

```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="...",
        password="...",
        database="doctor_appointment_db"
    )
```

Tu importeras et utiliseras `get_connection()` dans les autres fichiers.

---

### Étape 5 – Doctor Repository (CRUD pour les médecins)

**Questions :**

1. Que signifie **CRUD** ?
2. Comment le CRUD se traduit-il en opérations SQL ?

   - Create → `INSERT`
   - Read → `SELECT`
   - Update → `UPDATE`
   - Delete → `DELETE`

**Tâches :**

- Créer `doctor_repository.py`.
- Implémenter des fonctions du type :

  ```python
  def create_doctor(doctor: Doctor) -> int: ...
  def get_doctor_by_id(doctor_id: int) -> Doctor | None: ...
  def get_all_doctors() -> list[Doctor]: ...
  def update_doctor(doctor: Doctor) -> None: ...
  def delete_doctor(doctor_id: int) -> None: ...
  ```

- Utiliser `get_connection()` pour accéder à la base.
- En bas de `doctor_repository.py`, ajouter des tests qui :
  - insèrent un médecin,
  - le lisent,
  - affichent la liste de tous les médecins.

Exécute ce fichier et vérifie que le contenu de la base est mis à jour comme prévu.

---

### Étape 6 – Patient Repository (CRUD pour les patients)

**Questions :**

1. Quels champs sont nécessaires pour identifier et contacter un patient ?
2. En quoi ce repository est-il similaire à celui des médecins ?

**Tâches :**

- Créer `patient_repository.py`.
- Implémenter des fonctions :

  ```python
  def create_patient(patient: Patient) -> int: ...
  def get_patient_by_id(patient_id: int) -> Patient | None: ...
  def get_all_patients() -> list[Patient]: ...
  def update_patient(patient: Patient) -> None: ...
  def delete_patient(patient_id: int) -> None: ...
  ```

- Tester en ajoutant et en récupérant des patients.

---

### Étape 7 – Rendez-vous & règles de réservation

**Questions :**

1. Quelles règles doivent être respectées lors de la prise d’un rendez-vous ?
   - Exemple : un médecin ne peut pas avoir deux rendez-vous au même créneau horaire le même jour.
2. Que se passe-t-il si un patient essaie de réserver un créneau déjà pris ?

**Tâches :**

- Créer `appointment_repository.py`.
- Implémenter des fonctions comme :

  ```python
  def create_appointment(appointment: Appointment) -> int: ...
  def get_appointment_by_id(appointment_id: int) -> Appointment | None: ...
  def get_appointments_by_doctor(doctor_id: int) -> list[Appointment]: ...
  def get_appointments_by_patient(patient_id: int) -> list[Appointment]: ...
  def get_appointments_by_doctor_and_date(doctor_id: int, date: str) -> list[Appointment]: ...
  def cancel_appointment(appointment_id: int) -> None: ...
  ```

- Dans `create_appointment` :
  - Avant de faire l’`INSERT`, interroger la base pour voir s’il existe déjà un rendez-vous avec le même `doctor_id`, la même `date` et le même `time_slot` avec un statut non annulé.
  - Si oui, refuser la réservation (par exemple en retournant `None` ou en levant une exception).

C’est ta **logique de réservation principale**.

---

### Étape 8 – Menu console pour l’admin

**Questions :**

1. Quelles actions un “admin” doit-il pouvoir faire sur les médecins ?
2. En quoi un menu texte simple peut-il t’aider à tester tes repositories ?

**Tâches :**

- Créer `admin_console.py`.
- Implémenter une boucle comme :

  ```text
  1. Ajouter un médecin
  2. Lister tous les médecins
  3. Mettre à jour un médecin
  4. Supprimer un médecin
  5. Quitter
  ```

- Utiliser les fonctions de `doctor_repository` à l’intérieur du menu.
- Bien gérer les saisies utilisateur (entiers, chaînes de caractères, valeurs vides).

Tu devrais pouvoir exécuter :

```bash
python admin_console.py
```

et gérer les médecins depuis le terminal.

---

### Étape 9 – Console patient (réservation & annulation)

**Questions :**

1. De quoi un patient a-t-il besoin pour prendre un rendez-vous ?
2. Comment peux-tu guider l’utilisateur étape par étape dans la console pour qu’il ne se perde pas ?

**Tâches :**

- Créer `patient_console.py`.
- Implémenter un flux utilisateur comme :

  1. Demander : « Es-tu un patient existant ? (O/N) »
     - Si **N** : créer un nouveau patient et l’enregistrer dans la base.
     - Si **O** : demander l’ID du patient et le charger.
  2. Afficher un menu :

     ```text
     1. Voir mes informations
     2. Lister tous les médecins
     3. Prendre un rendez-vous
     4. Voir mes rendez-vous
     5. Annuler un rendez-vous
     6. Quitter
     ```

  3. “Prendre un rendez-vous” doit :
     - lister les médecins avec leurs IDs,
     - demander l’ID du médecin, la date et le créneau horaire,
     - appeler `create_appointment` et gérer le cas où le créneau est déjà pris.

  4. “Voir mes rendez-vous” doit afficher tous les rendez-vous du patient courant.
  5. “Annuler un rendez-vous” doit :
     - lister les rendez-vous du patient avec leurs IDs,
     - demander lequel annuler,
     - appeler `cancel_appointment`.

---

## 6. Comment travailler sur ce projet

- Avance **une étape à la fois**.
- Essaie d’avoir **quelque chose qui fonctionne** à la fin de chaque étape.
- C’est normal si tu :
  - fais des erreurs,
  - dois corriger des bugs,
  - dois améliorer ton design au fur et à mesure.

Ce qui compte, c’est que :

- Ta base de données fonctionne.
- Tes classes ont du sens.
- Tes repositories parlent correctement avec la base.
- Tes menus console permettent à un utilisateur de :
  - créer des médecins et des patients,
  - prendre des rendez-vous,
  - les consulter et les annuler.

Une fois que ton **application console sera solide**, tout le reste plus tard (par exemple, ajouter une interface web) sera beaucoup plus facile.

Amuse-toi bien à construire ce système, et n’oublie pas de célébrer chaque petite victoire. 🚀

---

### Phase 2 – Basic Web Application (Django + MySQL, Core Features)

**Goal:**  
Put a **simple web interface** on top of the logic you already understand, using Django and HTML templates.

**What you will do :**

- Create a Django project that uses the **same kind of database structure** as Phase 1.
- Define Django **models** for Doctor, Patient, Appointment.
- Implement **user registration and login** (for patients).
- Build basic pages to:
  - List doctors  
  - Show doctor details  
  - Allow a logged-in patient to book an appointment  
  - Show “My Appointments” for the logged-in patient  
  - Cancel an appointment

The objective here is to **translate** what you already have in the console into a **web version**, not to invent new logic. You are mostly changing *how* the user interacts with the system, not *what* it does.

---

### Phase 3 – Full Online System (Roles, Treatments, Feedback, Search, UI)

**Goal:**  
Turn the basic web app into a **full doctor appointment platform** that matches the complete description above.

**What you will do:**

- Implement and separate **user roles**:
  - **Admin** – manage doctors, view patients and appointments, see feedback.
  - **Doctor** – manage profile, view appointments, search patients, add treatments.
  - **Patient** – manage profile, book/cancel appointments, view history, give feedback.
- Add **filters and search**:
  - Admin and doctors can filter appointments by date, status, patient, etc.
  - Patients can search doctors by **name, specialty, locality**.
- Add **treatment management**:
  - Doctors can record treatments and notes for each appointment.
  - Patients can view their past treatment details.
- Add **feedback**:
  - Patients can submit feedback about doctors or the service.
  - Admin can read and manage feedback.
- Improve the **frontend**:
  - Use HTML/CSS/JS to create a clean, user-friendly interface.
  - (Optionally) enhance with responsive layout and better UX.

Phase 3 makes your system feel like a **real-world web application** that could be used by a clinic.

---

## 💻 Getting Started

### Prerequisites
* Python installed on your machine.
* `pip` (Python package manager).

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/philippengani/medox.git]
    cd medox
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations (Database Setup)**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Start the Server**
    ```bash
    python manage.py runserver
    ```

---

## 🤝 Contributing

This is an educational project. Suggestions and pull requests to improve the code structure are welcome!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
