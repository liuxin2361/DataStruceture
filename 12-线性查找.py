def line_search(find_value, args):
    for index, value in enumerate(args):
        if find_value == value:
            return index
    return -1


def line_search2(func, args):
    for index, value in enumerate(args):
        if func(value):
            return index
    return -1


def line_search3(find_value, args):
    """
    递归实现线性查找
    :param find_value:
    :param args:
    :return:
    """
    if len(args) == 0:
        return -1
    index = len(args) - 1
    if args[index] == find_value:
        return index
    return line_search3(find_value, args[:index])


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # assert line_search(5, nums) == 5
    # print(line_search2(lambda x: x == 9, nums))
    print(line_search3(5, nums))
