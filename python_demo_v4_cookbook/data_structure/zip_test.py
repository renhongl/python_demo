

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

ziped = zip(prices.keys(), prices.values())
print(list(ziped))

min_item_by_key = min(zip(prices.keys(), prices.values()))
print(min_item_by_key)

min_item_by_value = min(zip(prices.values(), prices.keys()))
print(min_item_by_value)