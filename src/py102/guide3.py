from to_do import TODO
import math
def guide3(radius: float) -> float:
    result = (4 * math.pi * radius**3) /3
    return result

if __name__== "__main__":
    print(guide3(5))
    print(guide3(1))
    print(guide3(0))