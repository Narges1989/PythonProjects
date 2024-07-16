from to_do import TODO


def guide1(country: str) -> bool:
    if ((country.lower()) == 'sweden'):
        return True
    else:
        return False

if __name__== "__main__":
    # sweden, Sweden, SWEDEN , output = True
    print(guide1('SWeden'))

    # panama,PANAma, output = False
    print(guide1('IRan'))

    # panama,PANAma, output = False
    print(guide1('Denmark'))

    # panama,PANAma, output = False
    print(guide1('PANAma'))