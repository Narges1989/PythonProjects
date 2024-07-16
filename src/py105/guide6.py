from to_do import TODO


def guide6(birthdays: dict[str, int], letter: str, month: int) -> int:
    result = 0
    for name,value in birthdays.items():
        if name[0].lower() == letter.lower() and value == month:
            result += 1

    return result