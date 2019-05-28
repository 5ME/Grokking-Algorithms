# -*- coding: utf-8 -*-
# 选择排序
# 2019-05-28

# 找出数组最小值及其索引
def findSmallest(arr):
    # 初始化最小值及其索引
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index       # 返回最小值索引

# 选择排序
def selectionSort(arr):
    newArr = []
    # 循环每次找出数组中最小值并将其添加到新数组
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def main():
    arr = [5, 3, 6, 2, 10]
    print(selectionSort(arr))

if __name__ == '__main__':
    main()
