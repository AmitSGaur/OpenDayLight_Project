from collections import defaultdict
import json
import datetime

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


class DFS:


    def __init__(self, node,edges):
        self.node = node
        self.edges = edges
        self.color=['W' for i in range(0,node)] # W for White
        self.graph =color=[[False for i in range(0,node)] for j in range(0,node)]
        self.parent =[-1 for u in range(0,node)]

        # Start DFS
        self.construct_graph()
        self.dfs_traversal()

    def construct_graph(self):
        for u,v in self.edges:
            self.graph[u][v], self.graph[v][u] = True, True

    def dfs_visit(self, u):
        self.color[u]='G' # G for Gray
        for i in range(0, self.node):
            if self.graph[u][i]==True and self.color[i]=='W':
                self.parent[i]=u
                self.dfs_visit(i)
        self.color[u]='B' # B for black

    def dfs_traversal(self):
        for i in range(0,self.node):
            if self.color[i]=='W': # W for white
                self.dfs_visit(i)

    def print_path(self, source, destination):
        if destination==source:
            print destination,
        elif self.parent[destination] == -1:
            print "No Path"
        else:
            self.print_path(source, self.parent[destination])
            print "-> ",destination,
			
			

g1 = Graph()
g2 = Graph()

json_data = open('edges').read()
data = json.loads(json_data)
node_list=tuple(open('node','r'))
datetime.datetime.now()

#while node in node_list:
#try:
for node in node_list:
    node=node.rstrip('\n')
    node1=node[22]
    #print 'aaabbb'
    g1.add_node(node1)
#       break
#except ValueError:
#print('hi sailee')

json_data=open('edges').read()

data = json.loads(json_data)

edges = data['edgeProperties']

for fs in edges:
    #print fs['edge']['tailNodeConnector']['node']['id'],':',fs['edge']['tailNodeConnector']['id'], 'to', fs['edge']['headNodeConnector']['node']['id'],':',fs['edge']['headNodeConnector']['id']
    tailnode=fs['edge']['tailNodeConnector']['node']['id']
    headnode=fs['edge']['headNodeConnector']['node']['id']
    tailnode=int(tailnode[22])
    headnode=int(headnode[22])

    print headnode,'to',tailnode
    g1.add_edge(headnode,tailnode,1)
    g1.add_edge(tailnode,headnode,1)

path1 = {}

start = raw_input('Enter start node :')
start = start.rstrip('\n')
start = int(start)

home = raw_input('Enter dest node :')
home = home.rstrip('\n')
home = int(home)

g2.add_node(1);
g2.add_node(2);
g2.add_node(3);
g2.add_node(4);
g2.add_node(5);
g2.add_node(6);

g2.add_edge(1,2,1)
g2.add_edge(2,1,1)
g2.add_edge(3,1,1)
g2.add_edge(1,3,1)
g2.add_edge(4,1,1)
g2.add_edge(1,4,1)
g2.add_edge(2,4,1)
g2.add_edge(4,2,1)
g2.add_edge(4,5,1)
g2.add_edge(5,4,1)
g2.add_edge(6,5,1)
g2.add_edge(5,6,1)

#print g2.edges
print "-----------------------------------------------"
print g1.edges
print "-----------------------------------------------"
ret = dijsktra(g2,1)
#print ret
path1=ret[1]
print "-----------------------------------------------"
print path1

print "-----------------------------------------------"
#while home != start:
#    home = path1[home]
#    print home

print "done"

node = 8 # 8 nodes from 0 to 7
edges =[(0,1),(0,3),(1,2),(1,5),(2,7),(3,4),(3,6),(4,5),(5,7)] # bi-directional edge

dfs = DFS(node, edges)
dfs.print_path(0, 7)
print ""
dfs.print_path(2, 5)
print ""
dfs.print_path(0, 4)