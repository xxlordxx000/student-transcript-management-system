import csv

# Data structure to hold student records
students = []

# Module 5: Save and Quit
def save_and_quit():
    """
    Saves the student data to a CSV file and exits the program.
    """
    output_file = "student.csv"
    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Major", "ID", "Name", "Gender", "Subject", "Score"]
        )
        writer.writeheader()
        writer.writerows(students)

    print("File successfully saved. Welcome next use!")
    exit()
