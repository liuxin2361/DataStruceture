def insert_sort(args):
    for i in range(1, len(args)):
        for j in range(i, 0, -1):
            if args[j] < args[j - 1]:
                args[j], args[j - 1] = args[j - 1], args[j]


if __name__ == '__main__':
    nums = [10, 1, 35, 61, 89, 36, 55]
    insert_sort(nums)
    print(nums)
