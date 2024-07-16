from to_do import TODO


def task6(base1: float, base2: float, height: float) -> float:
    result = (base1+base2)*height/2
    return result

if __name__ == '__main__':
    # base1=10, base2=20, height= 1,output: 15
    print(task6(10,20,1))

    # base1=10, base2=10, height= 2,output: 20
    print(task6(10,10,2))
