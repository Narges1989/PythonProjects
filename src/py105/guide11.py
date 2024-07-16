from to_do import TODO


def guide11(classroom: dict[str, float]) -> float:
    if classroom == {}:
        return 0

    all_grade = 0
    for grade in classroom.values():
        all_grade += grade
    result = all_grade/len(classroom)
    return result


if __name__ == "__main__":
    print(guide11({"Far" : 5.0, "Bob" : 4.5, "Ben" : 5.0}))