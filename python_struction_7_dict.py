class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return "Assoc({0},{1})".format(self.key, self.value)

class StackUnderFlow(ValueError):
    pass
    # 栈下溢

# 利用list写stack
class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderFlow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderFlow("in SStack pop()")
        return self._elems.pop()



# use list to achieve dict
class DictList:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def num(self):
        return len(self._elems)

    def search(self, key):
        pass

    def insert(self, key, value):
        pass

    def delete(self, key):
        pass

    def values(self):
        pass

    def entries(self):
        pass



# 有序线性表可用二分法检索
def bisearch(lst, key):
    low , high = 0, len(lst) -1
    while low <= high:
        mid = low + (high - low)//2
        if key == lst[mid].key:
            return lst[mid].value
        if key < lst[mid].value:
            high = mid -1
        else:
            low = mid + 1

# 可以继承ListDict， 定义新的字典类，重写search， insert，delete

# 线性表实现字典只适合简单需求
# hash Table

# 二叉树排序字典类

class BinTNode:
    def __init__(self, dat, left = None, right = None):
        self.data = dat
        self.left = left
        self.right = right



def bt_search(btree, key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key< entry.key:
            bt = bt.left
        elif key > bt.data:
            bt = bt.right
        else:
            return entry.value
    return None

class DictBinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None


    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key <  entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return
    # 给字典定义一个迭代器方法，生成其中所有值的序列
    def values(self):
        t, s =self._root, SStack()
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        yield t.data.value
        t = t.right

    def entries(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key, t.data.value
            t = t.right


    def delete(self, key):
        p, q = None, self._root
#         维持p为q的父节点
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right

        if q is None:
            return

            # q引用要删除节点，p是其父节点or None
        if q.left is None:
            # q no left
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return


        r = q.left
        while r.right is not None:
            r = r.right
        r.right = q.right

        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left


    def print(self):
        for k, v in self.entries():
            print(k,v)

def buld_dictBinTree(entries):
    dic = DictBinTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic







