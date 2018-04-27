#condig-utf8

def bubble_sort(alist):
    '''冒泡排序'''
    n = len(alist)

    # 走多少次
    # 从头走到尾

    for j in range(n - 1):
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i+1]:
                # 位置调换
                alist[i], alist[i+1] = alist[i+1], alist[i]


    # i 0 ~ n-2  range(0, n-1) j=0
    # i 1 ~ n-3  range(0, n-1-1) j=1
    # i 2 ~ n-4  range(0, n-1-1-1) j=2
    # j=n i range(0, n-1-j)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 34]
    bubble_sort(li)
    print(li)
