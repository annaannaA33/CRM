import datetime
import uuid
import re
from RequestType import RequestType, TicketStatus, Source, Executor




class Ticket:
    def __init__(self, ticket_number, client_name, client_phone, request_type, source, description, executor, solution, created_at, status="active"):
        self.ticket_number = ticket_number
        self._client_name = client_name
        self._client_phone = client_phone
        self.request_type = request_type
        self.source = source
        self.description = description
        self.executor = executor
        self.solution = solution
        self.created_at = created_at
        self.status = status

    def __str__(self):
        return f"\n #: {self.ticket_number}\n -----\n CUSTOMER INFORMATION: \n NAME: {self.client_name}\n PHONE: {self.client_phone}\n REQUEST TYPE: {self.request_type}\n SOURCE: {self.source}\n DESCRIPTION: {self.description}\n EXECUTOR: {self.executor}\n STATUS: {self.status}\n DATE AND TIME CREATED: {self.created_at}\n -----\n"



    def generate_ticket_number(self):
        self.ticket_number = uuid.uuid4()
        return self.ticket_number
    
    def get_created_at(self):
        created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        return created_at
    

    # client_name    
    @property
    # getter
    def client_name(self):
        return self._client_name
    

    @client_name.setter
    def client_name(self, value):
        if len(value) >= 3 and not any(char.isdigit() for char in value):
            self._client_name = value
        else:
            raise ValueError("Invalid client name")
        
    # client_phone
    @property
    def client_phone(self):
        return self._client_phone
    
    @client_phone.setter
    def client_phone(self, value):
        if re.match(r'^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,9}$', value):
            self._client_phone = value
        else:
            raise ValueError("Invalid phone number")
    
        
    # description            
    @property
    # getter
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if len(value) >= 5:
            self._description = value
        else:
            raise ValueError("Description must be at least 5 characters long")

    
    def as_dict(self):
        return {
            "ticket_number": self.ticket_number,
            "client_name": self._client_name,
            "client_phone": self._client_phone,
            "request_type": self.request_type,
            "source": self.source,
            "description": self.description,
            "executor": self.executor,
            "status": self.status,
            "solution": self.solution,
            "created_at": self.created_at,
        }
    

    @staticmethod
    def print_requests(list_of_tickets):
        if not list_of_tickets:
            print("No tickets available.")
        else:
            print('=' * 30)
            print("Tickets:")
            print('=' * 30)
            for ticket in list_of_tickets:
                print(f"Ticket Number: {ticket.ticket_number}")
                print(f"Client Name: {ticket.client_name}")
                print(f"Client Phone: {ticket.client_phone}")
                print(f"Request Type: {ticket.request_type}")
                print(f"Source: {ticket.source}")
                print(f"Description: {ticket.description}")
                print(f"Executor: {ticket.executor}")
                print(f"Status: {ticket.status}")
                print(f"Solution: {'Waiting for resolution' if not ticket.solution else 'Answered... open request view more'}")
                print(f"Created At: {ticket.created_at}")
                print("-" * 30)
  
   
    def print_ticket_details(self, ticket):
        print('-' * 30)
        print(ticket)
        print(f"Solution: {'Waiting for resolution' if not ticket.solution else ticket.solution}")
        print('-' * 30)

    @staticmethod
    def find_ticket(ticket_number, tickets):
        for ticket in tickets:
            if str(ticket.ticket_number) == ticket_number:
                return ticket
        return None
    
    @staticmethod
    def filter_source(tickets):
        filtered_tickets = []
        # Prompt user to select the filter option
        filter_value = int(input("Enter the number of your choice: 1. CHAT 2. CALL: ").strip().lower())
        while True:
            if filter_value == 1:
                # Filter tickets based on the selected option
                for ticket in tickets:
                    if ticket.source == "CHAT":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == 2:
                for ticket in tickets:
                    if ticket.source == "CALL":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == 0:
                break
            else:
                print("Choose option 0. BACK 1. CHAT 2. CALL")
        return filtered_tickets
    
    @staticmethod
    def filter_status(tickets):
        filtered_tickets = []
        # Prompt user to select the filter option
        filter_value = int(input("Enter the number of your choice:\n 1. active\n 2. in progress\n 3. resolved\n 4. closed:\n ").strip().lower())
        while True:
            if filter_value == 1:
                # Filter tickets based on the selected option
                for ticket in tickets:
                    if ticket.status == "active":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == 2:
                for ticket in tickets:
                    if ticket.status == "in progress":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == 3:
                for ticket in tickets:
                    if ticket.status == "resolved":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == 4:
                for ticket in tickets:
                    if ticket.status == "closed":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == "x":
                break
            else:
                print("Choose option 1. active 2. in progress 3. resolved 4. closed")
        return filtered_tickets

    @staticmethod
    def filter_phone(tickets):
        filtered_tickets = []
        # Prompt user to enter the phone number to filter by
        filter_value = input("Enter the client phone number: ").strip()
        # Filter tickets based on the entered phone number
        filtered_tickets = [ticket for ticket in tickets if ticket.client_phone == filter_value]
        return filtered_tickets

    @staticmethod
    def filter_executor(tickets):
        filtered_tickets = []
        # Prompt user to select the filter option
        filter_value = int(input("Enter the number of your choice: 1. SERVICE_DEPT 2. LOGISTICS_DEPT 3. SALES_DEPT: ").strip().lower())
        while True:
            if filter_value == 1:
                # Filter tickets based on the selected option
                for ticket in tickets:
                    if ticket.executor == "SERVICE_DEPT":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == 2:
                for ticket in tickets:
                    if ticket.executor == "LOGISTICS_DEPT":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == 3:
                for ticket in tickets:
                    if ticket.executor == "SALES_DEPT":
                        filtered_tickets.append(ticket)
                break
            elif filter_value == "x":
                break
            else:
                print("Choose option 1. SERVICE_DEPT 2. LOGISTICS_DEPT 3. SALES_DEPT")
        return filtered_tickets
    
    @staticmethod
    def all_filters(tickets):
        while True:
            print("Select filter criteria:")
            print("1. Source")
            print("2. Status")
            print("3. Executor")
            print("4. Phone")
            print("X. Back to main menu")
            filter_choice = int(input("Enter the number of your choice: ").strip().lower())
            if filter_choice == 1:
                # Call the filter_source function
                filtered_tickets = Ticket.filter_source(tickets)
                # Print the filtered tickets
                Ticket.print_requests(filtered_tickets)
                break
            elif filter_choice == 2:
                # Call the filter_status function
                filtered_tickets = Ticket.filter_status(tickets)
                # Print the filtered tickets
                Ticket.print_requests(filtered_tickets)
                break
            elif filter_choice == 3:
                # Call the filter_executor function
                filtered_tickets = Ticket.filter_executor(tickets)
                # Print the filtered tickets
                Ticket.print_requests(filtered_tickets)
                break
            elif filter_choice == 4:
                # Call the filter_phone function
                filtered_tickets = Ticket.filter_phone(tickets)
                # Print the filtered tickets
                Ticket.print_requests(filtered_tickets)
                break
            elif filter_choice == "x":
                break
            else:
                print("Please choose a valid filter option")
        
    @staticmethod
    def process_the_lead(ticket):
        print("Process the lead and provide a solution for the ticket. Once the solution is provided, the ticket will be returned to the operator for review.")
        while True:
            solution = input("Enter the solution: ")
            if len(solution) >= 10:
                ticket.solution = solution
                ticket.status = "resolved"
                print("Solution added successfully. Ticket status updated to 'resolved'.")
                break
            else:
                print("Solution must be at least 10 characters long. Please try again.")
