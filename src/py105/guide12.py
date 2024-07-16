from to_do import TODO


def guide12(hard_drive: dict[str, float]) -> float:
    programming_extension = ['kt', 'py', 'yml', 'json', 'java']
    result = 0
    for file_name,file_size in hard_drive.items():
        extension = file_name.split('.')[1]
        if extension not in programming_extension:
            result += file_size
    return result
