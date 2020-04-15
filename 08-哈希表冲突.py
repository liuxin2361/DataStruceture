"""
二次探查法解决哈希冲突
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
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return 'key:{} value:{}'.format(self.key, self.value)


class HashTable:
    def __init__(self):
        self.size = 4
        self.items = Array(self.size)

    def _get_index(self, key):
        return hash(key) % self.size

    def _find_index_to_insert(self, key):
        """
        插入数据时，为key创建对应的新索引
        :param key:
        :return:
        """
        index = self._get_index(key)
        while self.items[index] is not None:
            if self.items[index].key == key:
                return index
            else:
                index = (5 * index + 1) % self.size
        return index

    def _find_key(self, key):
        """
        根据key查找时，找出key对应存放的索引
        :param key:
        :return:
        """
        index = self._get_index(key)
        while self.items[index] is not None:
            if self.items[index].key == key:
                return index
            else:
                index = (5 * index + 1) % self.size
        return None

    def put(self, key, value):
        s = Slot(key, value)
        index = self._find_index_to_insert(key)
        self.items[index] = s

    def get(self, key):
        index = self._find_key(key)  # 获取key对应的索引
        return self.items[index]


if __name__ == '__main__':
    h = HashTable()
    h.put('name', 'foo')
    h.put('sex3', '男')
    h.put('sex1', '女')
    h.put('sex2', '保密')
    print(h.get('name'))
    print(h.get('sex3'))
    print(h.get('sex2'))
    print(h.get('sex1'))
