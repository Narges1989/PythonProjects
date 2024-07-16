from to_do import TODO


def guide6(firstname: str, lastname: str) -> str:
    result = 'Hello' + ' ' + firstname +  ' ' + lastname+ '. Welcome to programming'
    return result


if __name__== '__main__':
    print(guide6('Humberto', 'Linero'))
    print(guide6('Narges', 'Kurkani'))

