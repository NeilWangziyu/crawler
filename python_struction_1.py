def sequential_search(a_list, item):
    pos =0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found == FutureWarning
        else:
            pos += 1
    return found

# test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequential_search(test_list, 3))
# print(sequential_search(test_list, 13))


# 中值查找必须是有序数列
def binary_search(a_list, item):
    first = 0
    last = len(a_list) -1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint -1
            else:
                first = midpoint + 1

    return found

# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binary_search(test_list, 3))
# print(binary_search(test_list, 13))



class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put_data_in_slot(self, key, data, slot):
        if self.slots[slot] == None:
            self.slots[slot] = key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key:
                self.data[slot] = data
                return True
            else:
                return False

    def put(self, key, data):
        slot = self.hash_function(key, self.size)
        # slot 就是hash数
        result  = self.put_data_in_slot(key, data, slot)
        while not result:
            slot = self.rehash(slot, self.size)
            result=self.put_data_in_slot(key, data, slot)

    # reminder method
    # 取余数
    def hash_function(self, key, size):
        return key % size

    # +1方法
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)



def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]  # move backward
            position = position - gap
            a_list[position] = current_value


if __name__ == '__main__':
    # table = HashTable()
    # table[54] = 'cat'
    # table[26] = 'dog'
    # table[93] = 'lion'
    # table[17] = "tiger"
    # table[77] = "bird"
    # table[44] = "goat"
    # table[55] = "pig"
    # table[20] = "chicken"
    #
    # print(table.get(20))
    # print(table.slots)
    # print(table.data)
    # transfered = map(ord, 'cat')
    # for item in transfered:
    #     print(item)


    # for item in 'cat':
    #     print(ord(item))

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 88]
    shell_sort(a_list)
    print(a_list)
