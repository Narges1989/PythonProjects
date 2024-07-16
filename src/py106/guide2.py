from typing import Callable

from to_do import TODO


def guide2(script: Callable[[], list[str]]) -> str:
    try:
        names = script()
        result = ''
        for name in names:
            if len(name)> len(result):
                result = name
        #return max(names,key=len)
        return result

    except ZeroDivisionError:
        return ''
