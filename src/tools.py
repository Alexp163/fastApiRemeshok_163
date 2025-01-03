def make_product_groups(products, amount):
    groups = []
    group = []
    i = 0
    for product in products:
        group.append(product)
        i += 1
        if i == amount:
            groups.append(group)
            group = []
            i = 0
    if i != 0:
        groups.append(group)
    return groups


def make_categories_groups(categories, amount):
    for category in categories:
        category.groups = make_product_groups(category.products, amount)
    return categories
