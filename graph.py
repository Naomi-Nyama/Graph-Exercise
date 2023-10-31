import heapq

# Node in a graph
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

# Weighted graph
class WeightedGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        node = Node(name)
        self.nodes[name] = node

    def add_edge(self, node1, node2, weight):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.nodes[node1].add_neighbor(node2, weight)
        self.nodes[node2].add_neighbor(node1, weight)

# finding the shortest path using Dijkstra's algorithm
class ShortestPath:
    def __init__(self, graph):
        self.graph = graph

    def find(self, start, end):
        if start not in self.graph.nodes:
            return f"Start node {start} does not exist in the graph.", None
        if end not in self.graph.nodes:
            return f"End node {end} does not exist in the graph.", None

        queue = [(0, start)]
        distances = {node: float('infinity') for node in self.graph.nodes}
        distances[start] = 0
        previous_nodes = {node: None for node in self.graph.nodes}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if distances[current_node] < current_distance:
                continue

            for neighbor, weight in self.graph.nodes[current_node].neighbors.items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        path = []
        while end is not None:
            path.append(end)
            end = previous_nodes[end]
        path = path[::-1]

        return path, distances[path[-1]]


graph = WeightedGraph()
nodes = ["Ntcheu", "Dedza", "Lilongwe", "Salima", "Dowa", "Ntchisi", "Kasungu", "Mchinji", "Nkhotakota"]
edges = [("Ntcheu", "Dedza", 74), ("Dedza", "Lilongwe", 92), ("Dedza", "Salima", 96),
         ("Salima", "Nkhotakota", 112), ("Salima", "Dowa", 67), ("Dowa", "Lilongwe", 55),
         ("Dowa", "Ntchisi", 38), ("Dowa", "Kasungu", 117), ("Ntchisi", "Nkhotakota", 66),
         ("Kasungu", "Mchinji", 141), ("Mchinji", "Lilongwe", 109)]

for node in nodes:
    graph.add_node(node)
for edge in edges:
    graph.add_edge(*edge)

shortest_path = ShortestPath(graph)
path, distance = shortest_path.find("Ntcheu", "Kasungu")
print(f"The shortest path and distance from Ntcheu to Kasungu is:")
print(f"Shortest path: {path}")
print(f"Distance: {distance}")
