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

def print_operator_memu():
    
    print("WELCOME TO OPERATOR MODE. PLEASE SELECT FUNCTIONS:")
    print("1. CREATE A NEW REQUEST")
    print("2. VIEW REQUESTS")
    print("3. RETURN TO ROLE SELECTION MENU")
    #print("2. CLOSE A REQUEST")
    #print("3. REDIRECT A REQUEST")
    #print("5. PROCESS A REQUEST")
    #print("6. SEND A REMINDER")
           

def operator_functionality(operator):
    file_manager = FileManager()
    while True:
        print_operator_memu()
        choice = input("ENTER YOUR CHOICE: ")
        if choice == "1":
            # CREATE A NEW REQUEST
            print("CREATING A NEW REQUEST:")
            new_ticket = operator.create_request() 
            print(f"{new_ticket}") # print the string representation of the new_ticket
            if new_ticket:
                file_manager.save_ticket(new_ticket)

        elif choice == "2":
            # VIEW REQUESTS
            downloaded_requests = file_manager.load_tickets_from_file()

            # Варианты выбора для фильтрации
            status_choices = {'1': 'active', '2': 'in progress', '3': 'resolved', '4': 'closed'}
            executor_choices = {'1': 'SERVICE_DEPT', '2': 'LOGISTICS_DEPT', '3': 'SALES_DEPT'}
            source_choices = {'1': 'CHAT', '2': 'CALL'}
            phone_choices = {'1': 'full', '2': 'partial', '3': 'skip'}

            # Вывести варианты выбора
            print("Status Choices:")
            for key, value in status_choices.items():
                print(f"{key}. {value}")

            print("Executor Choices:")
            for key, value in executor_choices.items():
                print(f"{key}. {value}")

            print("Source Choices:")
            for key, value in source_choices.items():
                print(f"{key}. {value}")

            print("Phone Choices:")
            for key, value in phone_choices.items():
                print(f"{key}. {value}")

            # Запросить ввод пользователя
            status = status_choices.get(input("Enter the status to filter (or press Enter to skip): "), None)
            executor = executor_choices.get(input("Enter the executor to filter (or press Enter to skip): "), None)
            source = source_choices.get(input("Enter the source to filter (or press Enter to skip): "), None)

            phone_choice = input("Choose an option for phone filtering: ").strip()
            phone_filter = None
            if phone_choice == '1':
                phone_filter = input("Enter the full phone number to filter: ")
            elif phone_choice == '2':
                phone_filter = input("Enter the partial phone number to filter: ")

            # Фильтрация заявок
            filtered_tickets = Ticket.filter_tickets(downloaded_requests,
                                                    status=status,
                                                    executor=executor,
                                                    source=source,
                                                    phone_filter=phone_filter)

            # Вывести отфильтрованные заявки
            Ticket.print_tickets(filtered_tickets)


        elif choice == "3":
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