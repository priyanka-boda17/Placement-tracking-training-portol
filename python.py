class PlacementPortal:
    def _init_(self):
        self.students = {}

    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")
        self.students[roll] = {
            "name": name,
            "branch": branch,
            "training": [],
            "placed": False,
            "company": None
        }
        print("Student added successfully!\n")

    def add_training(self):
        roll = input("Enter Roll Number: ")
        if roll in self.students:
            course = input("Enter Training Course Name: ")
            self.students[roll]["training"].append(course)
            print("Training added successfully!\n")
        else:
            print("Student not found!\n")

    def update_placement(self):
        roll = input("Enter Roll Number: ")
        if roll in self.students:
            company = input("Enter Company Name: ")
            self.students[roll]["placed"] = True
            self.students[roll]["company"] = company
            print("Placement details updated!\n")
        else:
            print("Student not found!\n")

    def view_students(self):
        if not self.students:
            print("No students available.\n")
            return
        for roll, data in self.students.items():
            print(f"Roll No: {roll}")
            print(f"Name: {data['name']}")
            print(f"Branch: {data['branch']}")
            print(f"Training: {', '.join(data['training']) if data['training'] else 'None'}")
            print(f"Placed: {'Yes' if data['placed'] else 'No'}")
            if data['placed']:
                print(f"Company: {data['company']}")
            print("-" * 30)

    def menu(self):
        while True:
            print("\n--- Placement Tracking and Training Portal ---")
            print("1. Add Student")
            print("2. Add Training Course")
            print("3. Update Placement Status")
            print("4. View Student Details")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_training()
            elif choice == "3":
                self.update_placement()
            elif choice == "4":
                self.view_students()
            elif choice == "5":
                print("Exiting Portal. Thank you!")
                break
            else:
                print("Invalid choice! Try again.\n")
