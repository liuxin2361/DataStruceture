def bubble_sort(array):
    count = len(array) - 1
    for i in range(count):
        flag = True
        for j in range(count - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
                flag = False
        if flag:
            print('比较了{}次'.format(i))
            break


if __name__ == '__main__':
    num = [10, 1, 35, 61, 89, 36, 55]
    bubble_sort(num)
    print(num)
