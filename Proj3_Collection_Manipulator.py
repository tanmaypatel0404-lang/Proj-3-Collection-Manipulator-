print("Welcome to the Student Data Organizer")
print()

students = []
subjects_offered = set()

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    print()

    # ---Add Student
    if choice == 1:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth: ")
        subjects = input("Enter Subjects separated by comma: ").split(",")

        personal_info = (student_id, dob)

        for subject in subjects:
            subjects_offered.add(subject)

        student = {
            "personal": personal_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)

        print("Student added successfully!")
        print()

    # ---Display Students
    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print("ID:", student["personal"][0])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grade:", student["grade"])
                print("DOB:", student["personal"][1])
                print("Subjects:", student["subjects"])
                print()

    # ---Update Student
    elif choice == 3:
        student_id = int(input("Enter Student ID: "))

        for student in students:
            if student["personal"][0] == student_id:

                print("1. Update Age")
                print("2. Update Subjects")

                update = int(input("Enter choice: "))

                if update == 1:
                    student["age"] = int(input("Enter new age: "))
                    print("Age updated!")

                elif update == 2:
                    subjects = input("Enter new subjects: ").split(",")

                    student["subjects"] = subjects

                    for subject in subjects:
                        subjects_offered.add(subject)

                    print("Subjects updated!")

                break

    # ---Delete Student
    elif choice == 4:
        student_id = int(input("Enter Student ID: "))

        for student in students:
            if student["personal"][0] == student_id:
                students.remove(student)
                del student
                print("Student deleted!")
                break

    # ---Display Subjects
    elif choice == 5:
        print("Subjects Offered:")

        for subject in subjects_offered:
            print(subject)

        print()

    # ---Exit
    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
