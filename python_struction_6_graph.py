inf = float("inf")

class GraphError(ValueError):
    pass


# 邻接矩阵的实现
class Graph:
    def __init__(self, mat, unconn=1):
        #  unconn服务于在构造图对象的时候可以通过参数为无关连的情况提供一个特殊值
        #  主要参数mat，表示出事的邻接矩阵，要求其是一个二维的表参数，
        #  提供图的基本构架，主要确定定点个数
        #  先确定是否合法，检测给定矩阵是否为方阵
        vnum = len(mat)
        # vnum:端点数
        for x in mat:
            if len(x) != vnum:
        #         check if it is square
                raise ValueError("Argument for 'Graph'")
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v > self._vnum

    def add_vertex(self):
        raise GraphError("Adj_Matrix does nnot support 'add_vertex'")

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             "is not a valid vertex.")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             "is not a valid vertex.")
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi)+ "is not a valid vertex.")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return "{\n" + ",\n".join(map(str, self._mat)) + "\n}" \
                + "\nUnconnected: " + str(self._unconn)

# 邻接表实现
# 每个顶点v的所有邻接边用一个list对象表示，
# 元素形式为（边的终点， 权重）
class GraphAL(Graph):
    def __init__(self, mat=[], unconn = 0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("Argument for GraphAL")
            self._mat = [Graph._out_edges(mat[i], unconn)
                         for i in range(vnum)]
            self._vnum = vnum
            self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("Cannot add edge to empty graph")
        if self._invalid(vi) or self._invalid(vj) :
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             "is not a valid vertex.")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] == (vj, val)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))


    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             "is not a valid vertex.")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex.")
        return self._mat[vi]


class StackUnderFlow(ValueError):
    pass
    # 栈下溢

# 利用list写stack
class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderFlow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderFlow("in SStack pop()")
        return self._elems.pop()

# 深度优先非递归算法
def DFS_graph(graph, v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum
    visited[v0] = 1
    DFS_seq = [v0]
#     visited记录访问过的点， DFS_Seq记录访问过的序列
    st = SStack()
#     利用一个栈作为辅助数据结构
    st.push((0, graph.out_edges(v0)))       # 入栈
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i+1, edges))
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return DFS_seq
# 入栈元素为（i, edges),其中edges是某个顶点的边表，i是边表下标记



# 递归生成树算法
def DFS_span_forest(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * vnum

    def dfs(graph, v):      #   递归遍历函数， 在递归中记录经由边
        nonlocal span_forest    #   span_forest is nonloacal
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)

    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)

    return span_forest

# 最小生成树算法
# Kruskal算法
def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    #         w 表示权值， vi，vj表示端点
    edges.sort()
    # use sort to find the min edge
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi, vj, w))
            if len(mst) == vnum -1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst

#  Prim算法
# 基于最小生成树性质
# 优先队列
class PrioQueueError(ValueError):
    pass

class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse = True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()

def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None] * vnum
    cands = PrioQue([(0, 0, 0)])
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w, v, vi))
    return mst



if __name__ == "__main__":
    print("start to build a graph")
    mat = [[0,0,1], [1, 0, 1], [0, 1, 0]]
    g = Graph(mat)
    print(g.vertex_num())
    g.add_edge(1, 2, 3)
    print(str(g))
    g_al = GraphAL(mat)
    print(str(g_al))

    span_forest = DFS_span_forest(g_al)
    print(span_forest)

    print("MST",Kruskal(g_al))
    print(Prim(g_al))