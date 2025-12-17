#Student Transcript Management System
#Coded by AHMED MD SHAKIL

from menu import welcome_menu
from student import create_new, show_all, query
from storage import save_and_quit

# Main Program
def main():
    """
    Main function to control the program flow.
    """
    while True:
        welcome_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            create_new()
        elif choice == "2":
            show_all()
        elif choice == "3":
            query()
        elif choice == "0":
            save_and_quit()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    
    #Coded by AHMED MD SHAKIL
