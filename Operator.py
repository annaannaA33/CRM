from Ticket import Ticket
import re
from datetime import datetime
from RequestType import RequestType, TicketStatus, Source, Executor

class Operator(Ticket):
    def __init__(self):
        
        self.tickets = []

    def validate_name(self, value):
        if len(value) >= 3 and value.isalpha():
            return value
        else:
            raise ValueError("Invalid client name. Must be at least 3 characters and contain only letters.")

    def validate_phone(self, value):
        if re.match(r'^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,9}$', value):
            return value
        else:
            raise ValueError("Invalid phone number.")

    def validate_request_type(self, value):
        try:
            return RequestType(int(value)).name
        except ValueError:
            raise ValueError("Invalid request type.")

    def validate_source(self, value):
        try:
            return Source(int(value)).name
        except ValueError:
            raise ValueError("Invalid source.")

    def validate_executor(self, value):
        try:
            return Executor(int(value)).name
        except ValueError:
            raise ValueError("Invalid executor.")
    
    def validate_description(self, value):
        if len(value) >= 5:
            return value
        else:
            raise ValueError("Description must be at least 5 characters long.")
      

    def create_request(self):
        # Define a dictionary mapping parameter names to their validation functions
        validations = {
            'client_name': self.validate_name,
            'client_phone': self.validate_phone,
            'request_type': self.validate_request_type,
            'source': self.validate_source,
            'executor': self.validate_executor,
            'description': self.validate_description,
        }

        # Initialize a dictionary to store entered values
        ticket_data = {}

        # Helper function to prompt for and validate a single parameter
        def prompt_and_validate(param_name, prompt_text):
            while True:
                try:
                    value = validations[param_name](input(prompt_text))
                    ticket_data[param_name] = value
                    return value
                except ValueError as e:
                    print(f"Error: {e}")

        # Prompt for and validate each parameter
        ticket_data['client_name'] = prompt_and_validate('client_name', "Enter the client name: ")
        ticket_data['client_phone'] = prompt_and_validate('client_phone', "Enter the client phone: ")
        ticket_data['request_type'] = prompt_and_validate('request_type', "Enter the request type (0: SERVICE, 1: PURCHASE, 2: LOGISTICS): ")
        ticket_data['source'] = prompt_and_validate('source', "Enter the source (0: CHAT, 1: CALL): ")
        ticket_data['executor'] = prompt_and_validate('executor', "Enter the executor (0: SERVICE_DEPT, 1: LOGISTICS_DEPT, 2: SALES_DEPT): ")
        ticket_data['description'] = prompt_and_validate("description", "Enter the description: ")
        

        # Create the new ticket using the validated information
        new_ticket = Ticket(
            ticket_number=Ticket.generate_ticket_number(self),
            **ticket_data # Unpack the dictionary to pass keyword arguments to the Ticket constructor
        )
        return new_ticket


    def close_request(self, ticket):
        if ticket.status == "Resolved":
            ticket.status = "Closed"
            print(f"Ticket {ticket.ticket_number} closed successfully.")
        else:
            print("Cannot close the ticket. Please resolve it first.")


    def redirect_request(self, request, new_executor):
        # Implement logic to redirect a request to a new executor
        pass

    

    def process_request(self, request):
        # Implement logic to process a request
        pass

    def send_reminder(self, request):
        pass

