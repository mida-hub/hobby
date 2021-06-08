import networkx as nx
import matplotlib.pyplot as plt

def add_vertex(graph: nx.Graph, n: int)->nx.Graph:
    for i in range(n):
        graph.add_node(i)
    return graph

def add_edge(graph: nx.Graph, m: int)->nx.Graph:
    for i in range(m):
        a, b = map(int, input().split())
        graph.add_edge(a, b, attr_name=f'{a}-{b}')
    return graph

n, m = map(int, input().split())

simple_graph = nx.Graph()
simple_graph = add_vertex(simple_graph, n)
simple_graph = add_edge(simple_graph, m)

nx.draw(simple_graph, with_labels=True)
plt.show()
