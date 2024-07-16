from to_do import TODO


def guide5(classroom: list[float]) -> float:
    assert(len(classroom)>0)
    Sum = 0
    for grade in classroom:
        Sum += grade
    return Sum/len(classroom)

