from to_do import TODO


def guide11(sales: str) -> str:
    result = sales[0:5]
    return result


if __name__ == '__main__':
    print(guide11('SDNFSNSI'))
    print(guide11('SINFSNSD'))
    print(guide11('SDNFSISN'))

