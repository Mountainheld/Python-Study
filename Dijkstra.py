import sys
import heapq

class Edge(object):
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node(object):
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.adjacencies_list = []
        self.min_distance = sys.maxsize

    def __cmp__(self, other_vertex):
        return self.cmp(self.min_distance, other_vertex.min_distance)

    def __lt__(self, other):
        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority

class Algorithm(object):

    def calculate_shortest_path(self, vertex_list, start_vertex):
        heap = []
        start_vertex.min_distance = 0
        heapq.heappush(heap, start_vertex)

        while heap:
            actual_vertex = heapq.heappop(heap)

            for edge in actual_vertex.adjacencies_list:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight

                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(heap, v)

    def get_shortest_path_to(self, target_vertex):
        print("Shortest path to vertex is: ", target_vertex.min_distance)

        node = target_vertex

        while node is not None:
            print("%s " % node.name)
            node = node.predecessor

    
if __name__ == "__main__":

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    node1.adjacencies_list.append(edge1)
    node1.adjacencies_list.append(edge2)
    node1.adjacencies_list.append(edge3)
    node2.adjacencies_list.append(edge4)
    node2.adjacencies_list.append(edge5)
    node2.adjacencies_list.append(edge6)
    node8.adjacencies_list.append(edge7)
    node8.adjacencies_list.append(edge8)
    node5.adjacencies_list.append(edge9)
    node5.adjacencies_list.append(edge10)
    node5.adjacencies_list.append(edge11)
    node6.adjacencies_list.append(edge12)
    node6.adjacencies_list.append(edge13)
    node3.adjacencies_list.append(edge14)
    node3.adjacencies_list.append(edge15)
    node4.adjacencies_list.append(edge16)

    vertex_list = (node1, node2, node3, node4, node5, node6, node7, node8)

    thm = Algorithm()
    thm.calculate_shortest_path(vertex_list, node1)
    
    thm.get_shortest_path_to(node4)