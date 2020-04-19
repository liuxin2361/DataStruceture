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


class Heap:
    def __init__(self):
        self._items = Array(10)
        self._count = 0

    def __iter__(self):
        for v in self._items:
            yield v

    def add(self, value):
        self._items[self._count] = value
        self._siftup(self._count)
        self._count += 1

    def _siftup(self, index):
        """
        最大堆排序
        :param index:
        :return:
        """
        if index > 0:
            parent = int((index - 1) / 2)
            if self._items[index] > self._items[parent]:
                self._items[index], self._items[parent] = self._items[parent], self._items[index]
                self._siftup(parent)

    def pop(self):
        """
        最大堆删除根节点数据
        :return:
        """
        if self._count <= 0:
            return None
        else:
            value = self._items[0]
            self._count -= 1
            self._items[0] = self._items[self._count]
            self._siftdown(0)
            self._items[self._count] = None
            return value

    def _siftdown(self, index):
        """
        删除根节点数据后重新排序
        :param index:
        :return:
        """
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if right < self._count:
            if self._items[right] >= self._items[left]:
                if self._items[right] > self._items[index]:
                    largest = right
            else:
                if self._items[left] > self._items[index]:
                    largest = left
        else:
            if self._items[left] > self._items[index]:
                largest = left
        if largest != index:
            self._items[index], self._items[largest] = self._items[largest], self._items[index]
            self._siftdown(largest)


if __name__ == '__main__':
    heap = Heap()
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(30)

    print(heap.pop(), '---------------------')
    for i in heap:
        if i:
            print(i)
