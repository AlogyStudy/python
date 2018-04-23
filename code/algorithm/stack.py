#coding=utf-8


class Stack(object):
    '''栈'''
    def __init__(self):
        self.__list = []

    def push(self, item):
        '''添加一个新的元素item到栈顶'''
        self.__list.append(item)
        # 确定是尾部还是头部插入数据
        # 选择在尾部添加，而非头部插入，顺序表对于尾部操作的时间复杂度是O(1)
        # self.__list.insert(0, item)
    def pop(self):
        '''弹出栈顶元素'''
        return self.__list.pop()
        # self.__list.pop(0)

    def size(self):
        '''返回栈的元素个数'''
        return len(self.__list)

    def is_empty(self):
        '''判断栈是否为空'''
        # '', 0, {}, [], ()
        return self.__list == []

    def peek(self):
        '''返回栈顶元素'''
        if self.__list:
            return self.__list[-1]
        else:
            return None

if __name__ == '__main__':
    stack = Stack()

    stack.push(11)
    stack.push(1000)
    print(stack.size(), 'stack.size()')
    print(stack.pop(), 'stack.pop()')
