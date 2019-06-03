# -*- coding: utf-8 -*-
# 快速排序

def quicksort(arr):
    if len(arr) < 2:            # 基线条件
        return arr
    else:                       # 递归条件
        # 基准值
        pivot = arr[0]
        # 比基准值小的元素
        less = [i for i in arr[1:] if i <= pivot]
        # 比基准值大的元素
        greater = [i for i in arr[1:] if i > pivot]
        # 分别对子数组进行快速排序
        return quicksort(less) + [pivot] + quicksort(greater)

def main():
    arr = [6, 5, 8, 3, 9, 7, 4]
    print(quicksort(arr))

if __name__ == "__main__":
    main()