import pytest
from Ticket import Ticket
from RequestType import Executor
from Operator import Operator
from FileManager import FileManager


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

def test_create_ticket(sample_ticket):
    assert sample_ticket.ticket_number == "123456"
    assert sample_ticket.client_name == "John Doe"
    assert sample_ticket.client_phone == "+1234567890"
    assert sample_ticket.request_type == "Service"
    assert sample_ticket.source == "Call"
    assert sample_ticket.description == "Test description"
    assert sample_ticket.executor == Executor.SERVICE_DEPT
    assert sample_ticket.solution == "Test solution"
    assert sample_ticket.created_at == "2024-02-07 12:00"
    assert sample_ticket.status == "Active"

# checking validators:
def test_validate_name():
    operator = Operator()
    assert operator.validate_name("John") == "John"
    try:
        operator.validate_name("")
        assert False, "Empty name should raise ValueError"
    except ValueError:
        pass
    try:
        operator.validate_name("Ab")
        assert False, "Short name should raise ValueError"
    except ValueError:
        pass
    try:
        operator.validate_name("123")
        assert False, "Name with digits should raise ValueError"
    except ValueError:
        pass

def test_validate_phone():
    operator = Operator()
    assert operator.validate_phone("+1234567890") == "+1234567890"
    try:
        operator.validate_phone("12a4")
        assert False, "Invalid phone number should raise ValueError"
    except ValueError:
        pass
    try:
        operator.validate_phone("+1234567811111190123114")
        assert False, "Invalid phone number should raise ValueError"
    except ValueError:
        pass
    try:
        operator.validate_phone("+1234")
        assert False, "Invalid phone number should raise ValueError"
    except ValueError:
        pass
    try:
        operator.validate_phone("")
        assert False, "Invalid phone number should raise ValueError"
    except ValueError:
        pass

def test_validate_request_type():
    operator = Operator()
    assert operator.validate_request_type("0") == "SERVICE"
    try:
        operator.validate_request_type("3")
        assert False, "Invalid request type should raise ValueError"
    except ValueError:
        pass

def test_validate_source():
    operator = Operator()
    assert operator.validate_source("0") == "CHAT"
    try:
        operator.validate_source("2")
        assert False, "Invalid source should raise ValueError"
    except ValueError:
        pass


def test_validate_executor():
    operator = Operator()
    assert operator.validate_executor("0") == "SERVICE_DEPT"
    try:
        operator.validate_executor("3")
        assert False, "Invalid executor should raise ValueError"
    except ValueError:
        pass


def test_validate_description():
    operator = Operator()
    assert operator.validate_description("Test description") == "Test description"
    try:
        operator.validate_description("1234")
        assert False, "Invalid description should raise ValueError"
    except ValueError:
        pass