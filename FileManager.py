from enum import Enum

class RequestType(Enum):
    SERVICE = 'service'
    PURCHASE = 'purchase'
    LOGISTICS = 'logistics'

class Source(Enum):
    CHAT = 'chat'
    CALL = 'call'

class Executor(Enum):
    SERVICE_DEPT = 'service department'
    LOGISTICS_DEPT = 'logistics department'
    SALES_DEPT = 'sales department'