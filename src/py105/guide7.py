from to_do import TODO


def guide7(classroom: dict[str, float]) -> int:
    result = 0
    for student_name in classroom.keys():
        last_characters = student_name[-4:]
        if last_characters == 'sson':
            result += 1
    return result

if __name__== "__main__":
    print(guide7({"Ann Johannsson" : 10.0, "Pat Ericsson" : 9.5, "Pat Lark" : 9.0}))