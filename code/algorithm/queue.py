#coding=utf-8


class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        '''往队列中添加一个item元素'''
        self.__list.append(item) # 尾部插入
        # self.__list.insert(0, item) # 头部插入

    def dequeue(self):
        '''从队列头部删除一个元素'''
        return self.__list.pop(0) # 尾部删除
        # return self.__list.pop() # 头部删除

    def is_empty(self):
        '''判断一个队列是否为空'''
        return not self.__list

    def size(self):
        '''返回队列的大小'''
        return len(self.__list)

if __name__ == '__main__':

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(13)

    print(queue.size())
    print(queue.dequeue())
