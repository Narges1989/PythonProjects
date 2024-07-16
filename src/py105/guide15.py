from to_do import TODO


def guide15(birthdays: dict[str, int]) -> dict[str, str]:
    for name,month in birthdays.items():
        if month in range(3,6):
            birthdays[name] = 'Spring'
        elif month in range(6,9):
            birthdays[name] = 'Summer'
        elif month in range(9,12):
            birthdays[name] = 'Fall'
        else:
            birthdays[name] = 'Winter'
    return birthdays