def grocery_store(**kwargs):
    sorted_grocery = sorted(kwargs.items(), key=lambda item: (-(item[1]), -len(item[0]), item[0]))
    result = []
    for product in sorted_grocery:
        result.append(f"{product[0]}: {product[1]}")
    return '\n'.join(result)


print(grocery_store(bread=5, pasta=12, eggs=12))
print(grocery_store(
 bread=2,
 pasta=2,
 eggs=20,
 carrot=1,
))