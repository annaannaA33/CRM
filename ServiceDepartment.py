from Ticket import Ticket

class ServiceDepartment(Ticket):
    def __init__(self):
        self.tickets = []  # Список тикетов, назначенных отделу обслуживания

    def find_ticket(self, ticket_number, tickets):
        # Вызов метода find_ticket родительского класса Ticket
        ticket = super().find_ticket(ticket_number, tickets)
        if ticket and ticket.executor == "SERVICE_DEPT":
            return ticket
        else:
            return None

    def process_service_request(self, ticket):
        print("Обработайте заявку обслуживания. После внесения решения заявка вернется к оператору на проверку.")
        
        solution = input("Введите решение: ")
        if len(solution) >   5:
            ticket.solution = solution
            ticket.status = "resolved"
            print("Решение сохранено, статус отвечено.")
        else:
            print("Решение не внесено.")
        ticket.print_ticket_details(ticket)  # Печатаем тикет полностью
        return ticket.solution
