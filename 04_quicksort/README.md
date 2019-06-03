# 第4章 快速排序

## 1. 分而治之

分而治之（divide and conquer，D&C）是一种递归式问题解决方法。

D&C的工作原理：

1. 找出简单的基线条件；
2. 确定如何缩小问题的规模，使其符合基线条件。

D&C并不是解决问题的算法，而是一种解决问题的思路。

数组求和示例：

+ 循环求解
    ``` Python
    def sum(arr):
        total = 0
        for x in arr:
            total += x
        return total
    ```
+ 递归求解
    ``` Python
    def sum(arr):
        if arr == []:
            return 0
        else:
            return arr[0] + sum(arr[1:])
    ```
+ 编写涉及数组的递归函数时，基线条件通常是数组为空或只包含一个元素。

***

## 2. 快速排序

+ 快速排序是常用的排序算法，比选择排序快得多，是**最快的排序算法之一**。
+ C语言标准库中的`qsort`函数就是快速排序。
+ 快速排序使用了**分而治之**。
+ 基线条件：
  
  数组为空或只有一个元素。这样的数组无需排序。

+ 快速排序工作原理：
  
  1. 选择一个元素作为基准值（pivot）；
  2. 找出比基准值小的元素和比基准值大的元素，即分区（partitioning）；
  3. 分别对子数组进行快速排序。

+ 快速排序代码：
    ``` Python
    def quicksort(arr):
        if len(arr) < 2:        # 基线条件
            return arr
        else:                   # 递归条件
            # 基准值
            pivot = arr[0]
            # 比基准值小的元素
            less = [i for i in arr[1:] if i <= pivot]
            # 比基准值大的元素
            greater = [i for i in arr[1:] if i > pivot]
            # 分别对子数组进行快速排序
            return quicksort(less) + [pivot] + quicksort(greater)
    ```

+ 快速排序复杂度分析
  + 无论如何划分数组，每层都涉及`O(n)`个元素
  + 最佳情况：
  
    调用栈高度为`O(log n)`，每层需要的时间为`O(n)`，因此时间复杂度为`O(n) * O(log n) = O(nlogn)`；

  + 最差情况：
    调用栈高度为`O(n)`，每层需要的时间为`O(n)`，因此时间复杂度为`O(n) * O(n) = O(n^2)`；

  + 平均情况：
    
    快速排序的最佳情况也是其平均情况。只要每次随机选择基准值，快速排序的平均运行时间就将为`O(nlogn)`。

