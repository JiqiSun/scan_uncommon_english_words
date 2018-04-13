def table_generator(items, col):
    _items = items
    row = 1
    table = dict()

    while _items:
        table[row] = _items[:col]
        del _items[:col]
        row += 1

    return table
