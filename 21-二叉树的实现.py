"""
二叉查找树是这样一种二叉树结构，它的每个节点的左子节点小于该节点，每个节点的右子节点小于该节点
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return '数据是：{}'.format(self.data)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def init_data(self, datas):
        node_dict = {}
        for d in datas:
            node = Node(d['key'], d['left'], d['right'])
            node_dict[d['key']] = node
        for d in datas:
            node = node_dict[d['key']]
            if node.left:
                node.left = node_dict[node.left]
            if node.right:
                node.right = node_dict[node.right]
            if d['is_root']:
                self.root = node

    def search(self, value, subtree):
        if subtree is None:
            return None
        elif subtree.data > value:
            return self.search(value, subtree.left)
        elif subtree.data < value:
            return self.search(value, subtree.right)
        else:
            return subtree

    def get_min(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self.get_min(subtree.left)

    def _insert_data(self, subtree, value):
        if subtree is None:
            subtree = Node(value)
        elif subtree.data > value:
            subtree.left = self._insert_data(subtree.left, value)
        elif subtree.data < value:
            subtree.right = self._insert_data(subtree.right, value)
        return subtree  # 避免返回的root是None

    def add(self, value):
        # 查找数据，是否存在
        node = self.search(value, self.root)
        if node:
            return "值已存在！"
        else:
            self.root = self._insert_data(self.root, value)

    def _remove_node(self, subtree, value):
        if subtree is None:
            return None
        elif subtree.data > value:
            subtree.left = self._remove_node(subtree.left, value)
            return subtree
        elif subtree.data < value:
            subtree.right = self._remove_node(subtree.right, value)
            return subtree
        else:
            # 找到数据节点，三种情况
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left:
                    return subtree.left
                else:
                    return subtree.right
            else:
                node = self.get_min(subtree.right)
                subtree.data = node.data
                subtree.right = self._remove_node(subtree.right, node.data)
                return subtree

    def remove(self, value):
        if self.search(value, self.root):
            self._remove_node(self.root, value)


if __name__ == '__main__':
    node_list = [
        {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
        {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
        {'key': 4, 'left': 1, 'right': None, 'is_root': False},
        {'key': 1, 'left': None, 'right': None, 'is_root': False},
        {'key': 41, 'left': 29, 'right': None, 'is_root': False},
        {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
        {'key': 23, 'left': None, 'right': None, 'is_root': False},
        {'key': 37, 'left': None, 'right': None, 'is_root': False},
        {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
        {'key': 71, 'left': None, 'right': 84, 'is_root': False},
        {'key': 100, 'left': None, 'right': None, 'is_root': False},
        {'key': 84, 'left': None, 'right': None, 'is_root': False},
    ]

    tree = Tree()
    tree.init_data(node_list)
    # print(tree.search(41, tree.root))
    # print(tree.search(66, tree.root))
    # print(tree.get_min(tree.root))
    # tree.add(60)
    # tree.add(50)
    # tree.add(70)
    print(tree.root.data)
    # print(tree.root.left)
    # print(tree.root.right)
    tree.remove(12)
    print(tree.root.left)
