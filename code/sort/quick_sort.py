#conding=utf-8

def quick_sort(alist, first, last):
    '''快速排序'''
    if first >= last:
        return

    # mid_value = alist[0] # 中间值
    mid_value = alist[first] # 中间值
    # n = len(alist)
    # 左右游标
    # low = 0
    low = first
    # high = n-1
    high = last

    while low < high:
        # high 游标 左移动
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        # low += 1

        # low 游标 右移动
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        # high -= 1

        # 等于的情况放到其中一边去处理
        # 为了保证二个指针不错过，注释 【low += 1】和 【high -= 1】

    # 退出循环的时候，low == high
    alist[low] = mid_value # 中间值赋值到该位置

    # 递归
    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low-1)
    # 对low右边的列表执行快速排序
    quick_sort(alist, low+1, last)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 34]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)


