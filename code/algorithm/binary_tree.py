#coding=utf-8

class Node(object):
    '''节点类'''
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    '''二叉树'''
    def __init__(self):
        self.root = None        

    # 插入 （广度优先遍历）
    def add (self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue: # 不为空列表
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    def breadth_travel(self):
        '''广度遍历'''
        '''层次遍历'''
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def preorder(self, node): # 中序，先序，后序，根节点都在变化，为了调用自身，而且是调用不同的子树，所以根节点作为参数传入
        '''先序遍历'''
        if node is None:
            return
        print(node.elem, end=' ') # 根
        self.preorder(node.lchild) # 左边
        self.preorder(node.rchild) # 右边

    def inorder(self, node):
        '''中序遍历'''
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=' ')
        self.inorder(node.rchild)
    
    def postorder(self, node):
        '''后序遍历'''
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=' ')

if __name__ == '__main__':
    tree = Tree()

    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(' ')
    tree.preorder(tree.root)
    print(' ')
    tree.inorder(tree.root)
    print(' ')
    tree.postorder(tree.root)
    print(' ')
