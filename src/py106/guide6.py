from typing import Any

from to_do import TODO


def guide6(scandinavia: dict[str, dict[str, Any]]) -> float:
    scandinavia_countries = ['denmark', 'norway', 'sweden', 'finland', 'iceland', 'faroe', 'islands', 'greenland', 'åland']
    sum = 0
    for country,key in scandinavia.items():
        assert(country.lower() in scandinavia_countries)
        sum += key['population']

    return sum