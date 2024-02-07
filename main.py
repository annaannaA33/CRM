from Operator import Operator
from Ticket import Ticket
from FileManager import FileManager
import sys

def main():
    select_role()

def select_role():
    operator = Operator()
    
    while True:
        print("WELCOME TO THE ONLINE STORE CRM SYSTEM! PLEASE SELECT YOUR ROLE:")
        print("1. OPERATOR")
        print("2. SALESPERSON")
        print("3. DELIVERY")
        print("X EXIT")


        choice = input("ENTER YOUR CHOICE: (1 FOR OPERATOR, 2 FOR SALESPERSON, 3 FOR DELIVERY, 'X' TO EXIT): ").strip().lower()
        if choice == "1":
            operator_functionality(operator)
        elif choice == "x":
            sys.exit("EXITING THE PROGRAM. GOODBYE!")
        else:
            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION.")


    
           

def operator_functionality(operator):
    file_manager = FileManager()
    operator = Operator()
    #ticket = Ticket(ticket.ticket_number, ticket.client_name, ticket.client_phone, ticket.request_type, ticket.source, ticket.description, ticket.executor, ticket.status, ticket._solution, ticket.created_at)
    while True:
        Operator.print_operator_menu()
        choice = input("ENTER YOUR CHOICE: ").strip()
        if choice == "1":
            # CREATE A NEW REQUEST
            print("CREATING A NEW REQUEST:")
            new_ticket = operator.create_request() # сделать тикет суперклассом.но сначала сохранить
            print("New ticket created")
            print(f"{new_ticket}") # print the string representation of the new_ticket
            if new_ticket:
                file_manager.save_ticket(new_ticket)

        elif choice == "2":
            # VIEW REQUESTS
            downloaded_requests = []
            downloaded_requests = file_manager.load_tickets_from_file()
            Ticket.view_requests(downloaded_requests)

        elif choice == "3":
            # FILTER REQUESTS
            downloaded_requests = []
            downloaded_requests = file_manager.load_tickets_from_file()
            filtered_tickets = Ticket.filter_tickets(downloaded_requests)
            Ticket.view_requests(filtered_tickets)

        elif choice == "4":
            # WORK WITH A TICKET
            loaded_requests = []
            required_ticket_number = None
            loaded_requests = file_manager.load_tickets_from_file()
            ticket = None  # Initialize the ticket variable

            # Find the request by ticket number, client_phone, etc.
            while True:
                required_ticket_number = input("Enter the number of the ticket (or X to return to the menu): ").strip()
                if required_ticket_number.lower() == "x":
                    break  # Return to the menu

                # Assuming find_ticket is a method of the Operator class that finds a ticket by its number
                ticket = operator.find_ticket(required_ticket_number, loaded_requests)
                if ticket:
                    print(ticket)
                    while True:
                        selected_option = input("Select an action:\n1. View details\n2. Redirect request\n3. Close ticket\n4. Send reminder\nEnter your choice (X to return to the menu): ").strip().lower()
                        if selected_option.lower() == "x":
                            break  # Return to the menu
                        if selected_option not in ["1", "2", "3", "4"]:
                            print("Invalid choice. Please enter a valid option.")
                            continue
                        if selected_option == "1":
                            ticket.print_ticket_details()  # Assuming print_ticket_details is a method of the Ticket class
                        elif selected_option == "2":  
                            # redirect request
                            operator.redirect_request(ticket)
                        elif selected_option == "3":
                            Operator.close_ticket(ticket)
                        elif selected_option == "4":
                            operator.send_reminder(ticket)
                    break  # Exit the loop if the ticket is successfully processed
                else:
                    print("Ticket not found. Please enter a valid ticket number.")


        elif choice == "0":
            # RETURN TO ROLE SELECTION MENU
            break
        else:
            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION")


def close_request(operator):
    # Implement logic to get input for closing a request
    ticket_number = input("Enter the ticket number to close: ")
    ticket = find_ticket(operator, ticket_number)

    if ticket:
        operator.close_request(ticket)

def redirect_request(operator):
    # Implement logic to get input for redirecting a request
    ticket_number = input("Enter the ticket number to redirect: ")
    ticket = find_ticket(operator, ticket_number)

    if ticket:
        new_executor = input("Enter the new executor: ")
        operator.redirect_request(ticket, new_executor)

def process_request(operator):
    # Implement logic to get input for processing a request
    ticket_number = input("Enter the ticket number to process: ")
    ticket = find_ticket(operator, ticket_number)

    if ticket:
        operator.process_request(ticket)

def send_reminder(operator):
    #  to get input for sending a reminder
    ticket_number = input("Enter the ticket number to send a reminder: ")
    ticket = find_ticket(operator, ticket_number)

    if ticket:
        operator.send_reminder(ticket)

def find_ticket(operator, ticket_number):
    for ticket in operator.tickets:
        if ticket.ticket_number == ticket_number:
            return ticket

    print(f"Ticket {ticket_number} not found.")
    return None

if __name__ == "__main__":
    main()