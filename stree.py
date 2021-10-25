class SegmentTree:
    def __init__(self):
        n = 256
        self.mItems = 2 * n * [0]
        self.mSize = n

    def update(self, pos):
        pos += self.mSize
        i = pos // 2
        while i > 0:
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]
            i = i >> 1

    def add(self, pos, x):
        pos += self.mSize
        self.mItems[pos] += x
        i = pos // 2
        while i > 0:
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]
            i = i >> 1

    def sum(self, left, right):
        left += self.mSize
        right += self.mSize
        res = 0
        while left <= right:
            if left % 2 == 1:
                res += self.mItems[left]
            if right % 2 == 0:
                res += self.mItems[right]
            left = (left + 1) >> 1
            right = (right - 1) >> 1
        return res

    def Add(self, L, R, value):
        while L <= R:
            self.add(L, value)
            L += 1

    def Get(self, L, R):
        return self.sum(L, R)


if __name__ == '__main__':
    q, L, R, p = map(int, input().split())
    tree = SegmentTree()
    for _ in range(q):
        tree.Add(L, R, 1)
        Lnew = tree.Get(min(L, R), max(L, R)) % p
        Rnew = 255 - Lnew
        L = Lnew
        R = Rnew
    print(tree.Get(0, 255))
