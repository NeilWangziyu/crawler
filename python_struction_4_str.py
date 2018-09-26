import re

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


# 利用列表写stack
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderFlow("in LStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderFlow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem



if __name__ == '__main__':
    # ---------------------------
    # 正则
    # r1 = re.compile("abc")
    # result = re.search(r1, "abcdefg")
    # print(result)
    #
    # result = re.match(r1, "abcdefg")
    # print(result)
    #
    # result = re.split(' ', "abc abb are not the same")
    # print(result)
    #
    # result = re.findall(r1, "abcdabcd tfe ")
    # print(result)
    #
    # ---------------------------

    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())


    st1 = LStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())