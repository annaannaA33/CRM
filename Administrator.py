import csv
from Operator import Operator
from User import User
import os


class Administrator(User, Operator):
    
    def __init__(self, username, password, role):
        super().__init__(username, password, role)
        self.username = username
        self.password = self.hash_password(password)
        self.role = role


    @staticmethod
    def register_user():
        while True:
            username = input("Enter username: ").strip()
            if len(username) <  3:
                print("Username must have at least  3 characters. Please try again.")
                continue
            password = input("Enter password: ").strip()
            if len(password) <  5:
                print("Password must have at least  5 characters. Please try again.")
                continue
            departments = ["operator", "delivery", "sales", "service"]
            while True:
                print("Available departments:")
                for i, dept in enumerate(departments,  1):
                    print(f"{i}. {dept}")
                department_choice = input("Choose department by entering its number: ").strip()
                if department_choice == "0":
                    break
                try:
                    department_choice = int(department_choice)
                    if  1 <= department_choice <=  4:
                        department = departments[department_choice -  1]
                        break
                    else:
                        print("Invalid department choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number corresponding to a department.")
            new_user = User(username, password, department)
            print(new_user)
            print("New user registered successfully.")
            return new_user

    def manage_tickets(self, file_manager):
        while True:
            print("\nMANAGE TICKETS:")
            print("1. View All Tickets")
            print("2. Search Tickets")
            print("3. Update Ticket")
            print("0. Go Back")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                Operator.print_requests(file_manager)
            elif choice == "2":
                downloaded_requests = file_manager.load_tickets_from_file()
                ticket_number = input("ENTER THE TICKET NUMBER TO SEARCH (OR 0 TO RETURN TO THE MENU): ").strip()
                if ticket_number == "0":
                    break  # Return
                Operator.find_ticket(ticket_number, downloaded_requests)
            #elif choice == "3":
            #    pass
            elif choice == "0":
                break # Return
            else:
                print("Invalid choice. Please enter a valid option.")

    def delete_user(users):
        while True:
            input_login = input('Enter the login to delete user (or 0 to go back): ')
            if input_login == "0":
                break
            try:
                user_to_delete = next(user for user in users if user.login == input_login)
                users.remove(user_to_delete)
                print("User successfully deleted.")
            except StopIteration:
                print("User not found.")
            else:
                return users


