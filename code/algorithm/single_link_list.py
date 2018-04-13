# coding=utf-8
# single_link_list

class Node(object):
    '''节点'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# node = Node(100) # 保存  elem, next

class SingleLinkList(object):
    '''单链表'''
    def __init__(self, node=None):
        self.__head = node # 头节点
    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        # 游标, 指针
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None: # cur.next == None
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next

    def add(self, item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        node.next = self.__head # 保证链表中的所有关系不打断
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        # item 数据元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:     
            cur = self.__head
            while cur.next != None: # 从头往后走，然后最后挂载一个新的游标
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素
            :param pos 从0开始
        '''
        if pos < 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head # pre, prior
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node
    def remove(self, item):
        '''删除节点'''
        pass
    def search(self, item):
        '''查找节点是否存在'''
        pass

if __name__ == '__main__':
    sll = SingleLinkList()
    print('is_empty', sll.is_empty())
    print('length', sll.length())
    sll.append(100)
    print('is_empty', sll.is_empty())
    print('length', sll.length())

    sll.append(22)
    sll.add(7)
    sll.append(20)
    sll.insert(2, 777)


    sll.travel()