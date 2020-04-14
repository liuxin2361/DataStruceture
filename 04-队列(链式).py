class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return 'Node:{}'.format(self.value)


class DoubleLinkList:
    def __init__(self):
        self.root = Node()
        self.size = 0
        self.end = None

    def append(self, value):
        node = Node(value)  # 封装节点对象
        # 判断是否已经有数据
        if not self.end:  # 没有节点
            self.root.next = node  # 将root的下一个节点设置为新的node节点
            node.prev = self.root  # 设置新节点的上一个节点为root
        else:
            self.end.next = node  # 将原来最后节点的下一个节点，设置为新的node节点
            node.prev = self.end  # 设置新节点的上一个节点为原来的最后一个节点
        self.end = node  # 更新最后一个节点新加的node节点
        self.size += 1

    def append_first(self, value):
        node = Node(value)
        # 判断是否已经有数据
        if not self.end:  # 没有节点
            self.end = node  # 更新最后一个节点新加的node节点
        else:
            temp = self.root.next  # 保存原来root连接的节点
            node.next = temp  # 设置新节点的下一个节点为原来的第一个节点
            temp.prev = node  # 更行原来的第一个节点的上一个节点位置为新的node节点
        node.prev = self.root  # 设置新节点的上一个节点为root
        self.root.next = node  # 将root的下一个节点设置为新的node节点
        self.size += 1

    def __iter__(self):
        current = self.root.next
        if current:
            while current is not self.end:
                yield current
                current = current.next
            yield current

    def revers_iter(self):
        current = self.end  # 获取最后一个节点
        if current:
            while current is not self.root:
                yield current
                current = current.prev

    def remove_first(self):
        if self.end:
            temp = self.root.next  # 获取第一个节点
            self.root.next = temp.next  # 设置第二个节点 root的下一个节点
            if temp.next:  # 判断temp的下一个节点是否仍然是一个节点
                temp.next.prev = self.root  # 设置第一个节点的上一个节点为root
            return temp


class Queue:
    def __init__(self, size=4):
        self.item = DoubleLinkList()
        self.size = size
        self.length = 0

    def put(self, value):
        """
        存放数据
        :param value:
        :return:
        """
        self.item.append(value)
        self.length += 1

    def pop(self):
        """
        取出并删除数据
        :return:
        """
        if self.length <= 0:
            return "No value"
        self.length -= 1
        return self.item.remove_first()

    def empty(self):
        pass


if __name__ == '__main__':
    q = Queue()
    q.put('唐三藏')
    q.put('嫦娥')
    q.put('月兔')

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
