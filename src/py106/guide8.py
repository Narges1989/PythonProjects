def guide8(a: int, b: int) -> dict[int, dict[str, list[int]]]:
    if a>=b:
        return {0:0}
    result = {}
    for number1 in range(a, b+1):
        result[number1] = {
            "multiplication": [number1 * number for number in range(1, 6)],
            "summation": [number1 + number for number in range(1, 6)],
        }

    return result


if __name__ == "__main__":
    print(guide8(a=1, b=3))
    #print(guide8(a=10, b=3))
