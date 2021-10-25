class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")
        return self.items.pop(0)

    def last(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")
        return self.items[-1]

    def first(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")
        return self.items[0]

    def __len__(self):
        return len(self.items)

    def __getitem__(self, i):
        return self.items[i]


def try_sort(n, to_sort, k):
    queues = [Queue() for _ in range(k)]
    order = list()
    for i in range(n):
        available = -1
        for j in range(len(queues)):
            if queues[j].empty() or queues[j].last() <= to_sort[i]:
                available = j
                break
        if available == -1:
            print('NO', end='')
            return
        queues[available].enqueue(to_sort[i])
        order.append(available + 1)
    print('YES')
    for i in range(n):
        print('I({})'.format(order[i]))
    for i in range(n):
        min_number = float('inf')
        min_index = float('inf')
        for j in range(len(queues)):
            if not queues[j].empty():
                if queues[j].first() <= min_number:
                    min_index = j
                    min_number= queues[j].first()
        queues[min_index].dequeue()
        print('R({})'.format(min_index+1))


n = int(input())
to_sort = list(map(int, input().split()))
k = int(input())

try_sort(n, to_sort, k)






