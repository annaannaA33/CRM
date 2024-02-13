import pytest
from Ticket import Ticket

# Создание тестовых тикетов
ticket1 = Ticket(ticket_number="123456", client_name="John", client_phone="+1234567890", request_type="Service", source="Call", description="Test description", executor="Service Dept", solution="Test solution", created_at="2024-02-07 12:00", status="Active")
ticket2 = Ticket(ticket_number="789012", client_name="Alice", client_phone="+9876543210", request_type="Purchase", source="Chat", description="Another test description", executor="Logistics Dept", solution="", created_at="2024-02-08 12:00", status="Resolved")
ticket3 = Ticket(ticket_number="345678", client_name="Bob", client_phone="+2468135790", request_type="Service", source="Email", description="Yet another test description", executor="Sales Dept", solution="", created_at="2024-02-09 12:00", status="Active")
ticket4 = Ticket(ticket_number="901234", client_name="Eve", client_phone="+1357924680", request_type="Logistics", source="Call", description="One more test description", executor="Logistics Dept", solution="", created_at="2024-02-10 12:00", status="Closed")
filter_value=1 # active
tickets = [ticket1, ticket2, ticket3, ticket4]

def test_find_ticket():

    assert Ticket.find_ticket("123456", tickets) == ticket1
    assert Ticket.find_ticket("789012", tickets) == ticket2
    assert Ticket.find_ticket("999999", tickets) is None
    assert Ticket.find_ticket("", tickets) is None
    assert Ticket.find_ticket("   ", tickets) is None
    assert Ticket.find_ticket("abc", tickets) is None
    assert Ticket.find_ticket("-123", tickets) is None

