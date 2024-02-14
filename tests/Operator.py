from Ticket import Ticket
import re
from datetime import datetime
from RequestType import RequestType, TicketStatus, Source, Executor
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_data import executor_email, sender_email_data, sender_password_data


class Operator():
    def __init__(self):
        self.tickets = []
    def validate_name(self, value):
        if len(value) >= 3 and value.isalpha():
            return value
        else:
            raise ValueError("INVALID CLIENT NAME. MUST BE AT LEAST 3 CHARACTERS AND CONTAIN ONLY LETTERS")

    def validate_phone(self, value):
        if re.match(r'^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,9}$', value):
            return value
        else:
            raise ValueError("INVALID PHONE NUMBER")

    def validate_request_type(self, value):
        try:
            return RequestType(int(value)).name
        except ValueError:
            raise ValueError("INVALID REQUEST TYPE")

    def validate_source(self, value):
        try:
            return Source(int(value)).name
        except ValueError:
            raise ValueError("INVALID SOURCE")

    def validate_executor(self, value):
        try:
            return Executor(int(value)).name
        except ValueError:
            raise ValueError("INVALID EXECUTOR")
    
    def validate_description(self, value):
        if len(value) >= 5:
            return value
        else:
            raise ValueError("DESCRIPTION MUST BE AT LEAST 5 CHARACTERS LONG")
      

    def create_request(self):
        # Collect ticket data through user input and validation
        ticket_data = self.collect_ticket_data()

        # If ticket data collection was successful, proceed to create the ticket
        if ticket_data:
            # Create a new Ticket instance
            new_ticket = self.create_ticket(ticket_data)
            return new_ticket
        else:
            print("FAILED TO COLLECT TICKET DATA. NO TICKET CREATED")
            return None

    def collect_ticket_data(self):
        """Collect and validate ticket data from the user."""
        ticket_data = {}
        fields = [
            ('client_name', "Enter the client name: ", self.validate_name),
            ('client_phone', "Enter the client phone: ", self.validate_phone),
            ('request_type', "Enter the request type (0: SERVICE,  1: PURCHASE,  2: LOGISTICS): ", self.validate_request_type),
            ('source', "Enter the source (0: CHAT,  1: CALL): ", self.validate_source),
            ('executor', "Enter the executor (0: SERVICE_DEPT,  1: LOGISTICS_DEPT,  2: SALES_DEPT): ", self.validate_executor),
            ('description', "Enter the description: ", self.validate_description),
        ]

        for field_name, prompt_text, validation_func in fields:
            while True:
                try:
                    value = validation_func(input(prompt_text))
                    ticket_data[field_name] = value
                    break
                except ValueError as e:
                    print(f"Error: {e}")

        return ticket_data

    def create_ticket(self, ticket_data):
        """Create a new Ticket instance with the collected data."""
        # Create a new Ticket instance with a placeholder for created_at
        new_ticket = Ticket(
            ticket_number=None,  # Placeholder for ticket_number
            client_name=ticket_data['client_name'],
            client_phone=ticket_data['client_phone'],
            request_type=ticket_data['request_type'],
            source=ticket_data['source'],
            description=ticket_data['description'],
            executor=ticket_data['executor'],
            solution="",  # Assuming no initial solution
            created_at=None,  # Placeholder for created_at
            status="active"  # Default status
        )

        # Set the ticket_number and created_at attributes
        new_ticket.ticket_number = new_ticket.generate_ticket_number()
        new_ticket.created_at = new_ticket.get_created_at()

        return new_ticket


    @staticmethod
    def redirect_request(ticket):
        while True:
            new_executor_number = int(input("SELECT THE NEW EXECUTOR: \n1. SERVICE_DEPT\n 2. LOGISTICS_DEPT\n 3. SALES_DEPT\n").strip())
            if new_executor_number == 1:
                new_executor = "SERVICE_DEPT"
            elif new_executor_number == 2:
                new_executor = "LOGISTICS_DEPT"
            elif new_executor_number == 3:
                new_executor = "SALES_DEPT"
            elif new_executor_number == 0:
                break
            else:
                print("PLEASE ENTER ONE OF THE PROVIDED NUMBERS OR 0 TO GO BACK")
                continue

            if ticket.executor != new_executor:
                ticket.executor = new_executor
                print(f"NEW EXECUTOR FOR TICKET {ticket.ticket_number} SET SUCCESSFULLY: {new_executor}")
            else:
                print("YOU ARE ASSIGNING THE SAME EXECUTOR")
            break

    @staticmethod
    def change_request_status(ticket):
        while True:
            new_status_number = int(input("SELECT THE NEW STATUS:\n0. TO GO BACK \n1. ACTIVE\n 2. IN PROGRESS\n 3. RESOLVED\n 4. CLOSED\n").strip())
            if new_status_number == 1:
                new_status = "active"
            elif new_status_number == 2:
                new_status = "in progress"
            elif new_status_number == 3:
                new_status = "resolved"
            elif new_status_number == 4:
                new_status = "closed"
            elif new_status_number == 0:
                break
            else:
                print("PLEASE ENTER ONE OF THE PROVIDED NUMBERS OR 0 TO GO BACK")
                continue

            if ticket.status != new_status:
                ticket.status = new_status
                print(f"NEW STATUS FOR TICKET {ticket.ticket_number} SET SUCCESSFULLY: {new_status}")
            else:
                print("YOU ARE ASSIGNING THE SAME STATUS")
            break

    def close_ticket(ticket):
        if ticket.status == "resolved":
            ticket.status = "closed"
            print(f"TICKET {ticket.ticket_number} CLOSED SUCCESSFULLY.")
        else:
            print("CANNOT CLOSE THE TICKET. PLEASE RESOLVE IT FIRST")

    def send_reminder(self, ticket):
        # Determine the recipient's email address based on the executor
        recipient_email = ""
        if ticket.executor == 'SERVICE_DEPT':
            recipient_email = executor_email
        elif ticket.executor in ['LOGISTICS_DEPT', 'SALES_DEPT']:
            # For example, I use the same address here, but you can add other addresses
            recipient_email = executor_email

        # Sender's email address and password
        sender_email = sender_email_data
        sender_password = sender_password_data

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = "REMINDER: YOUR RESPONSE IS AWAITED FOR THIS REQUEST"

        # Email message content
        message_body = f"TICKET:\n{ticket}\n"
        message.attach(MIMEText(message_body, 'plain'))

        # # Sending the email
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            print("REMINDER SUCCESSFULLY SENT")
            server.quit()
        except Exception as e:
            print(f"ERROR SENDING REMINDER {str(e)}")

    def print_operator_menu():

        print("WELCOME TO OPERATOR MODE. PLEASE SELECT FUNCTION:")
        print("1. CREATE A NEW REQUEST")
        print("2. VIEW REQUESTS")
        print("3 TO USE FILTRES")
        print("4 WORK WITH A TICKET")
        print("0 RETURN TO ROLE SELECTION MENU")

