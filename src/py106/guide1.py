from typing import Callable

from to_do import TODO


def guide1(script: Callable[[], list[int]]) -> list[int]:
    result = []
    try:
        list_out = script()
        #for index,value in enumerate(list_out):
            #result.append(index*value)
        #return result

        # list comprehension
        #return [index*value for index,value in enumerate(list_out)]

        # tranaformation
        return list(map(lambda item: item[0]*item[1],enumerate(list_out)))

    except FileNotFoundError:
        return result


