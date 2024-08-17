import heapq
from functools import cmp_to_key

# Python default heap is minq. for max heap we need to write comparator

jobsAsList = [(1, 'eat'), (3, 'code'), (2, 'sleep')]  # Heaqpq only support list
jobsAsDict = {1: 'eat', 3: 'code', 2: 'sleep'}  # Heapq doesnt support Dict

heapq.heapify(jobsAsList)

for _ in range(len(jobsAsList)):
    popped_item = heapq.heappop(jobsAsList)
    print(popped_item)

# heapq.heapify(jobsAsDict)
# for _ in range(len(jobsAsDict)):
#     popped_item = heapq.heappop(jobsAsList)
#     print(popped_item)


# Heap with comparator
print("Heapq with comparator")
l = [['a', 3], ['b', 1]]


def new_heapify(data, cmp):
    s = list(map(cmp_to_key(cmp), data))
    heapq.heapify(s)
    return s


def new_heappop(data):
    return heapq.heappop(data).obj


def foo(x, y):
    return x[1] - y[1]


heap = new_heapify(l, cmp=foo)
for _ in l:
    print(new_heappop(heap))
