from Ticket import Ticket

class Salesperson(Ticket):
    def __init__(self):
        self.tickets = []  # List to hold tickets assigned to the salesperson



    def find_ticket(self, ticket_number, tickets):
        # Вызов метода find_ticket родительского класса Ticket
        ticket = super().find_ticket(ticket_number, tickets)
        if ticket and ticket.executor == "SALES_DEPT":
            return ticket
        else:
            return None
        
    def process_the_lead(ticket):
        print("Обработайте заявку, после внесите решение по заявке. После внесения решения заявка вернется к оператору на проверку.")
        
        ticket._solution = input("Введите решение: ")
        return ticket._solution


