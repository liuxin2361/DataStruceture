"""
选择排序
"""


def selector_sort(args):
    for j in range(0, len(args) - 1):
        min_index = j
        for i in range(j + 1, len(args)):
            if args[i] < args[min_index]:
                min_index = i
        args[j], args[min_index] = args[min_index], args[j]


if __name__ == '__main__':
    nums = [10, 1, 35, 61, 89, 36, 55]
    selector_sort(nums)
    print(nums)
