from to_do import TODO


def guide10(sales: str) -> str:
    result = sales[-1]
    return result

if __name__ == '__main__':
    print(guide10('SDNFSNSI'))
    print(guide10('SINFSNSD'))
    print(guide10('SDNFSISN'))
