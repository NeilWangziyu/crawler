import numpy as np
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinnkedLidtUnderflow (ValueError):
    pass

# ------------------------------------------------
# 基础单链表
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)
#         从表头插入元素

    def pop(self):
        if self._head is None:
            raise LinnkedLidtUnderflow("inn pop")
        e = self._head.elem
        self._head = self._head.next
        return e
    # 删除第一个元素

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
# 末尾插入一个元素

    def pop_last(self):
        if self._head is None:
            raise LinnkedLidtUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        #     直到p是最后一个节点
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
#    pred：判断谓词,不好用，只能找到满足的第一个元素，使用filter代替

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print(' ')

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q._next = p
            p = q
        self._head = p
#     it can only be used in LList, in other class, it must be rewrited


# ------------------------------------------------
class LList1(LList):
#     定义一个基于LList的列表LList1， 其带有尾节点
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)


    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    # POP没有变，因为判断是否是空，采用head判断
    def pop(self):
        if self._head is None:
            raise LinnkedLidtUnderflow("inn pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def pop_last(self):
        if self._head is None:
            #the list is empty
            raise LinnkedLidtUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            #in the list there is only one element
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


# ------------------------------------------------
class LCList:
#     循环单链表类
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            # 建立一个节点的环
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        # 前端弹出
        if self._rear is None:
            raise LinnkedLidtUnderflow("in pop of LCList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next


class DLNode(LNode):
# 双链表类
    def __init__(self, elem, prev = None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


# ------------------------------------------------
class DLList(LList1):
#     双链表实现
    def __init__(self):
        LList.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
#             the list is empyt
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinnkedLidtUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinnkedLidtUnderflow("in pop_last of DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e


# ---------------------
# list examp
def josephus_L(n,k,m):
    people = list(range(1, n+1))

    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m -1)%num
        print(people.pop(i),end=(", " if num > 1 else "\n"))
    return

if __name__ == '__main__':
    pass

    # llist1 = LNode(1)
    # p = llist1
    # for i in range(2,11):
    #     p.next = LNode(i)
    #     p = p.next
    #
    # p = llist1
    # while p is not None:
    #     print(p.elem)
    #     p = p.next

    # mlist1 = LList()
    # for i in range(10):
    #     mlist1.prepend(i)
    # for i in range(11, 20):
    #     mlist1.append(i)
    # # mlist1.printall()
    #
    # for x in mlist1.elements():
    #     print(x)

    # mlist1 = LList1()
    # mlist1.prepend(100)
    # for i in range(1,20):
    #     mlist1.append(i)
    # for x in mlist1.filter(lambda y:y % 2 == 0):
    #     print(x)

    mlist1 = LCList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()

    josephus_L(10, 5 ,2)