import pytest
from Ticket import Ticket
from RequestType import Executor
from Operator import Operator
from FileManager import FileManager

def main():
    print(sample_ticket.ticket)

@pytest.fixture
def sample_ticket():
    return Ticket(
        ticket_number="123456",
        client_name="John Doe",
        client_phone="+1234567890",
        request_type="Service",
        source="Call",
        description="Test description",
        executor=Executor.SERVICE_DEPT,
        solution="Test solution",
        created_at="2024-02-07 12:00",
        status="Active"
    )
