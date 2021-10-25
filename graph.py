# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def empty(self):
#         return len(self.items) == 0
#
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def dequeue(self):
#         if self.empty():
#             raise Exception("Queue: 'dequeue' applied to empty container")
#         return self.items.pop(0)
#
#     def __len__(self):
#         return len(self.items)
#
#
# class Vertex:
#     def __init__(self, vertexId):
#         self.mId = vertexId # Ідентифікатор вершини
#         self.mData = None # Навантаження (дані) вершин
#
#     def getId(self):
#         "Отримати ідентифікатор вершини"
#         return self.mId
#
#     def setData(self, aData):
#         "Встановити навантаження на вершину"
#         self.mData = aData
#
#     def getData(self):
#         "Отримати навантаження на вершину"
#         return self.mData
#
#     def __str__(self):
#         "Зображення вершини у вигляді рядка"
#         return str(self.mId) + ": Data=" + str(self.getData())
#
#
# class GraphVertex(Vertex):
#     def __init__(self, vertexId):
#         super().__init__(vertexId) # Викликаємо конструктор батьківського класу
#         self.mNeighbors = {} # Список сусідів вершини у вигляді пар
#         # (ім'я_сусіда: вага_ребра)
#
#     def addNeighbor(self, aVertex, aWeight=1):
#         """Додати сусіда, тобто ребро, що сполучає
#         поточну вершину з вершиною aVertex з вагою aWeight """
#         if isinstance(aVertex, Vertex): # Якщо aVertex - вершина
#             self.mNeighbors[aVertex.getId()] = aWeight
#         else: # Якщо aVertex - ім'я (ключ) вершини
#             self.mNeighbors[aVertex] = aWeight
#
#     def getNeighbors(self):
#         """Повернути список всіх сусідів поточної вершини"""
#         return self.mNeighbors
#
#     def getWeight(self, aNeighbor):
#         "Отримати вагу ребра, що сполучає поточну вершину сусідом aNeighbor"
#         if isinstance(aNeighbor, Vertex): # Якщо aNeighbor - вершина (не ім'я)
#             return self.mNeighbors[aNeighbor.getId()]
#         else: # Якщо aNeighbor - ім'я (ключ) сусідньої вершини
#             return self.mNeighbors[aNeighbor]
#
#     def __str__(self):
#         "Зображення вершини у вигляді рядка у разом з усіма її сусідами"
#         return super().__str__() + ' connected to: ' + str(self.mNeighbors)
#
#
# class Graph:
#     """ Граф, що задається списком суміжних вершин """
#     def __init__(self, isOriented=False):
#         self.mIsOriented = isOriented # Поле чи орієнтований граф
#         self.mVertexNumber = 0 # Лічильник вершин у графі
#         self.mVertices = {} # Список (словник) вершин у графі у вигляді пар (ключ, вершина)
#
#     def addVertex(self, aVertex):
#         """ Додає вершину у граф, якщо така вершина не міститься у ньому """
#         if aVertex in self: # Якщо вершина міститься у графі, її вже не треба додавати
#             return False
#         if not isinstance(aVertex, GraphVertex): # Якщо aVertex - вершина (не ім'я)
#             newVertex = GraphVertex(aVertex) # створюємо нову вершину з іменем aVertex
#             self.mVertices[aVertex] = newVertex # додаємо цю вершину до списку вершин графу
#         else: # Якщо aVertex - ім'я ключ вершини
#             self.mVertices[aVertex.getId()] = aVertex # додаємо цю вершину до списку вершин графу
#         self.mVertexNumber += 1 # Збільшуємо лічильник вершин у графі
#         return True
#
#     def getVertex(self, aVertex):
#         "Повертає вершину графу, якщо така вершина міститься у графі"
#         assert aVertex in self
#         # Визначаємо ключ вершини
#         key = aVertex.getId() if isinstance(aVertex, GraphVertex) else aVertex
#         return self.mVertices[key]
#
#     def getVertices(self):
#         "Повертає список всіх вершин у графі"
#         return self.mVertices
#
#     def addEdge(self, fromVert, toVert, weight=1):
#         "Додавання ребра з кінцями в точках fromVert та toVert з вагою weight"
#         if fromVert not in self: # якщо вершина fromVert ще не міститься у графі
#             self.addVertex(fromVert) # Додаємо її
#         if toVert not in self: # якщо вершина toVert ще не міститься у графі
#             self.addVertex(toVert) # Додаємо її
#         # встановлюємо зв'язок (тобто ребро) між вершинами fromVert та toVert
#         self[fromVert].addNeighbor(toVert, weight)
#         if not self.mIsOriented: # Якщо граф не орієнтований, то треба додати зворотній зв'язок
#             self.mVertices[toVert].addNeighbor(fromVert, weight)
#
#     def setVertexData(self, aVertex, aData):
#         "Встановлення навантаження aData на вершину з іменем aVertex"
#         assert aVertex in self # Перевірка чи міститься вершина в графі
#         self[aVertex].setData(aData)
#
#     def getVertexData(self, aVertex):
#         "Повернення навантаження вершини з іменем aVertex"
#         assert aVertex in self # Перевірка чи міститься вершина в графі
#         return self[aVertex].getData()
#
#     def getWay(self, fromVert, toVert):
#         verts = []
#
#     def __contains__(self, aVertex):
#         "Перевірка чи міститься вершина з іменем vertex у графі"
#         if isinstance(aVertex, GraphVertex): # Якщо aVertex - вершина (не ім'я)
#             return aVertex.getId() in self.mVertices
#         else: # Якщо aVertex - ім'я (ключ) вершини
#             return aVertex in self.mVertices
#
#     def __iter__(self):
#         "Ітератор для послідовного проходження всіх вершин у графі"
#         return iter(self.mVertices.values())
#
#     def __len__(self):
#         "Перевизначення методу len() як кількість вершин у графі"
#         return self.mVertexNumber
#
#     def __str__(self):
#         "Зображення графа разом з усіма вершинами і ребрами у вигляді рядка"
#         s = ""
#         for vertex in self:
#             s += str(vertex) + "\n"
#         return s
#
#     def __getitem__(self, vertex):
#         return self.getVertex(vertex)
#
# def DFS(graph, start, finish):
#     frontier = Queue()
#     frontier.enqueue(start)
#     came_from = {}
#     came_from[start] = None
#
#     while not frontier.empty():
#         current = frontier.dequeue()
#         for next in graph[current].getNeighbors():
#             if next not in came_from:
#                 frontier.enqueue(next)
#                 came_from[next] = current
#                 if next == finish:
#                     return came_from
#
#
# s = 'abc'
#
# g = Graph(isOriented=True)
# g.addVertex(0)
# g.addVertex(1)
# g.addVertex(2)
# g.addVertex(3)
# g.addVertex(4)
# g.addEdge(0, 2, 'a')
# g.addEdge(2, 3, 'b')
# g.addEdge(3, 4, 'c')
# g.addEdge(0, 1, 'd')
# print(g)
#
# print(DFS(g, 0, 4))


class Graph:
    def __init__(self, isOriented=False, aInitialVertexNumber=20):
        self.mIsOriented = isOriented
        self.mVertexNumber = aInitialVertexNumber
        self.mAdjacentMatrix = []
        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)

    def addEdge(self, fromVert, toVert, weight=1):
        "Додавання ребра з кінцями в точках fromVert та toVert з вагою weight"
        assert 0 <= fromVert < self.mVertexNumber
        assert 0 <= toVert < self.mVertexNumber
        self.mAdjacentMatrix[fromVert][toVert] = weight
        if not self.mIsOriented:
            self.mAdjacentMatrix[toVert][fromVert] = weight

    def findPath(self, s, path = []):
        if len(s) == 0:
            if path[0][0] == path[-1][1]:
                return None
            return path

        n = len(self.mAdjacentMatrix)
        for i in range(n):
            for j in range(n):
                if self.mAdjacentMatrix[i][j] == s[0]:
                    if len(path) > 0:
                        if i != path[-1][1]:
                            continue
                    path.append((i, j))
                    return self.findPath(s[1:], path[:])

        return None

    def addByTask(self, s):
        fromVert, toVert, el = s.split()
        self.addEdge(int(fromVert), int(toVert), el)


def task(g, s):
    path = g.findPath(s)
    if path is not None:
        print('YES', str(path[0][0]) + ' ' + str(path[-1][1]), sep='\n')
    else:
        print('NO')

if __name__ == '__main__':
    s = input()
    n = int(input())
    if n < 2:
        print('NO')
    else:
        g = Graph(aInitialVertexNumber=n+1)
        for i in range(n-1):
            g.addByTask(input())

        task(g, s)


