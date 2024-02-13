### Setup and Usage

1. Clone this repository
2. Rename `rename_to.env` to `.env`
3. Update **EMAIL_ADDRESS** and **EMAIL_PASSWORD** values in `.env`. In order to get the _Gmail_ authentication work, you need to create a password for the application [here](https://myaccount.google.com/apppasswords)
4. Install:
pip install secure-smtplib 
pip install requests
pip install python-dotenv 
pip install questionary



5. Run the program using: `python main.py


Description
Imagine there's an online store selling various products. It's a CRM system designed to store and manage customer requests. Requests can come from two sources: chat and phone calls. Clients can reach out to the support department for service inquiries, assistance with purchases, or delivery-related queries. All requests are received by an operator who directs them to the appropriate department for processing.

There are several roles with different processing capabilities:

Operator Role:

Accept a request, fill in all fields, and save the request.
View the entire list of requests.
Modify a request.
Send a reminder to the executor regarding a request.
Currently, it's assumed that there's one operator in each department. The operator can filter requests by the source of the inquiry, client's phone number, responsible party, or processing stage.

Sales Department Employee Role:

View all requests directed to the sales department.
Process a request and make a decision.
Find a request by its number.
Service Department Employee Role:

View all requests directed to the service department.
Process a request and make a decision.
Find a request by its number.
Take ownership of a request.
Logistics Department Employee Role:

View all requests directed to the logistics department.
Process a request and make a decision.
Find a request by its number.
Upon starting the program, the user is prompted to select a role, and then the functionality corresponding to the chosen role is displayed.

For data storage, CSV files are used, and for sending data, environment variables are utilized.