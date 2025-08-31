from collections import defaultdict
from collections import deque
class graph:
    def __init__(self,directed):
        self.adj=defaultdict(list)
        self.vertices=set() # this is empty initially, set wount add 2,3 times uniqu
        self.directed=directed
    def add_vertex(self,vertex):
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            if vertex not in self.adj:
                self.adj[vertex]=[] # to give empty small lists
            print(f"vertex '{vertex}' added.")
        else:
            print(f"vertex '{vertex}' already exist")
    def add_edge(self,u,v,wt): 
        self.add_vertex(u)
        self.add_vertex(v) # before adding edge, making sure vertex are exist.
        if [v,wt] not in self.adj[u]:
            self.adj[u].append([v,wt])
            print(f" edge added: {u} -> {v} ")
        if not self.directed:
            if [u,wt] not in self.adj[v]:
                self.adj[v].append([u,wt])
                print(f"edge added: {v}->{u}")
    def display(self):
        if not self.vertices:
            print("graph is empty")
            return
        sorted_vertices=sorted(list(self.vertices)) #  to display good
        for vertex in sorted_vertices:
            neighbors=sorted(self.adj.get(vertex,[]))
            print(f"{vertex}:{neighbors}")
    def remove_vertex(self,vertex):
        if vertex not in self.vertices:
            print(f"vertex {vertex} not found in the graph")
            return
        self.vertices.remove(vertex)
        print(f" vertex {vertex} removed ")
        if vertex in self.adj: #removing all edges in that index
            del self.adj[vertex]
            print(f"adjacency list entry for {vertex} cleared.")
        for i in range(len(self.vertices)):
            if i == vertex:
                continue
            self.adj[i][:]=[[neighbor,wt] for neighbor,wt in self.adj[i] if neighbor !=vertex]
        print(f" vertex {vertex} and its edges removed")
    def remove_edge(self,u,v,wt):
        if u not in self.vertices or v not in self.vertices:
            print(f"connot remove edge: vertex {u} and {v} and not exist")
            return
        edge_removed=False
        if [v,wt] in self.adj[u]:
            self.adj[u].remove([v,wt])
            print(f" edge removed : {u}-> {v}")
            edge_removed=True
        else:
            print(f"edge {u}->{v} not found")
        if not self.directed:
            if [u,wt] in self.adj[v]:
                self.adj[v].remove([u,wt])
                print(f"edge removed : {v}->{u} for undirected.")
                edge_removed=True
            elif edge_removed:
                print(f"Note: for undirected removal,{v}->{u} was not found(already removed or never existed)")
        else:
            print(f"edge {v} -> {u} not found (for directed)")

my_graph=graph(False)
my_graph.add_edge(0,1,10)
my_graph.add_edge(2,0,20)
my_graph.add_edge(1,3,20)
my_graph.add_edge(2,3,40)
my_graph.add_edge(1,4,50)
my_graph.add_edge(3,4,70)
my_graph.add_edge(4,5,90)


my_graph.add_vertex(6)

my_graph.display()
my_graph.remove_vertex(2)
my_graph.remove_edge(1,0,10)
my_graph.display()