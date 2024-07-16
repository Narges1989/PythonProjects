from to_do import TODO
import statistics

def task9(grades: dict[str, list[float]]) -> float:
    if len(grades) == 0:
        return 0
    '''sum_class = 0
    for key, value in grades.items():
        sum_student = 0
        for numb in value:
            sum_student += numb
        sum_class += sum_student/len(value)

    return  sum_class/len(grades)'''

    # solution 2
    '''sum_class = 0
    for key, value in grades.items():
        sum_class += sum(value) / len(value)

    return sum_class / len(grades)'''

    # solution 3
    sum_class = 0
    for key, value in grades.items():
        sum_class += statistics.mean(value)
    return sum_class/len(grades)

if __name__== "__main__":
    print(task9({"Ana" : [4.0, 4.5, 5.0], "John" : [5.0, 5.0, 3.0], "Lise" : [5.0, 5.0, 5.0]}))