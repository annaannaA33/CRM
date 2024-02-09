from Operator import Operator
from Ticket import Ticket
from FileManager import FileManager
import sys

def main():
    select_role()
    ticket: Ticket = Ticket(ticket_number, client_name, client_phone, request_type, source, description, executor)

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
            operator_functionality(operator, Ticket)
        elif choice == "x":
            sys.exit("EXITING THE PROGRAM. GOODBYE!")
        else:
            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION.")


def operator_functionality(operator, Ticket):
    file_manager = FileManager()
    operator = Operator()

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
            #filtered_tickets = Ticket.filter_tickets(downloaded_requests)
            Ticket.all_filters(downloaded_requests)
            #Ticket.view_requests(filtered_tickets)

        elif choice == "4":
            # WORK WITH A TICKET
            loaded_requests = []
            required_ticket_number = None
            loaded_requests = file_manager.load_tickets_from_file()

            # Find the request by ticket number, client_phone, etc.
            while True:
                required_ticket_number = input("Enter the number of the ticket (or X to return to the menu): ").strip().lower()
                if required_ticket_number == "x":
                    break  # Return to the menu

                # Assuming find_ticket is a method of the Operator class that finds a ticket by its number
                ticket = Ticket.find_ticket(required_ticket_number, loaded_requests)
                if ticket:
                    print(ticket)
                    while True:
                        selected_option = input("Select an action:\n1. View details\n2. Redirect request\n3. Close ticket\n4. Send reminder\n5.Change request status\n Enter your choice (X to return to the menu):\n ").strip().lower()
                        if selected_option.lower() == "x":
                            break  # Return to the menu
                        if selected_option not in ["1", "2", "3", "4", "5"]:
                            print("Invalid choice. Please enter a valid option.")
                            continue
                        if selected_option == "1":
                            ticket.print_ticket_details()  # Assuming print_ticket_details is a method of the Ticket class
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
                    print("Ticket not found. Please enter a valid ticket number.")


        elif choice == "0":
            # RETURN TO ROLE SELECTION MENU
            break
        else:
            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION")




if __name__ == "__main__":
    main()