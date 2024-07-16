from to_do import TODO


def guide8(items: list[str]) -> list[str]:
    Scandinavian_countries = ['denmark','norway','sweden','finland','iceland','faroe islands','greenland','åland']
    return [item for item in items if item.lower() in Scandinavian_countries]
