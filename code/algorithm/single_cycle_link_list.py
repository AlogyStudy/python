# coding=utf-8
# single_cycle_link_list

class Node(object):
    '''节点'''
    def __init__(self, node):
        self.elem = node
        self.next = None

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
            cur = cur.next
            print(cur.elem, end=' ')
        # print(cur.elem, '-------')
        # print('')

    def add(self, item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        if self.is_empty():
            # 如果为空，指向节点，然后节点的指针指向自己
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            # 指针先移动到尾端
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            # 改变指针指向
            node.next = self.__head
            self.__head = node
            # cur.next = node
            cur.next = node

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素
            :param pos 从0开始
        '''
        if pos < 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        '''
            1. 头节点
            2. 尾节点
            3. 中间节点
            4. 只存在一个节点
            5. 空链表
            6. 首节点就是删除的节点
        '''
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    # 头节点的情况
                    # 找到尾节点
                    rear = self.__head
                    # 为了顺利把尾节点的指针指向到头节点，先把指针便利到尾部
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                # 两个游标顺次往链表后边移动
                pre = cur
                cur = cur.next
        # 尾部情况
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if self.__head == cur:
                # 只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点        
        if cur.elem == item:
            return True
        return False

if __name__ == '__main__':
    scll = SingleCycleLinkList()
    print('is_empty', scll.is_empty())
    print('length', scll.length())

    scll.append(100)
    print('is_empty', scll.is_empty())
    print('length', scll.length())

    scll.append(22)
    scll.add(7)
    scll.append(20)
    scll.insert(2, 777)

    scll.travel()
    scll.remove(7)
    scll.travel()
