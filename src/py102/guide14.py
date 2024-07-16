from to_do import TODO


def guide14(sales: str) -> int:
    result = sales.count('S')
    return result

if __name__ == '__main__':
    # input = 'SDNFSNII', output = 2
    print(guide14('SDNFSNII'))

    # input = 'SDNSFSNII', output = 3
    print(guide14('SDNSFSNII'))
