from to_do import TODO


def guide16(hard_drive: dict[str, float]) -> dict[str, float]:
    # for filename, filesize in hard_drive.items():
    #     #hard_drive[filename] = filesize * 0.0009765625
    #     hard_drive.update({filename:filesize * 0.0009765625})
    # return hard_drive

    # dictionary comprehension
    #return {filename:filesize * 0.0009765625 for filename,filesize in hard_drive.items()}

    # transform function
    result = map(lambda item:(item[0],item[1]*0.0009765625),hard_drive.items())
    return dict(result)
