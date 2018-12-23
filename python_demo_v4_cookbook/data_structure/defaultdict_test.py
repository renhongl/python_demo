
from collections import defaultdict

data = defaultdict(list)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

for key, value in s:
    data[key].append(value)


print(data)
