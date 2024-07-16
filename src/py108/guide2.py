from to_do import TODO

from enum import Enum
class Pizza (Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    FAMILY = 4
def guide2(attendees: int) -> Pizza:
    if attendees < 4:
        return Pizza.SMALL
    elif attendees in range(4,7):
        return Pizza.MEDIUM
    elif attendees in range (7,10):
        return Pizza.LARGE
    else:
        return Pizza.FAMILY
