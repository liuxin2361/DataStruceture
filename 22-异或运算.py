"""
一个数组中，一种数出现奇数次，其他数出现偶数次，求奇数次的数，要求时间度O(N)，空间复杂度O(1)
"""

def get_result(args):
    a = 0
    for i in args:
        a ^= i
    return a


def get_change(list, i, j):
    list[i] = list[i] ^ list[j]
    list[j] = list[i] ^ list[j]
    list[i] = list[i] ^ list[j]


if __name__ == '__main__':
    int_list = [1, 3, 3, 5, 5, 6, 6, 6, 6]
    print(get_result(int_list))
    get_change(int_list, 2, 3)
    print(int_list)
