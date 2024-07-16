from typing import Any

from to_do import TODO


def guide19(supermarket: dict[str, dict[str, Any]]) -> str:
    Min_price = 1000000
    for product,spec in supermarket.items():
        if spec['price']<Min_price:
            Min_price = spec['price']
            result = product
    return result