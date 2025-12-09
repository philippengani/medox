
if __name__ == "__main__":
    while True:
        print("\n1. Add a new patient")
        print("2. List all patients")
        print("q. Exit")

        menu = input("Enter your choice: ")

        if menu == "q":
            break
        elif menu == "1":
            print("Patient added successfully!")
            print("\n")
            name = input("Patient name: ")
            firstName = input("Patient first name: ")
            age = int(input("Patient age: "))
            email = input("Patient email: ")

        elif menu == "2":
            print("List of all patients:")
