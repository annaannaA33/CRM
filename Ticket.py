import datetime
import uuid
import re
from RequestType import RequestType, TicketStatus, Source, Executor




class Ticket:
    def __init__(self, ticket_number, client_name, client_phone, request_type, source, description, executor, status="active", _solution = "", created_at=None):
        self.ticket_number = ticket_number
        self._client_name = client_name
        self._client_phone = client_phone
        self.request_type = request_type
        self.source = source
        self.description = description
        self.executor = executor
        self.status = status
        self._solution = ""
        self.created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def __str__(self):
        return f"\n #: {self.ticket_number}\n -----\n CUSTOMER INFORMATION: \n NAME: {self.client_name}\n PHONE: {self.client_phone}\n REQUEST TYPE: {self.request_type}\n SOURCE: {self.source}\n DESCRIPTION: {self.description}\n EXECUTOR: {self.executor}\n STATUS: {self.status}\n DATE AND TIME CREATED: {self.created_at}\n -----\n"



    def generate_ticket_number(self):
        self.ticket_number = uuid.uuid4()
        return self.ticket_number
    

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

    
    # solution
    @property
    # getter
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, value):
        # 
        if self.executor is not None:  # Проверка, что у заявки есть исполнитель
            self._solution = value
            print(f"Solution added by {self.executor}: {value}")
        else:
            print("Ticket has no assigned executor. Solution cannot be added.")


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
            "_solution": self._solution,
            "created_at": self.created_at,
        }
    

    @staticmethod
    def view_requests(list_of_tickets):
        if not list_of_tickets:
            print("No tickets available.")
        else:
            print("Tickets:")
            for ticket in list_of_tickets:
                print(f"Ticket Number: {ticket.ticket_number}")
                print(f"Client Name: {ticket.client_name}")
                print(f"Client Phone: {ticket.client_phone}")
                print(f"Request Type: {ticket.request_type}")
                print(f"Source: {ticket.source}")
                print(f"Description: {ticket.description}")
                print(f"Executor: {ticket.executor}")
                print(f"Status: {ticket.status}")
                print(f"Solution: {'Waiting for resolution' if not ticket.solution else ticket.solution}")
                print(f"Created At: {ticket.created_at}")
                print("-" * 30)

    def filter_tickets(list_of_tickets):
        # Function to normalize phone numbers by removing non-digit characters
        def normalize_phone_number(phone_number):
            return ''.join(c for c in phone_number if c.isdigit())

        # Menu for selecting filter criteria
        print("Select filter criteria:")
        print("0. Source")
        print("1. Status")
        print("2. Executor")
        print("3. Phone")
        filter_choice = int(input("Enter the number of your choice: "))

        # Dictionary to map choices to filter criteria and possible values
        filter_options = {
            0: ('source', ['CHAT', 'CALL']),
            1: ('status', ['active', 'in progress', 'resolved', 'closed']),
            2: ('executor', ['SERVICE_DEPT', 'LOGISTICS_DEPT', 'SALES_DEPT']),
            3: ('client_phone', None)
        }

        # Get the filter criteria and possible values based on the user's choice
        filter_criteria, possible_values = filter_options.get(filter_choice, (None, None))

        # If the user chose a criteria with predefined values, ask for the specific value
        if possible_values:
            print(f"Select {filter_criteria}:")
            for i, value in enumerate(possible_values):
                print(f"{i}. {value.capitalize()}")
            filter_value = possible_values[int(input("Enter the number of your choice: "))]
        else:
            # For phone, allow free entry but validate for digits only
            while True:
                filter_value = input("Enter the phone number: ").strip()
                if filter_value.isdigit():
                    break
                else:
                    print("Warning: The phone number must consist only of digits.")

        # Normalize the filter value for phone numbers
        if filter_criteria == 'client_phone':
            filter_value = normalize_phone_number(filter_value)

        # Filter the list of tickets based on the user's input
        filtered_tickets = [ticket for ticket in list_of_tickets if normalize_phone_number(getattr(ticket, filter_criteria, '')) == filter_value]

        return filtered_tickets
