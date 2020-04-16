"""
链接法(chaining)解决哈希冲突
"""


class Array:
    def __init__(self, size):
        self.__size = size  # 记录容器大小
        self.__item = [None] * size  # 分配空间
        self.__length = 0

    def __setitem__(self, key, value):
        self.__item[key] = value
        self.__length += 1

    def __getitem__(self, key):
        return self.__item[key]

    def __len__(self):
        return self.__length

    def __iter__(self):
        for value in self.__item:
            yield value


class Slot:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return 'key:{} value:{}'.format(self.key, self.value)


class HashTable:
    def __init__(self):
        self.size = 4
        self.items = Array(self.size)

    def _get_index(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        s = Slot(key, value)
        index = self._get_index(key)  # 获取默认的索引位置
        if self.items[index]:
            if self.items[index].key == key:
                self.items[index].value = value
            else:
                temp_next = self.items[index].next
                while temp_next is not None:
                    if temp_next.key == key:
                        temp_next.value = value
                        return
                    temp = temp_next
                    temp_next = temp.next
                temp_next = s
                return
        self.items[index] = s

    def get(self, key):
        index = self._get_index(key)  # 获取key对应的索引
        if self.items[index]:
            if self.items[index].key == key:
                return self.items[index]
            else:
                temp_next = self.items[index].next
                while temp_next is not None:
                    if temp_next.key == key:
                        return temp_next
                    temp = temp_next
                    temp_next = temp.next
                return None
        return None


if __name__ == '__main__':
    h = HashTable()
    h.put('name', 'foo')
    h.put('sex1', '男')
    h.put('sex2', '女')
    h.put('sex3', '保密')
    print(h.get('name'))
    print(h.get('sex3'))
    print(h.get('sex2'))
    print(h.get('sex1'))
