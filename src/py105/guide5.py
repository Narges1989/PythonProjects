from to_do import TODO


def guide5(universities: dict[str, str]) -> dict[str, str]:
    result = {}
    for key,value in universities.items():
        result[value] = key

    return result

if __name__ == "__main__":
    print(guide5({"UTP" : "Panama", "KTH" : "Sweden", "MIT" : "USA"}))
