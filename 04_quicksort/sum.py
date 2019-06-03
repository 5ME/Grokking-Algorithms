# -*- coding: utf-8 -*-
# 数组求和

# 循环求解
def sum1(arr):
    total = 0
    for x in arr:
        total += x
    return total

# 递归求解
def sum2(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum2(arr[1:])

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("循环求解：" + str(sum1(arr)))
    print("递归求解：" + str(sum2(arr)))

if __name__ == "__main__":
    main()
