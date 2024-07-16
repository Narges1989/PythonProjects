from to_do import TODO


def task8(items: list[int]) -> list[int]:
    items = list(set(items))
    Max = items[0]
    result = []
    iteration = 1
    while (iteration<4):
        for number in items:
            if number>Max:
                Max = number
        if Max in items:
            items.remove(Max)
            result.append(Max)
        if items != []:
            Max = items[0]
        iteration += 1

    return result[::-1]

if __name__== "__main__":
    # [8, 9, 7, 10] --> [9, 10, 60]
    print(task8([1,1,1,1]))