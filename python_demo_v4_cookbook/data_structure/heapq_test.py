
from heapq import heappush, heappop, nlargest, nsmallest

data = []
heappush(data, 30)

heappush(data, 54)
heappush(data, 12)
heappush(data, 9)
heappush(data, 76)
heappush(data, 43)

print(heappop(data))
print(nlargest(3, data))
print(nsmallest(2, data))