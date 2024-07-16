from to_do import TODO


def task13(sells: list[int]) -> str:
    Max = sells[0]
    week_day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    Week_day_max = week_day[0]
    for index,sell in enumerate(sells):
        if sell>Max:
            Max = sell
            Week_day_max = week_day[index]
    return Week_day_max
