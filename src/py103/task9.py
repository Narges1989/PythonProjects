from to_do import TODO


def task9(temperature: str) -> str:
    temp = temperature[:-1]
    if temperature[-1].lower() == 'c':
        result = 9*int(temp) /5 + 32
        result = str(int(result)) + 'F'
    else:
        result = 5 * (int(temp)-32) / 9
        result = str(int(result)) + 'C'
    return result

if __name__ == '__main__':
    #temperature: -30c, output = -22F
    print(task9('-30c'))

    #temperature: 50f, output = 10C
    print(task9('50f'))


