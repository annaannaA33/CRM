from Ticket import Ticket


class Operator:
    def __init__(self):
        self.tickets = []

    def create_request(self, ticket_number, client_name, client_phone, request_type, source, executor, description):
        new_ticket = Ticket(ticket_number, client_name, client_phone, request_type, source, executor, description)
        self.tickets.append(new_ticket)
        print(f"New ticket created: {new_ticket}")
        return new_ticket


    def close_request(self, request):
        # Implement logic to close a request
        pass
    
    def close_request(self, ticket):
        if ticket.status == "Resolved":
            ticket.status = "Closed"
            print(f"Ticket {ticket.ticket_number} closed successfully.")
        else:
            print("Cannot close the ticket. Please resolve it first.")




    def redirect_request(self, request, new_executor):
        # Implement logic to redirect a request to a new executor
        pass

    def view_requests(self):
        # Implement logic to view requests
        pass

    def process_request(self, request):
        # Implement logic to process a request
        pass

    def send_reminder(self, request):
        pass

    '''
    

    def redirect_request(self, ticket, new_executor):
        if ticket.status == "Open":
            ticket.executor = new_executor
            print(f"Ticket {ticket.ticket_number} redirected to {new_executor}.")
        else:
            print("Cannot redirect a closed or resolved ticket.")

    def view_requests(self, status=None):
        if status:
            filtered_tickets = [t for t in self.tickets if t.status == status]
        else:
            filtered_tickets = self.tickets

        for ticket in filtered_tickets:
            print(ticket)

    def process_request(self, ticket):
        if ticket.status == "Open":
            ticket.status = "In Progress"
            print(f"Ticket {ticket.ticket_number} is now in progress.")
        else:
            print("Cannot process a closed or resolved ticket.")

    def send_reminder(self, ticket):
        # Implement logic to send a reminder
        pass
    '''