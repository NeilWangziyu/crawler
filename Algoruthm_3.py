# -----------------------
# from time import *
# t0 = time()
# count = 10**5
# nums = []
# for i in range(count):
#     nums.append(i)
#
# nums.reverse()
# t1 = time() - t0
# print(t1)
#
# r0 = time()
# nums = []
# for i in range(count):
#     nums.insert(0,i)
#
# t2 = time() - t0
# print(t2)
# ----------------------------

# print(hash("hello world"))

# ----------------------------
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) -1 ]

    def size(self):
        return len(self.items)

s = Stack()
print(s.is_empty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.peek())
print(s.size())
print(s.is_empty())
print(s.items)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())
print('-----------------------')
# ----------------------------
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue('Hello')
q.enqueue('Dog')
print(q.items)
q.enqueue(3)
q.dequeue()
print(q.items)
print('-----------------------')
# ----------------------------
# 双线队列：左右两边都可以插入和删除的队列
# 以右端为front，左端为rear
# class Deque:
#
#
#
#
#
#
#
# ----------------------------



