import re
import pandas as pd

class HashTable:
    def __init__(self):
        self.size = 20000
        # 哈希表统计上限size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.frequency = [None] * self.size

    def put_data_in_slot(self, data, slot):
        if self.slots[slot] == None:
            self.slots[slot] = slot
            self.data[slot] = data
            self.frequency[slot] = 1
            return True
        else:
            if self.slots[slot] == slot:
                if self.data[slot] == data:
                    self.frequency[slot] += 1
                    return True
                else:
                    return False
            else:
                return False

    def put(self, data):
        slot = self.hash_function(data, self.size)
        # slot 就是hash数
        result = self.put_data_in_slot(data, slot)
        while not result:
            slot = self.rehash(slot, self.size)
            result=self.put_data_in_slot(data, slot)

    # reminder method
    # 取余数
    def hash_function(self, data, size):
        key = 0
        len = 1
        transfered = map(ord, data)
        for item in transfered:
            key = key + item * len
            len += 1
        return key % size

    # +1方法
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get_frequency(self, data):
        stop = False
        found = False
        count = 0
        start_slot = self.hash_function(data, self.size)
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.data[position] == data:
                count = self.frequency[position]
                found = True
            else:
                position = self.rehash(position, self.size)
                if position == start_slot:
                    stop = True
        return count



    # def get(self, key):
    #     start_slot = self.hash_function(key, len(self.slots))
    #     data = None
    #     stop = False
    #     found = False
    #     position = start_slot
    #     while self.slots[position] != None and not found and not stop:
    #         if self.slots[position] == key:
    #             found = True
    #             data = self.data[position]
    #         else:
    #             position = self.rehash(position, len(self.slots))
    #             if position == start_slot:
    #                 stop = True
    #     return data

    # def __getitem__(self, key):
    #     return self.get(key)
    #
    # def __setitem__(self, key, data):
    #     self.put(key, data)

if __name__ == '__main__':
    table = HashTable()
    f = open('text.txt','r')
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
            continue
        line_words = re.findall("\w+", str.lower(line))

        for word in line_words:
            table.put(word)

    word_total = {}

    for item in table.data:
        if item != None:
            frequency = table.get_frequency(item)
            word_total[item] = frequency
            # print(item,'--',frequency)

    print(word_total)
    df = pd.DataFrame(word_total, index=[0])
    print(df)
    f.close()