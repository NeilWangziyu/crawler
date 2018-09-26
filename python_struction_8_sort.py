import random
class record:
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum


def insert_Sort1(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j>0 and lst[j-1].key > x.key:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x
    return lst

def insert_Sort2(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j<len(lst)-1 and lst[j+1].key<x.key:
            lst[j] = lst[j+1]
            j += 1
        lst[j] = x
    return lst


def insert_Sort3(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j>0 and lst[j-1].key < x.key:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x
    return lst

def select_sort(lst):
    for i in range(len(lst)-1):
        k = i
        for j in range(i, len(lst)):
            if lst[j].key < lst[k].key:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]

    return lst


def bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst)-i):
            if lst[j].key < lst[j-1].key:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                found = True
        if not found:
            break
    return lst



def quick_sort1(lst):
    if len(lst)<2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i.key <= pivot.key]
        more = [i for i in lst[1:] if i.key > pivot.key]
        return quick_sort1(less) + [pivot] + quick_sort1(more)


def quick_sort2(lst):
    if len(lst)<2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i.key <= pivot.key]
        more = [i for i in lst[1:] if i.key > pivot.key]
        return quick_sort2(more) + [pivot] + quick_sort2(less)



init = []
for t in range(10):
    init.append(record(random.randrange(15),t))


for each in init:
    print(each.key, each.datum)


init_sort = insert_Sort1(init)
print('------------------')
for each in init_sort:
    print(each.key, each.datum)

print('------------------')

init_sort = insert_Sort2(init)

for each in init_sort:
    print(each.key, each.datum)


init_sort = insert_Sort3(init)
print('------------------')
for each in init_sort:
    print(each.key, each.datum)

init_sort = select_sort(init)
print('------------------')
for each in init_sort:
    print(each.key, each.datum)

init_sort = bubble_sort(init)
print('------------------')
for each in init_sort:
    print(each.key, each.datum)


init_sort = quick_sort1(init)
print('quick sort1------------------')
for each in init_sort:
    print(each.key, each.datum)


init_sort = quick_sort2(init)
print('qucik sort2------------------')
for each in init_sort:
    print(each.key, each.datum)