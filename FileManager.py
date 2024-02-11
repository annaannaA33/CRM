import os
import csv
from Ticket import Ticket



class FileManager:
    def __init__(self):
        self.CLIENTS_FILE = "clients_file.csv"

    def save_ticket(self, some_ticket):
        header = [
            "ticket_number",
            "client_name",
            "client_phone",
            "request_type",
            "source",
            "description",
            "executor",
            "status",
            "solution",
            "created_at",
        ]
        if (
            not os.path.isfile(self.CLIENTS_FILE)
            or os.path.getsize(self.CLIENTS_FILE) == 0
        ):
            with open(self.CLIENTS_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
        with open(self.CLIENTS_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "ticket_number",
                    "client_name",
                    "client_phone",
                    "request_type",
                    "source",
                    "description",
                    "executor",
                    "status",
                    "solution",
                    "created_at",
                ],
            )
            writer.writerow(some_ticket.as_dict())

    def load_tickets_from_file(self):
        list_of_tickets = []
        try:
            with open(self.CLIENTS_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ticket = Ticket(
                        ticket_number=row['ticket_number'],
                        client_name=row['client_name'],
                        client_phone=row['client_phone'],
                        request_type=row['request_type'],
                        source=row['source'],
                        description=row['description'],
                        executor=row['executor'],
                        status=row['status'],
                        solution=row['solution'],
                        created_at=row['created_at']
                    )
                    list_of_tickets.append(ticket)
                    # Debugging output
                    #print(f"Added ticket: {ticket}") 

        except FileNotFoundError:
            print("File not found. No tickets loaded.")
        return list_of_tickets

    
    def save_tickets(self, tickets):
        header = [
            "ticket_number",
            "client_name",
            "client_phone",
            "request_type",
            "source",
            "description",
            "executor",
            "status",
            "solution",
            "created_at",
        ]
        with open(self.CLIENTS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for ticket in tickets:
                writer.writerow(ticket.as_dict())

