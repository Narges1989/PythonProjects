from to_do import TODO


def task14(sells: list[int]) -> str:
    Min = sells[0]
    week_day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    Week_day_min = week_day[0]
    for index,sell in enumerate(sells):
        if sell<Min:
            Min = sell
            Week_day_min = week_day[index]
    return Week_day_min