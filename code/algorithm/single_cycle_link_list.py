# coding=utf-8
# single_cycle_link_list

class Node(object):
    '''节点'''
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node # 指针指向当前列表的头部

class SingleCycleLinkList(object):
    '''单链表'''
    def __init__(self, node=None):
        self.__head = node # 头节点
        if node:
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        cur = self.__head
        # count记录数量
        count = 1 # count从1开始
        while cur.next != self.__head: # cur.next == None
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem)
            cur = cur.next
        print(cur.elem)
        print('')

    def add(self, item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = node

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        pass

    def insert(self, pos, item):
        '''指定位置添加元素
            :param pos 从0开始
        '''
        pass
    def remove(self, item):
        '''删除节点'''
        pass
    def search(self, item):
        '''查找节点是否存在'''
        pass

if __name__ == '__main__':
    scll = SingleCycleLinkList()
