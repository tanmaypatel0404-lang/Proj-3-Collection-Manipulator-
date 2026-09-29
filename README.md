# 🎓 Student Data Organizer

> A simple **Python-based Student Data Organizer** that allows you to add, view, update, delete, and manage student information through a menu-driven program.

---

## 📌 About the Project

The **Student Data Organizer** is a beginner-friendly Python project designed to practice important Python concepts such as:

* 📝 Lists
* 🔤 Strings
* 🔢 Integers
* 📦 Dictionaries
* 🔒 Tuples
* 🧮 Sets
* 🔄 Loops
* 🔀 Conditional statements
* ⌨️ User input
* 🛠️ Basic CRUD operations

The program runs continuously using a `while` loop until the user chooses **Exit**.

---

## ✨ Features

| Option | Feature          | Description                     |
| ------ | ---------------- | ------------------------------- |
| 1️⃣    | Add Student      | Add a new student's information |
| 2️⃣    | Display Students | View all stored students        |
| 3️⃣    | Update Student   | Update age or subjects          |
| 4️⃣    | Delete Student   | Remove a student                |
| 5️⃣    | Display Subjects | Show all unique subjects        |
| 6️⃣    | Exit             | Close the program               |

---

## 🧠 How the Program Works

When the program starts, it displays:

```text
Welcome to the Student Data Organizer
```

Then it shows a menu:

```text
1. Add Student
2. Display All Students
3. Update Student
4. Delete Student
5. Display Subjects
6. Exit
```

The user selects an option, and the program performs the corresponding operation.

The `while True` loop keeps showing the menu until the user selects **6. Exit**.

---

# 📦 Data Structures Used

One of the main purposes of this project is to understand how different Python data structures can work together.

### 1. List — `students`

```python
students = []
```

This empty list stores all the student records.

Whenever a new student is added:

```python
students.append(student)
```

the student's dictionary is added to the list.

For example:

```python
students = [
    student1,
    student2,
    student3
]
```

So, the **list stores multiple students**.

---

### 2. Set — `subjects_offered`

```python
subjects_offered = set()
```

This set stores all the subjects offered by the students.

A set is useful because it automatically avoids duplicate values.

For example:

```text
Student 1 → Python, Maths
Student 2 → Python, Science
```

The set will contain:

```text
Python
Maths
Science
```

instead of storing `Python` twice.

A subject is added using:

```python
subjects_offered.add(subject)
```

---

### 3. Tuple — `personal_info`

```python
personal_info = (student_id, dob)
```

The tuple stores:

* Student ID
* Date of Birth

Example:

```python
(101, "15-08-2005")
```

The tuple is then stored inside the student's dictionary.

---

### 4. Dictionary — `student`

Each student is represented using a dictionary:

```python
student = {
    "personal": personal_info,
    "name": name,
    "age": age,
    "grade": grade,
    "subjects": subjects
}
```

This makes the student's information easy to organize.

For example:

```text
Student
│
├── Personal
│   ├── ID
│   └── DOB
│
├── Name
├── Age
├── Grade
└── Subjects
```

---

# ➕ 1. Add Student

The first option collects information from the user:

```python
student_id = int(input("Enter Student ID: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))
grade = input("Enter Grade: ")
dob = input("Enter Date of Birth: ")
subjects = input("Enter Subjects separated by comma: ").split(",")
```

The `.split(",")` function converts the subjects entered with commas into a list.

For example:

```text
Python,Maths,Science
```

becomes:

```python
["Python", "Maths", "Science"]
```

The student's information is then stored in a dictionary and added to the `students` list:

```python
students.append(student)
```

---

# 👀 2. Display All Students

The program first checks whether there are any students:

```python
if len(students) == 0:
    print("No students found.")
```

If students exist, the program uses a `for` loop:

```python
for student in students:
```

It then displays the student's information.

For example:

```text
ID: 101
Name: Rahul
Age: 18
Grade: A
DOB: 15-08-2008
Subjects: ['Python', 'Maths']
```

---

# ✏️ 3. Update Student

The user enters the Student ID:

```python
student_id = int(input("Enter Student ID: "))
```

The program searches for that ID:

```python
for student in students:
    if student["personal"][0] == student_id:
```

The `[0]` accesses the Student ID from the tuple.

The user can then choose:

```text
1. Update Age
2. Update Subjects
```

### Update Age

```python
student["age"] = int(input("Enter new age: "))
```

### Update Subjects

```python
subjects = input("Enter new subjects: ").split(",")
student["subjects"] = subjects
```

The new subjects are also added to `subjects_offered`.

---

# 🗑️ 4. Delete Student

The user enters the Student ID that should be deleted.

The program searches through the list:

```python
for student in students:
```

When the matching student is found:

```python
students.remove(student)
```

The student is removed from the list.

Then:

```python
break
```

stops the loop.

---

# 📚 5. Display Subjects

This option displays all subjects stored in the set:

```python
for subject in subjects_offered:
    print(subject)
```

Because `subjects_offered` is a **set**, duplicate subjects are automatically avoided.

Example:

```text
Subjects Offered:
Python
Maths
Science
English
```

---

# 🚪 6. Exit

When the user chooses option `6`:

```python
elif choice == 6:
    print("Thank you!")
    break
```

The `break` statement stops the `while True` loop and ends the program.

---

# 🔄 Program Flow

```text
                START
                  │
                  ▼
        Welcome Message
                  │
                  ▼
            Display Menu
                  │
                  ▼
          User selects option
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Add      Display    Update
        │         │         │
        └─────────┼─────────┘
                  │
                  ▼
               Delete
                  │
                  ▼
          Display Subjects
                  │
                  ▼
                Exit?
              /       \
            No         Yes
            │           │
            └──► Menu   ▼
                      END
```

---

# 🛠️ Python Concepts Used

| Python Concept     | Used For                                        |
| ------------------ | ----------------------------------------------- |
| `list`             | Storing students                                |
| `dictionary`       | Storing student details                         |
| `tuple`            | Storing ID and DOB                              |
| `set`              | Storing unique subjects                         |
| `while` loop       | Keeping the menu running                        |
| `for` loop         | Searching and displaying students               |
| `if / elif / else` | Making decisions                                |
| `input()`          | Taking user information                         |
| `int()`            | Converting input to numbers                     |
| `.append()`        | Adding students                                 |
| `.remove()`        | Deleting students                               |
| `.add()`           | Adding subjects to set                          |
| `.split()`         | Converting comma-separated subjects into a list |
| `break`            | Stopping loops                                  |
| `del`              | Deleting the student variable                   |

---

# ▶️ How to Run

### 1️⃣ Install Python

Make sure Python is installed on your computer.

### 2️⃣ Save the file

Save the program as:

```text
student_data_organizer.py
```

### 3️⃣ Run the program

Open your terminal and use:

```bash
python student_data_organizer.py
```

---

# 💻 Example

```text
Welcome to the Student Data Organizer

1. Add Student
2. Display All Students
3. Update Student
4. Delete Student
5. Display Subjects
6. Exit

Enter your choice: 1

Enter Student ID: 101
Enter Name: Rahul
Enter Age: 18
Enter Grade: A
Enter Date of Birth: 15-08-2008
Enter Subjects separated by comma: Python,Maths,Science

Student added successfully!
```

After selecting **Display All Students**:

```text
ID: 101
Name: Rahul
Age: 18
Grade: A
DOB: 15-08-2008
Subjects: ['Python', 'Maths', 'Science']
```

---

# 🎯 Learning Objective

This project is mainly created to understand how different Python concepts can be combined to build a small real-world application.

Instead of learning lists, dictionaries, tuples, sets, loops, and conditions separately, this project shows how they can **work together in one program**.

---

# 🚀 Future Improvements

The project can be improved by adding:

* 🔍 Search student by ID or name
* 🛡️ Input validation
* 📊 Student marks and percentage
* 🏆 Grade calculation
* 💾 Save data to a file
* 📂 Read data from a file
* 📑 Export student data to CSV
* 🖥️ Graphical User Interface (GUI)
* 🗄️ Database support

---

## ⭐ Conclusion

**Student Data Organizer** is a simple but useful Python project for practicing fundamental programming concepts.

It demonstrates how:

```text
List + Dictionary + Tuple + Set
              ↓
        Student Data
              ↓
       CRUD Operations
              ↓
      Complete Python Project
```

> 💡 **Made with Python 🐍 — Learn → Practice → Build → Improve**

---

## 👨‍💻 Demo-Video

https://github.com/user-attachments/assets/c7fbf80a-b624-417d-aaaf-9cb044d0616c


