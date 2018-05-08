#conding=utf-8

def merge_sort(alist):
    '''归并排序'''

    '''
        分裂
    '''
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    
    '''
        合并
    '''
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 34]
    print(li)
    newLi = merge_sort(li)
    print(newLi)
    print(li)


'''
代码中不太清晰看见 时间复杂度的算法（一般情况下有递归调用），而分析整个过程

n * x
n * logn

时间上是其它排序算法上最小的，但是需要另外申请一块内存存储新的列表（空间上的利用，时间上的优化）
'''