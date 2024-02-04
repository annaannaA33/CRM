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
        self.created_at = created_at or datetime.datetime.now() # Use datetime.datetime.now()


    def __str__(self):
        return f"{self.ticket_number}\n {self.client_name}\n {self.client_phone}\n {self.request_type}\n {self.source}\n {self.description}\n {self.executor}\n {self.status}\n "



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

    def __str__ (self):
        return f""
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
    def get_request_type_name(ticket_type):
        return RequestType(ticket_type).name

    @staticmethod
    def get_ticket_status_name(ticket_status):
        return TicketStatus(ticket_status).name

    @staticmethod
    def filter_tickets(tickets, type=None, status=None, executor=None, source=None):
        filtered_tickets = tickets

        if type is not None:
            type_name = Ticket.get_ticket_type_name(type)
            filtered_tickets = [t for t in filtered_tickets if t.request_type == type_name]

        if status is not None:
            status_name = Ticket.get_ticket_status_name(status)
            filtered_tickets = [t for t in filtered_tickets if t.status == status_name]

        if executor is not None:
            filtered_tickets = [t for t in filtered_tickets if t.executor == executor]

        if source is not None:
            filtered_tickets = [t for t in filtered_tickets if t.source == source]

        return filtered_tickets

    @staticmethod
    def print_tickets(tickets):
        if not tickets:
            print("No tickets available.")
        else:
            print("Tickets:")
            for ticket in tickets:
                print(ticket)
