#coding=utf-8

class Dqueue(object):
    '''双端队列'''
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        '''添加一个新的元素item到栈顶'''
        self.__list.append(0, item) # 头部添加

    def add_rear(self, item):
        self.__list.append(item) # 尾部添加

    def pop_fornt(self):
        return self.__list.pop(0)
    
    def pop_rear(self):
        return self.__list.pop()

    def size(self):
        '''返回栈的元素个数'''
        return len(self.__list)

    def is_empty(self):
        '''判断栈是否为空'''
        # '', 0, {}, [], ()
        return self.__list == []

if __name__ == '__main__':
    dq = Dqueue()

    dq.add_front(11)
    dq.add_front(100)
    dq.add_rear(1000)
    print(dq.size(), 'dq.size()')
    print(dq.pop_fornt(), 'dq.pop_fornt()')
