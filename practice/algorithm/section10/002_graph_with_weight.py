import networkx as nx
import matplotlib.pyplot as plt

def add_vertex(graph: nx.Graph, n: int)->nx.Graph:
    for i in range(n):
        graph.add_node(i)
    return graph

def add_edge_with_weight(graph: nx.Graph, m: int)->nx.Graph:
    for i in range(m):
        a, b, w = map(int, input().split())
        graph.add_edge(a, b, weight=w, attr_name=f'{a}-{b}')
    return graph

n, m = map(int, input().split())

simple_graph = nx.Graph()
simple_graph = add_vertex(simple_graph, n)
simple_graph = add_edge_with_weight(simple_graph, m)
pos = nx.spring_layout(simple_graph)
edge_labels = {(i, j): w['weight'] for i, j, w in simple_graph.edges(data=True)}

nx.draw_networkx_edge_labels(simple_graph, pos, edge_labels=edge_labels)
nx.draw_networkx(simple_graph, pos, with_labels=True)
plt.show()
