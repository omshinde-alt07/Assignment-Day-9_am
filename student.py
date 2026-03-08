records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Sneha", "Chemistry", 85],
    ["Arjun", "Physics", 79],
    ["Neha", "Math", 92],
    ["Kiran", "Chemistry", 67],
    ["Riya", "Physics", 83],
    ["Vikram", "Math", 74],
    ["Pooja", "Chemistry", 90],
]


def add_student(name, subject, marks):
    for r in records:
        if r[0] == name and r[1] == subject:
            print("Duplicate entry not allowed.")
            return

    records.append([name, subject, marks])
    print("Student added successfully.")


def get_toppers(subject):
    subject_students = [r for r in records if r[1] == subject]

    toppers = sorted(subject_students, key=lambda x: x[2], reverse=True)[:3]

    if not toppers:
        print("No students found for this subject.")
        return

    print("\nTop Students in", subject)
    for t in toppers:
        print(t)


def class_average(subject):
    marks = [r[2] for r in records if r[1] == subject]

    if not marks:
        print("No records found.")
        return

    avg = sum(marks) / len(marks)
    print(f"Average marks in {subject}: {avg:.2f}")


def above_average_students():
    all_marks = [r[2] for r in records]

    overall_avg = sum(all_marks) / len(all_marks)

    result = [r for r in records if r[2] > overall_avg]

    print("\nStudents above class average:")
    for r in result:
        print(r)

    print("Class Average:", round(overall_avg, 2))


def remove_student(name):
    global records

    records = [r for r in records if r[0] != name]

    print("Student records removed if existed.")



def save_to_file():
    with open("students.txt", "w") as f:
        for r in records:
            line = ",".join([r[0], r[1], str(r[2])])
            f.write(line + "\n")

    print("Records saved to students.txt")

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add student")
        print("2. Show toppers")
        print("3. Show class average")
        print("4. Show above-average students")
        print("5. Remove student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            add_student(name, subject, marks)

        elif choice == "2":
            subject = input("Enter subject: ")
            get_toppers(subject)

        elif choice == "3":
            subject = input("Enter subject: ")
            class_average(subject)

        elif choice == "4":
            above_average_students()

        elif choice == "5":
            name = input("Enter student name to remove: ")
            remove_student(name)

        elif choice == "6":
            save_to_file()
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")



menu()