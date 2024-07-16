from to_do import TODO


def task12(a: list[int], b: list[str]) -> dict[int, str]:
    '''result = {}
    for i in range(len(a)):
        result[a[i]] = b[i]

    return result'''

    return {a[i]:b[i] for i in range(len(a))}