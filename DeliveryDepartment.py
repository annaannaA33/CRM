from Ticket import Ticket


class DeliveryDepartment(Ticket):
    def __init__(self):
        self.tickets = []

    def find_ticket(self, ticket_number, tickets):
        ticket = super().find_ticket(ticket_number, tickets)
        if ticket and ticket.executor == "LOGISTICS_DEPT":
            return ticket
        else:
            return None

    def process_logistics_request(self, ticket):
        print(
            "PROCESS THE LOGISTICS REQUEST. ONCE THE SOLUTION IS PROVIDED, THE TICKET WILL BE RETURNED TO THE OPERATOR FOR REVIEW."
        )

        solution = input("ENTER THE SOLUTION: ")
        if len(solution) > 5:
            ticket.solution = solution
            ticket.status = "resolved"
            print("SOLUTION SAVED, STATUS RESOLVED")
        else:
            print("SOLUTION NOT SAVED")

        ticket.print_ticket_details(ticket)
        return ticket.solution
