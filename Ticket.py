import datetime

class Ticket:
    def __init__(self, ticket_number, client_name, client_phone, request_type, source, description, executor, status="active"):
        self.ticket_number = ticket_number
        self.client_name = client_name
        self.client_phone = client_phone
        self.request_type = request_type
        self.source = source
        self.description = description
        self.executor = executor
        self.status = status
        self._solution = ""
        self.created_at = datetime.now()  # 


    def __str__(self):
        return f"{self.ticket_number}\n {self.client_name}\n {self.client_phone}\n {self.request_type}\n {self.source}\n {self.description}\n {self.executor}\n {self.status}\n "

    @property
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


    
