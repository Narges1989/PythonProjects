from to_do import TODO


def guide7(country: str, capital: str) -> str:
    result = f'The capital of {country} is {capital}'

    return result

if __name__== '__main__':
    print(guide7('Sweden', 'Stockholm'))
    print(guide7('Iran', 'Tehran'))