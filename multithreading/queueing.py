from queue import Queue, LifoQueue, PriorityQueue
q = Queue()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    q.put(number)
# FIFO by Default
print(q.get())
print(q.get())

ql = LifoQueue()
for number in numbers:
    ql.put(number)
# LIFO
print(ql.get())
print(ql.get())

# Priority order using tuple
qp = PriorityQueue()
qp.put((2, 'Hi'))
qp.put((3, 'Universe'))
qp.put((1, 'Hello'))
qp.put((15, 15))
qp.put((11, 11))
qp.put((18, "Least priority"))

while not qp.empty():
    print(qp.get())
