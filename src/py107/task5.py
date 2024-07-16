# TODO("Delete this 'TODO' and create your function here")
def groceries(grocery_items: list[dict[str,]]) -> float:
    result = 0
    for item in grocery_items:
        result += item['price'] * item['quantity']
    return result

print(groceries([{'product': 'Milk', 'quantity': 3, 'price': 1.5}, {'product': 'Meat', 'quantity': 2, 'price': 2.5}]))