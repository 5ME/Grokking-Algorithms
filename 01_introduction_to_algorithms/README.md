# 第1章 算法简介

1. 大O表示法
   
   大O表示法指出了算法运行时间的增速。
   
   常见大O运行时间：

   + O(log n)   对数时间，如二分查找
   + O(n)       线性时间，如简单查找
   + O(n*log n) 如快速排序（较快的排序算法） 
   + O(n^2)     如选择排序（较慢的排序算法） 
   + O(n!)      如旅行商问题，非常慢的算法
   
   算法复杂度是从其增速的角度度量的，是指随着操作数的增加，其运行时间将以什么样的速度增加。

2. 二分查找
   
   仅当列表有序时，二分查找才可使用。

   二分查找示例：

   ``` Python
    # -*- coding: utf-8 -*-
    # 二分查找（仅当列表有序时，二分查找才有用）
    # 2019-05-24

    def binary_search(list, item):
        # 设定起始low和high
        low = 0
        high = len(list) - 1
        # 只要范围没有缩小到1个元素就一直查找
        while low <= high:
            mid = (low + high) // 2     # //为取整除 - 向下取接近除数的整数
            guess = list[mid]
            if guess == item:       # 找到元素
                return mid
            if guess < item:        # 猜的数字小了
                low = mid + 1
            else:                   # 猜的数字大了
                high = mid - 1
        return None     # 没有找到元素，返回None

    def main():
        my_list = [1,2,3,4,5,6,7,8,9,10]
        print(binary_search(my_list, 7))    # 输出6
        print(binary_search(my_list, 2))    # 输出1
        print(binary_search(my_list, 15))   # 输出None

    if __name__ == '__main__':
        main()

   ```
   二分查找时间复杂度：O(log n)
   