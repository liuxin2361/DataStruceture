from collections import deque


class Stack:
    """
    双端队列（包含了栈的实现）
    """

    def __init__(self):
        self.item = deque()

    def put(self, value):
        self.item.append(value)

    def pop(self):
        return self.item.pop()

    def pop2(self):
        return self.item.popleft()

    def put2(self, value):
        self.item.appendleft(value)


if __name__ == '__main__':
    s = Stack()
    s.put('foo')
    s.put('foo1')
    s.put('foo2')
    print(s.pop2())
    print(s.pop2())
    print(s.pop2())
