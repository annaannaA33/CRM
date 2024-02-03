from Operator import Operator

def main():
    operator = Operator()

    while True:
        role = input("Enter your role (Operator/Salesperson/Delivery): ").lower()

        if role == "operator":
            operator_functionality(operator)
        #elif role == "salesperson":
       #     salesperson_functionality()
        #elif role == "delivery":
        #    delivery_functionality()
       # elif role == "exit":
         #   print("Exiting the program. Goodbye!")
         #   break
        else:
            print("Invalid role. Please try again.")

def operator_functionality(operator):
    while True:
        print("Operator, you can:")
        print("1. Create a new request")
        print("2. Close a request")
        print("3. Redirect a request")
        print("4. View requests")
        print("5. Process a request")
        print("6. Send a reminder")
        print("7. Exit to the main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_request(operator)
        elif choice == "2":
            close_request(operator)
        elif choice == "3":
            redirect_request(operator)
        elif choice == "4":
            view_requests(operator)
        elif choice == "5":
            process_request(operator)
        elif choice == "6":
            send_reminder(operator)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def create_request(operator):
    # Implement logic to get input for creating a request
    ticket = operator.create_request(ticket.ticket_number, ticket.client_name, ticket.client_phone, ticket.request_type, ticket.source, ticket.executor, ticket.description)
    # You may want to save the data to CSV here

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