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

    def __clear__(self, value=None):
        for i in range(self.__size):
            self.__item[i] = value


if __name__ == '__main__':
    a1 = Array(4)
    a1[0] = '张三'
    a1[1] = '猪八戒'
    print(a1[0])
    print(a1[1])
    print('-' * 30)
    for v in a1:
        print(v)
    print(len(a1))
    list()
