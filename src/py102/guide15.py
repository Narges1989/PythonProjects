from to_do import TODO


def guide15(sales: str) -> int:
    count_Sweden = sales.count('S')
    count_Norway = sales.count('N')
    result = count_Sweden + count_Norway
    return result

if __name__ == '__main__':
    # input = 'SDNFSNII', output = 4
    print(guide15('SDNFSNII'))

    # input = 'SDNSFSNIIN', output = 6
    print(guide15('SDNSFSNIIN'))
