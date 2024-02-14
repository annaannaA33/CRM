import os
import csv
from Ticket import Ticket
from User import User

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
            with open(
                self.CLIENTS_FILE, mode="r", newline="", encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ticket = Ticket(
                        ticket_number=row["ticket_number"],
                        client_name=row["client_name"],
                        client_phone=row["client_phone"],
                        request_type=row["request_type"],
                        source=row["source"],
                        description=row["description"],
                        executor=row["executor"],
                        status=row["status"],
                        solution=row["solution"],
                        created_at=row["created_at"],
                    )
                    list_of_tickets.append(ticket)
                    # Debugging output
                    # print(f"Added ticket: {ticket}")

        except FileNotFoundError:
            print("FILE NOT FOUND. NO TICKETS LOADED")
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

    def save_new_user(self, user):
        hashed_password = user.hash_password(user.password)
        with open('users.csv', mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([user.username, hashed_password, user.role])
        print("New user successfully registered.")

   
    def save_all_users(self, users):
        with open('users.csv', 'w', newline='') as csvfile:
            fieldnames = ['username', 'password', 'role']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for user in users:
                writer.writerow({
                    'username': user.username,
                    'password': user.password,
                    'role': user.role
                })
        print("User list successfully updated.")

    def load_users(self):
        users = []
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                username, password, role = row
                user = User(username, password, role)
                users.append(user)
        return users
    
    def init_csv_file(self):
        # Create a function to initialize the CSV file with headers if it doesn't exist
        filename = 'users.csv'
        headers = ['username', 'password', 'role']

        # Check if the file exists
        if not os.path.exists(filename):
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()