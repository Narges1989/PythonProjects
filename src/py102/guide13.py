from to_do import TODO


def guide13(sales: str) -> bool:
    if 'D' in sales:
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    # input = 'SNFSNII', result = False
    print(guide13('SNFSNII'))

    # input = 'SNFDSNII', result = True
    print(guide13('SNFDSNII'))