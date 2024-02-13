from Ticket import Ticket


class Salesperson(Ticket):
    def __init__(self):
        self.tickets = []  # List to hold tickets assigned to the salesperson

    def find_ticket(self, ticket_number, tickets):
        # Calling the find_ticket method of the parent class Ticket
        ticket = super().find_ticket(ticket_number, tickets)
        if ticket and ticket.executor == "SALES_DEPT":
            return ticket
        else:
            return None

    def process_the_lead(self, ticket):
        print(
            "PROCESS THE REQUEST, THEN ENTER THE SOLUTION FOR THE TICKET. AFTER ENTERING THE SOLUTION, THE TICKET WILL BE RETURNED TO THE OPERATOR FOR REVIEW"
        )

        solution = input("ENTER THE SOLUTION: ")
        if len(solution) > 5:
            ticket.solution = solution
            ticket.status = "resolved"
            print("SOLUTION SAVED, STATUS RESPONDED")
        else:
            print("SOLUTION NOT ENTERED")
        ticket.print_ticket_details(ticket)
        return ticket.solution
