'''
7 3
'''

MAX_SIZE, k = map(int, input().split())


class CircularQueue:
    def __init__(self):
        self.front, self.rear = 0, 0
        self.items = [i + 1 for i in range(MAX_SIZE)]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % MAX_SIZE

    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        '''
        is_full check
        '''
        if not self.is_full():
            self.rear = (self.rear + 1) % MAX_SIZE
            self.items[self.rear] = item

    def dequeue(self):
        '''
        is_empty check
        '''
        if not self.is_empty():
            self.front = (self.front + 1) % MAX_SIZE

    def peeK(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front + 1:self.rear + 1]
        else:
            out = self.items[self.front + 1:MAX_SIZE] + self.items[0:self.rear + 1]
