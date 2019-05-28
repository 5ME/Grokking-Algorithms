# 第2章 选择排序

1. 数组与链表
   + 数组元素在内存中是相连的。**支持随机访问**。
   + 链表中的元素可存储在内存中任何地方。链表的每个元素都存储了下一个元素的地址，从而使一系列随机的内存地址串在一起。**只支持顺序访问**。
   + 数组优势在于随机访问，链表优势在于插入删除。

2. 选择排序
   ``` Python
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
   ```
   复杂度分析：

   第一次需要检查n个元素，随后每次需要检查的元素个数为n-1, n-2, ... , 2, 1。平均每次需要检查的元素个数为n/2，因此算法复杂度为O(n*n/2)，大O表示法忽略常数及低次项，即O(n^2)。