# TODO("Delete this 'TODO' and create your function here")
def indecisive(month_number: int = 11) -> str:
    if month_number in range(3,6):
        season = 'Spring'
    elif month_number in range(6,9):
        season = 'Summer'
    elif month_number in range(9,12):
        season = 'Fall'
    elif month_number in [12,1,2]:
        season = 'Winter'
    else:
        return 'Error'

    return season
