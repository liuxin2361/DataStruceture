def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    count = len(nums) // 2
    left = merge_sort(nums[:count])
    right = merge_sort(nums[count:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])  # 当有最后只剩一个数字时，转成列表进行相加
    result += list(right[r:])  # 当有最后只剩一个数字时，转成列表进行相加
    return result


if __name__ == '__main__':
    num = [10, 1, 35, 61, 89, 36, 55]
    print(merge_sort(num))
