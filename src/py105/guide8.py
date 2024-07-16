from to_do import TODO


def guide8(hard_drive: dict[str, float]) -> int:
    result = 0
    programming_extensions = ['kt','py','yml','json','java']
    for file_name in hard_drive.keys():
        if file_name.split('.')[1] in programming_extensions:
            result += 1

    return result
