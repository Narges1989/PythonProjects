from to_do import TODO


def guide10(companies: list[str]) -> list[str]:
    result = []
    for company in companies:
        if company is None:
            continue
        new_company =''
        for index,letter in enumerate(company):
            new_company += letter.upper() if index % 2 == 0 else letter.lower()
        result.append(new_company)
    return result





    return TODO(
        "Replace this 'TODO' with the variable 'result'. Do not erase the 'return' keyword"
    )
