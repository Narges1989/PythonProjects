from to_do import TODO


def guide3(items: list[str]) -> int:
    if len(items) == 0:
        return -1
    index_last_element = len(items) -1
    length_fistcountry = len(items[0])
    return index_last_element*length_fistcountry

