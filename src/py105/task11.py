from to_do import TODO


def task11(mapa: dict[int, str], prospect: int) -> bool:
    keys = mapa.keys()
    if prospect in keys:
        return True
    else:
        return False