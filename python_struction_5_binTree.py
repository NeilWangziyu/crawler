# 优先队列
class PrioQueueError(ValueError):
    pass

class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse = True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()

# 二叉树的实现

class BinTNode:
    def __init__(self, dat, left = None, right = None):
        self.data = dat
        self.left = left
        self.right = right



t = BinTNode(1, BinTNode(2), BinTNode(3))

def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.dat + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)

# 遍历算法
def preorder(t, proc):
    assert (isinstance(t, BinTNode))
    if t is None:
        return
    proc(t.data)
    preorder(t.left)
    preorder(t.right)

def print_BinNodes(t):
    if t is None:
        print("^", end=" ")
        return
    print("(" + str(t.data), end=" ")
    print_BinNodes(t.left)
    print_BinNodes(t.right)
    print(")", end=" ")
print_BinNodes(t)




# 霍夫曼树的实现
class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data

class HuffmanPrioQ(PrioQue):
    def number(self):
        return len(self._elems)

# 霍夫曼树生成算法
def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number()>1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()



