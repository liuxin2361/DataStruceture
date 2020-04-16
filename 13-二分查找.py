def binary_search(value, args):
    # 记录列表查找的范围
    begin = 0
    end = len(args) - 1
    while begin <= end:
        # 计算中间索引号
        mid = (begin + end) // 2
        # 比较要查找的数据
        if args[mid] == value:
            return mid
        elif args[mid] > value:
            end = mid - 1
        else:
            begin = mid + 1
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(69, nums))
