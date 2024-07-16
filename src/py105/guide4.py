from to_do import TODO


def guide4(supermarket: dict[str, float], ingredients: list[str]) -> float:
    result = 0
    for ingredient in ingredients:
        ingredient_price = supermarket.get(ingredient,0)
        result += ingredient_price

    return result

if __name__== "__main__":
    print(guide4({"cheese" : 10.0, "eggs" : 5.0, "milk" : 30.0},["cheese", "eggs", "juice"]))