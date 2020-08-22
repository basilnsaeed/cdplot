import networkx as nx
import matplotlib.pyplot as plt
from math import *
import itertools as itr


def draw_dag(dag):
    draw_graph(dag.nodes, dag.arcs)

def draw_mag(mag):
    draw_graph(mag.nodes, mag.directed, mag.bidirected)

def draw_graph(nodes, directed, bidirected =set()):

    G = nx.DiGraph()

    ###Add nodes
    p = len(nodes)
    map(G.add_node, nodes)
    theta = 2*pi/p
    pos = dict()
    for node in nodes:
        pos[node] = (sin(theta*node),0.5*cos(theta*node))

    ###Draw all edges white because networkx is stupid
    for edge in itr.combinations(nodes, 2):
        i,j = edge
        G.add_edge(i,j)
    nx.draw_networkx(G, pos, nodelist = nodes, edge_color = 'w', node_color = 'w', font_size = 18, arrowsize = 20)

    ###Draw edges
    reversed_bi = {(i,j) for (j,i) in bidirected}
    edges_to_draw = directed.union(bidirected).union(reversed_bi)
    nx.draw_networkx(G, pos, nodelist = nodes, edgelist = edges_to_draw, edge_color = 'k',node_color = 'w', font_size = 18, arrowsize = 20)
    plt.show()

