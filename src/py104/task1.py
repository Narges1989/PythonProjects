from to_do import TODO
import random

def task1(items: list[str]) -> str:
    if len(items) == 0:
        return ''
    return random.choice(items)
