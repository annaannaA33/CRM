from enum import Enum

class RequestType(Enum):
    SERVICE = 0
    PURCHASE = 1
    LOGISTICS = 2


class Source(Enum):
    CHAT = 0
    CALL = 1


class Executor(Enum):
    SERVICE_DEPT = 0
    LOGISTICS_DEPT = 1
    SALES_DEPT = 2

class TicketStatus(Enum):
    ACTIVE = "Active"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"