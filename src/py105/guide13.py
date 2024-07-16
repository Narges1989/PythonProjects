from to_do import TODO


def guide13(hard_drive: dict[str, float], corrupted: str) -> dict[str, float]:
    # if corrupted.lower() in hard_drive.keys():
    #     del hard_drive[corrupted]
    # return hard_drive

    # using filter
    result = filter(lambda item: item[0] != corrupted, hard_drive.items())
    return dict(result)