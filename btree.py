from itertools import permutations

def DFS(tree, s = ''):
    if tree.getLeft() is not None:
        s += '<'
        s = DFS(tree.getLeft(), s)
    s += '|'
    if tree.getRight() is not None:
        s += '>'
        s = DFS(tree.getRight(), s)
    return s



class BinaryTree:
    def __init__(self, item = None):
        self.mItem = item
        self.mLeftNode = None
        self.mRightNode = None

    def setItem(self, item):
        self.mItem = item

    def getItem(self):
        return self.mItem

    def setLeft(self, node):
        self.mLeftNode = node

    def setRight(self, node):
        self.mRightNode = node

    def getLeft(self):
        return self.mLeftNode

    def getRight(self):
        return self.mRightNode

    def getLeftItem(self):
        assert self.getLeft() is not None
        return self.mLeftNode.getItem()

    def getRightItem(self):
        assert self.getRight() is not None
        return self.mRightNode.getItem()

    def __str__(self):
        return str(self.getItem())

    def add(self, item):
        if self.getItem() is None:
            self.setItem(item)

        if item < self.getItem():
            if self.getLeft() is None:
                self.setLeft(BinaryTree(item))
            else:
                self.getLeft().add(item)
        elif item > self.getItem():
            if self.getRight() is None:
                self.setRight(BinaryTree(item))
            else:
                self.getRight().add(item)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ai = map(int, input().split())
    k = 0 # лічільник

    baseTree = BinaryTree()
    for el in ai:
        baseTree.add(el)
    baseStr = DFS(baseTree)

    vals = list(range(1, m + 1))
    perms = list(permutations(vals, n))
    for p in perms:
        tree = BinaryTree()
        for el in p:
            tree.add(el)
        if DFS(tree) == baseStr:
            k += 1

    print(k)
