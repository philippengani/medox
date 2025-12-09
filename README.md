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
