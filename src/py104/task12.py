from to_do import TODO


def task12(guests: list[str], condition: str) -> list[str]:
    conditions = ['V','A','K']
    condition = condition[-1]
    guest_condition = []
    for guest in guests:
        condition1 = guest.split('-')[1]
        guest_condition.append(condition1)
    result = []
    for index,condition1 in enumerate(guest_condition):
        if guest_condition.count(condition)>1 and condition1 == condition:
            result.append(guests[index])
    return result

if __name__ == "__main__":
    # Change the situation to either "-V", "-A", or "-K" to test your code under different situation
    situation = "-A"
    guest_list = ['ZZStéphanie-A', 'ZZKù-A', 'ZZÖrjan-A', 'ZZPublicité-A', 'ZZEdmée-K', 'ZZMaëline-K', 'ZZNaéva-K', 'ZZUò-V', 'ZZCloé-V', 'ZZFèi-V', 'ZZMélissandre-V', 'ZZTáng-V', 'ZZLéana-V']

    # NOTE: Uncomment the code below when you are ready to test your answers
    print(
        f"The attendees with condition '{situation}' are {task12(guest_list, situation)}"
    )
