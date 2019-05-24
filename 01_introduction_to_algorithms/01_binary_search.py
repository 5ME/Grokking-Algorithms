# -*- coding: utf-8 -*-
# 二分查找（仅当列表有序时，二分查找才有用）

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
