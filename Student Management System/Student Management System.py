import json
import os

class StudentManagement:
    def __init__(self):
        self.students = {}
        self.file_name = "students.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.students = json.load(file)

        else:
            self.students = {}

    def save_data(self):
        with open(self.file_name, "w") as file:
            json.dump(self.students, file, indent=4)

    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("        WELCOME TO STUDENT MANAGEMENT")
            print("=" * 50)

            print("1. Add Student Information")
            print("2. Display Student Information")
            print("3. Add Subject and Marks")
            print("4. Display Marks")
            print("5. Display All Students")
            print("6. Delete Student")
            print("7. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_student_information()

            elif choice == "3":
                self.add_subject_and_marks()

            elif choice == "4":
                self.display_marks()

            elif choice == "5":
                self.display_all_students()

            elif choice == "6":
                self.delete_student()

            elif choice == "7":
                print("\nThank you for using Student Management System!")
                break

            else:
                print("\nInvalid choice! Please enter 1 to 7.")

    def add_student(self):
        print("\n--- Add Student Information ---")
        name = input("Enter student name: ")
        if name in self.students:
            print("\nStudent already exists!")
            return

        mobile = input("Enter mobile number: ")
        dob = input("Enter date of birth: ")
        standard = input("Enter standard: ")
        division = input("Enter division: ")

        self.students[name] = {
            "mobile": mobile,
            "dob": dob,
            "standard": standard,
            "division": division,
            "subjects": {}
        }
        self.save_data()
        print("\nStudent information added successfully!")

    def display_student_information(self):
        print("\n--- Student Information ---")
        name = input("Enter student name: ")
        if name not in self.students:
            print("\nStudent not found!")
            return

        student = self.students[name]
        print("\nStudent Name :", name)
        print("Mobile No    :", student["mobile"])
        print("Date of Birth:", student["dob"])
        print("Standard     :", student["standard"])
        print("Division     :", student["division"])

    def add_subject_and_marks(self):
        print("\n--- Add Subject and Marks ---")
        name = input("Enter student name: ")

        if name not in self.students:
            print("\nStudent not found!")
            return

        n = int(input("Enter number of subjects: "))
        for i in range(n):
            print(f"\nSubject {i + 1}")
            subject = input("Enter subject name: ")
            marks = int(input("Enter marks: "))
            self.students[name]["subjects"][subject] = marks

        self.save_data()
        print("\nSubjects and marks added successfully!")

    def display_marks(self):
        print("\n--- Display Marks ---")

        name = input("Enter student name: ")
        if name not in self.students:
            print("\nStudent not found!")
            return

        subjects = self.students[name]["subjects"]
        if len(subjects) == 0:
            print("\nNo subjects available for this student.")
            return

        print(f"\nMarks of {name}")
        print("-" * 30)

        for subject, marks in subjects.items():
            print(f"Subject: {subject}")
            print(f"Marks  : {marks}")
            print("-" * 30)

    def display_all_students(self):
        print("\n--- All Students ---")
        
        if len(self.students) == 0:
            print("\nNo students available.")
            return

        for name, student in self.students.items():
            print("\n" + "=" * 40)

            print("Student Name :", name)
            print("Mobile No    :", student["mobile"])
            print("Date of Birth:", student["dob"])
            print("Standard     :", student["standard"])
            print("Division     :", student["division"])

            print("\nSubjects and Marks:")
            subjects = student["subjects"]

            if len(subjects) == 0:
                print("No subjects available.")
            else:
                for subject, marks in subjects.items():
                    print(f"{subject}: {marks}")
        print("=" * 40)

    def delete_student(self):
        print("\n--- Delete Student ---")

        name = input("Enter student name: ")
        if name not in self.students:
            print("\nStudent not found!")
            return

        del self.students[name]
        self.save_data()
        print("\nStudent deleted successfully!")

student = StudentManagement()
student.menu()
