from sorting import bubble_sort, quick_sort
from storage import students

# Module 1: Create New Records
def create_new():
    """
    Creates a new student record and adds it to the list.
    """
    while True:
        student = {
            "Major": input("Major: "),
            "ID": input("ID: "),
            "Name": input("Name: "),
            "Gender": input("Gender: "),
            "Subject": input("Subject: "),
            "Score": int(input("Score: ")),
        }
        students.append(student)
        print("Student info successfully created.")
        if input("Would you like to create another? (Y/N): ").upper() != 'Y':
            break

# Module 2: Show All Records
def show_all():
    """
    Displays all student records in a table format.
    Allows sorting by ID or Score.
    """
    if not students:
        print("No records available.")
        return
    print("\nMajor\tID\t\tName\t\tGender\t\tSubject\t\tScore")
    for student in students:
        print(f"{student['Major']}\t{student['ID']}\t\t{student['Name']}\t\t{student['Gender']}\t\t{student['Subject']}\t\t{student['Score']}")
        #Coded by AHMED MD SHAKIL 

    choice = int(input("\nPlease choose the mode for display: 1. Sort by ID; 2. Sort by Score: "))
    if choice == 1:
        sorted_students = bubble_sort(students, key="ID")
    elif choice == 2:
        sorted_students = quick_sort(students, key="Score")
    else:
        print("Invalid choice!")
        return

    print("\nSorted Records:")
    for student in sorted_students:
        print(f"{student['Major']}\t{student['ID']}\t{student['Name']}\t{student['Gender']}\t{student['Subject']}\t\t{student['Score']}") 
        #Coded by AHMED MD SHAKIL 

# Module 3: Query Records
def query():
    """
    Searches for a student by name and allows modification or deletion.
    """
    name = input("Please input the student name for query: ")
    matches = [s for s in students if s["Name"] == name]
    if not matches:
        print("No matching records found.")
        return

    student = matches[0]
    print(f"\nMajor: {student['Major']} ID: {student['ID']} Name: {student['Name']} Gender: {student['Gender']} Subject: {student['Subject']} Score: {student['Score']}")
    #Coded by AHMED MD SHAKIL 

    choice = int(input("\n1. Modify; 2. Delete; 0. Back to menu: "))
    if choice == 1:
        modify(student)
    elif choice == 2:
        students.remove(student)
        print("Record deleted successfully.")
    elif choice == 0:
        return
    else:
        print("Invalid choice!")

# Module 4: Modify a Record
def modify(student):
    """
    Allows the user to modify the student's information.
    """
    print("\nTo modify, leave blank to keep the current value.")
    for key in student:
        new_value = input(f"Input new value for {key} ({student[key]}): ")
        if new_value:
            student[key] = int(new_value) if key == "Score" else new_value
    print("Modification successful!")
