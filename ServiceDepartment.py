from Ticket import Ticket


class ServiceDepartment(Ticket):
    def __init__(self):
        self.tickets = []

    def find_ticket(self, ticket_number, tickets):
        ticket = super().find_ticket(ticket_number, tickets)
        if ticket and ticket.executor == "SERVICE_DEPT":
            return ticket
        else:
            return None

    def process_service_request(self, ticket):
        print(
            "PROCESS THE REQUEST, THEN ENTER THE SOLUTION FOR THE TICKET. AFTER ENTERING THE SOLUTION, THE TICKET WILL BE RETURNED TO THE OPERATOR FOR REVIEW"
        )
        ticket.status = "In Progress"
        solution = input("ENTER THE SOLUTION: ")
        if len(solution) > 5:
            ticket.solution = solution
            ticket.status = "resolved"
            print("SOLUTION SAVED, STATUS RESPONDED")
        else:
            print("SOLUTION NOT ENTERED")
        ticket.print_ticket_details(ticket)
        return ticket.solution
