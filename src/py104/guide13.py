from to_do import TODO


def guide13(a: str, b: str) -> list[str]:
    # result= []
    # for lettera in a:
    #     if lettera in b:
    #         result.append(lettera)
    #
    # return result

    #solution 2
    #return [lettera for lettera in a if lettera in b]

    #solution 3
    filtered_letter = filter(lambda letter: letter in b ,a)
    return filtered_letter