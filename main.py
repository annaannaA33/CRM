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
        print("4. EXIT")
        choice = input("ENTER YOUR CHOICE: (1 FOR OPERATOR, 2 FOR SALESPERSON, 3 FOR DELIVERY, 4 TO EXIT): ").strip().lower()
        if choice == "1":
            operator_functionality(operator)
        elif choice == "4":
            sys.exit("EXITING THE PROGRAM. GOODBYE!")
        else:
            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION.")

def print_operator_menu():
    
    print("WELCOME TO OPERATOR MODE. PLEASE SELECT FUNCTIONS:")
    print("1. CREATE A NEW REQUEST")
    print("2. VIEW REQUESTS")
    print("0. RETURN TO ROLE SELECTION MENU")
    print("3 TO USE FILTRES")
    #print("2. CLOSE A REQUEST")
    #print("3. REDIRECT A REQUEST")
    #print("5. PROCESS A REQUEST")
    #print("6. SEND A REMINDER")
           

def operator_functionality(operator):
    file_manager = FileManager()
    while True:
        print_operator_menu()
        choice = input("ENTER YOUR CHOICE: ")
        if choice == "1":
            # CREATE A NEW REQUEST
            print("CREATING A NEW REQUEST:")
            new_ticket = operator.create_request() 
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
            downloaded_requests = []
            downloaded_requests = file_manager.load_tickets_from_file()
            filtered_tickets = Ticket.filter_tickets(downloaded_requests)
            Ticket.view_requests(filtered_tickets)


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

def view_requests(operator):
    # Implement logic to get input for viewing requests
    status = input("Enter the status to filter (or press Enter to view all): ")
    operator.view_requests(status)

def process_request(operator):
    # Implement logic to get input for processing a request
    ticket_number = input("Enter the ticket number to process: ")
    ticket = find_ticket(operator, ticket_number)

    if ticket:
        operator.process_request(ticket)

def send_reminder(operator):
    # Implement logic to get input for sending a reminder
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