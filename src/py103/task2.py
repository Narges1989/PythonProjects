from to_do import TODO

def task2(number: int) -> bool:
    if number<= 1:
        result = False
    elif number == 2:
        result = True
    else:
        result = True
        for num in range(2,abs(number)):
            if number%num == 0:
                result = False
    return result

if __name__ == '__main__':
    #Input = 29, output = True
    print(task2(29))

    #Input = 2, output = True
    print(task2(2))

    #Input = 8, output = False
    print(task2(8))