from to_do import TODO


def guide5(capital: str) -> bool:
    return capital.lower() == 'stockholm'


if __name__ == "__main__":
    # capital = stockholm, output = True
    print(guide5('stockholm'))

    # capital = StockHolm, output = True
    print(guide5('sTockHolm'))

    # capital = Oslo , output = False
    print(guide5('Oslo'))
