"""
一个数组中，两种数出现奇数次，其他数出现偶数次，求奇数次的数，要求时间度O(N)，空间复杂度O(1)
"""


def get_change(array):
    # 数组内所有数异或一次，则得到奇数次两种数的异或结果
    err = 0
    for i in array:
        err ^= i
    # err必定不等于0，则二进制位中必有一位是1
    # ~err 取反
    # & 与
    # 将err二进制位最右段1提取出来,其余位都为0
    right_one = err & (~err + 1)
    arr1 = 0
    # 对err相同位置为1的数异或运算，结果剩下一个出现奇数次的数
    for i in array:
        if (right_one & i) == 0:
            arr1 ^= i
    return arr1, err ^ arr1


if __name__ == '__main__':
    arr = [1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 7, 7, 8, 8]
    print(get_change(arr))
