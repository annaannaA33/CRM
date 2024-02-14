from Operator import Operator
from Ticket import Ticket
from FileManager import FileManager
import sys
from Salesperson import Salesperson
from ServiceDepartment import ServiceDepartment
from DeliveryDepartment import DeliveryDepartment
import os
import sys
import questionary
from questionary import Choice
from Administrator import Administrator
from User import User


def main():
    operator = Operator()
    file_manager = FileManager()
    file_manager.init_csv_file()
    users = file_manager.load_users()
    role = User.login(users)
    
    if role:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"You login successful! Your role is: {role}")
        # Trigger the appropriate functionality based on the role
        if role == 'admin':
            admin_functionality()
        elif role == 'operator':
            operator_functionality(operator, Ticket)
        elif role == 'sales':
            sales_department_functionality(Salesperson)
        elif role == 'delivery':
            delivery_department_functionality(DeliveryDepartment)
        elif role == 'service':
            service_department_functionality(ServiceDepartment)
    else:
        print("Login failed. Exiting the program.")


def operator_functionality(operator, Ticket):
    file_manager = FileManager()
    operator = Operator()

    while True:
        Operator.print_operator_menu()
        choice = input("ENTER YOUR CHOICE: ").strip()
        if choice == "1":
            # CREATE A NEW REQUEST
            print("CREATING A NEW REQUEST:")
            new_ticket = operator.create_request()
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 30)
            print("New ticket created:")
            print(f"{new_ticket}")  # print the string representation of the new_ticket
            if new_ticket:
                file_manager.save_ticket(new_ticket)
        elif choice == "2":
            # VIEW REQUESTS
            downloaded_requests = []
            downloaded_requests = file_manager.load_tickets_from_file()
            Ticket.print_requests(downloaded_requests)

        elif choice == "3":
            # FILTER REQUESTS
            downloaded_requests = []
            downloaded_requests = file_manager.load_tickets_from_file()
            # filtered_tickets = Ticket.filter_tickets(downloaded_requests)
            Ticket.all_filters(downloaded_requests)
            # Ticket.view_requests(filtered_tickets)

        elif choice == "4":
            # WORK WITH A TICKET
            loaded_requests = []
            required_ticket_number = None
            loaded_requests = file_manager.load_tickets_from_file()

            # Find the request by ticket number, client_phone, etc.
            while True:
                required_ticket_number = input(
                    "ENTER THE TICKET NUMBER TO SEARCH (OR 0 TO RETURN TO THE MENU): "
                ).strip()
                if required_ticket_number == "0":
                    break  # Return to the menu

                # Assuming find_ticket is a method of the Operator class that finds a ticket by its number
                ticket = Ticket.find_ticket(required_ticket_number, loaded_requests)
                if ticket:
                    print(ticket)
                    while True:
                        selected_option = input(
                            "SELECT AN ACTION:\n0. TO RETURN TO THE MENU\n1. VIEW DETAILS\n2. REDIRECT REQUEST\n3. CLOSE TICKET\n4. SEND REMINDER\n5.CHANGE REQUEST STATUS\n ENTER YOUR CHOICE:\n "
                        ).strip()
                        if selected_option == "0":
                            break  # Return to the menu
                        if selected_option not in ["1", "2", "3", "4", "5"]:
                            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION")
                            continue
                        if selected_option == "1":
                            ticket.print_ticket_details(
                                ticket
                            )  # Assuming print_ticket_details is a method of the Ticket class
                        elif selected_option == "2":
                            # redirect request
                            Operator.redirect_request(ticket)
                            file_manager.save_tickets(loaded_requests)
                        elif selected_option == "3":
                            Operator.close_ticket(ticket)
                            file_manager.save_tickets(loaded_requests)
                        elif selected_option == "4":
                            operator.send_reminder(ticket)
                        elif selected_option == "5":
                            # Change request status
                            Operator.change_request_status(ticket)
                            file_manager.save_tickets(loaded_requests)
                    break  # Exit the loop if the ticket is successfully processed
                else:
                    print("TICKET NOT FOUND. PLEASE ENTER A VALID TICKET NUMBER")
        elif choice == "0":
            # RETURN TO ROLE SELECTION MENU
            break
        else:
            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION")


def sales_department_functionality(Salesperson):
    file_manager = FileManager()
    sales_person = Salesperson()
    while True:
        request_to_buy = []
        print("=" * 30)
        print("SALES DEPARTMENT:\n")
        choice = input(
            "SELECT ACTION:   1. VIEW REQUESTS,   2. SEARCH REQUESTS, '0' GO BACK: "
        ).strip()
        if choice == "0":
            return  # Вернуться к выбору роли
        elif choice == "1":  # VIEW REQUESTS
            tickets = file_manager.load_tickets_from_file()
            for ticket in tickets:
                if ticket.executor == "SALES_DEPT":
                    request_to_buy.append(ticket)
            sales_person.print_requests(request_to_buy)

        elif choice == "2":  # SEARCH REQUESTS
            while True:
                request_number = None
                requests = file_manager.load_tickets_from_file()
                request_number = (
                    input("ENTER THE TICKET NUMBER TO SEARCH: ").lower().strip()
                )
                if request_number == "0":
                    break  # Return to the sales department menu
                request = sales_person.find_ticket(request_number, requests)
                if request:
                    print(request)
                    while True:
                        # options for the selected ticket
                        print("PRESS THE NUMBER WITH THE RELEVANT OPTION:")
                        selected_option = input(
                            "SELECT AN ACTION:\n1. VIEW DETAILS\n2. PROCESS THE LEAD\n0. TO RETURN TO THE MENU\n "
                        ).strip()
                        if selected_option not in ["0", "1", "2"]:
                            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION")
                            continue
                        if selected_option == "0":
                            break  # Return to the search requests menu
                        elif selected_option == "1":
                            sales_person.print_ticket_details(request)
                        elif selected_option == "2":  # process_the_lead
                            sales_person.process_the_lead(request)
                            solution = sales_person.process_the_lead(request)
                            if solution:
                                file_manager.save_tickets(requests)
                    break  # Exit the loop if the ticket is successfully processed
                else:
                    print("TICKET NOT FOUND. PLEASE ENTER A VALID TICKET NUMBER")


def service_department_functionality(ServiceDepartment):
    file_manager = FileManager()
    service_dept = ServiceDepartment()
    while True:
        request_to_service = []
        print("=" * 30)
        print("SERVICE DEPARTMENT:\n")
        choice = input("SELECT ACTION: 1. VIEW REQUESTS, 2. SEARCH REQUESTS: ").strip()
        if choice == "1":  # VIEW REQUESTS
            tickets = file_manager.load_tickets_from_file()
            for ticket in tickets:
                if ticket.executor == "SERVICE_DEPT":
                    request_to_service.append(ticket)
            service_dept.print_requests(request_to_service)

        elif choice == "2":  # SEARCH REQUESTS
            while True:
                request_number = None
                requests = file_manager.load_tickets_from_file()
                request_number = input("ENTER THE TICKET NUMBER TO SEARCH:")
                request = service_dept.find_ticket(request_number, requests)
                if request:
                    print(request)
                    while True:
                        print("PRESS THE NUMBER CORRESPONDING TO THE OPTION:")
                        selected_option = input(
                            "SELECT AN ACTION:\n1. VIEW DETAILS\n2. PROCESS THE LOGISTICS REQUEST\n0. TO RETURN TO THE MENU:\n "
                        ).strip()
                        if selected_option not in ["0", "1", "2"]:
                            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION")
                            continue
                        if selected_option == "0":
                            break  # Return to the menu
                        elif selected_option == "1":
                            service_dept.print_ticket_details(request)
                        elif selected_option == "2":  # process_service_request
                            solution = service_dept.process_service_request(request)
                            if solution:
                                file_manager.save_tickets(requests)
                    break  # Exit the loop if the ticket is successfully processed
                else:
                    print("TICKET NOT FOUND. PLEASE ENTER A VALID TICKET NUMBER")

        elif choice == "0":
            # RETURN TO ROLE SELECTION MENU
            break
        else:
            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION")


def delivery_department_functionality(DeliveryDepartment):
    file_manager = FileManager()
    delivery_dept = DeliveryDepartment()
    while True:
        request_to_deliver = []
        print("=" * 30)
        print("LOGISTICS DEPARTMENT:\n")
        choice = input(
            "SELECT ACTION:   1. VIEW REQUESTS,   2. SEARCH REQUESTS, '0' GO BACK: "
        ).strip()
        if choice == "0":
            break  # Return to the main menu
        elif choice == "1":  # VIEW REQUESTS
            tickets = file_manager.load_tickets_from_file()
            for ticket in tickets:
                if ticket.executor == "LOGISTICS_DEPT":
                    request_to_deliver.append(ticket)
            delivery_dept.print_requests(request_to_deliver)

        elif choice == "2":  # SEARCH REQUESTS
            while True:
                request_number = None
                requests = file_manager.load_tickets_from_file()
                request_number = input("ENTER THE TICKET NUMBER TO SEARCH: ").strip()
                if request_number == "0":
                    break  # Return to the logistics department menu
                request = delivery_dept.find_ticket(request_number, requests)
                if request:
                    print(request)
                    while True:
                        print("PRESS THE NUMBER CORRESPONDING TO THE DESIRED OPTION: ")
                        selected_option = input(
                            "SELECT AN ACTION:\n1. VIEW DETAILS\n2. PROCESS THE LOGISTICS REQUEST\n0. TO RETURN TO THE MENU:\n "
                        ).strip()
                        if selected_option not in ["0", "1", "2"]:
                            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION")
                            continue
                        if selected_option == "0":
                            break  # Return to the search requests menu
                        elif selected_option == "1":
                            delivery_dept.print_ticket_details(request)
                        elif selected_option == "2":  # process_logistics_request
                            solution = delivery_dept.process_logistics_request(request)
                            if solution:
                                file_manager.save_tickets(requests)
                    break  # Exit the loop if the ticket is successfully processed
                else:
                    print("TICKET NOT FOUND. PLEASE ENTER A VALID TICKET NUMBER")


def admin_functionality():
    admin = Administrator('admin_username', 'admin_password', 'admin_department')
    
    while True:
        print("\nADMINISTRATOR MODE:")
        print("1. Manage Users")
        print("2. Manage Tickets")
        print("0. Exit Admin Mode")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manage_users()  
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def manage_users():
    file_manager = FileManager()
    while True:
        print("\nMANAGE USERS:")
        print("1. Register New User")
        print("2. View All Users")
        print("3. Delete User")
        print("0. Go Back")
        choice = int(input("Enter your choice: ").strip())

        if choice == 1:
            # Register New User
            new_user = Administrator.register_user()
            file_manager.save_new_user(new_user) 
        elif choice == 2: 
            # View All Users
            users = file_manager.load_users()
            for user in users:
                print(user)
        elif choice == 3:
            # Delete User
            users = file_manager.load_users()
            users = Administrator.delete_user(users)
            file_manager.save_all_users(users)

        elif choice == 0:
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
