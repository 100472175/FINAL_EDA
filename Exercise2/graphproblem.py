# Eduardo Alarcón (1000472175)
import copy


def compare_lists(list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        return False
    # we compare both list of vertices
    for a, b in zip(list1, list2):
        # print(str(a), str(b))
        if a != b:
            return False
    return True


class MyGraph:
    """Implementation of an undirected and unweighted graph"""

    def __init__(self, lst_vertices: list) -> None:
        """We use a dictionary to save the vertices"""
        self._vertices = {}
        for vertex in lst_vertices:
            # Each vertex is a key of the dictionary
            # Its associated value will be the list of its adjacent vertices
            self._vertices[vertex] = []

    def check_vertex(self, vertex: str) -> bool:
        """checks if the vertex exists in the graph"""
        return vertex in self._vertices

    def add_edge(self, v1: str, v2: str) -> None:
        if not self.check_vertex(v1):
            print(v1, " is not a vertex!!!")
            return
        if not self.check_vertex(v2):
            print(v2, " is not a vertex!!!")
            return
        if v1 == v2:
            print("({},{}) loops edges are not allowed!".format(v1, v2))
            return
        if v2 in self._vertices[v1] or v1 in self._vertices[v2]:
            print("({},{}) multiple edges are not allowed!".format(v1, v2))
            return

        self._vertices[v1].append(v2)
        self._vertices[v2].append(v1)

    def remove_edge(self, v1: str, v2: str) -> None:
        if not self.check_vertex(v1):
            print(v1, " is not a vertex!!!")
            return
        if not self.check_vertex(v2):
            print(v2, " is not a vertex!!!")
            return
        if v1 == v2:
            print("({},{}) loops edges are not allowed!".format(v1, v2))
            return
        if v2 not in self._vertices[v1] or v1 not in self._vertices[v2]:
            print("({},{}) multiple edges are not allowed!".format(v1, v2))
            return

        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)

    def __eq__(self, other: 'MyGraph') -> bool:
        if other is None:
            return False

        self_keys = sorted(list(self._vertices.keys()))
        other_keys = sorted(list(other._vertices.keys()))

        if not compare_lists(self_keys, other_keys):
            return False

        # print(len(self_keys), len(other_keys))

        for vertex in self._vertices.keys():
            if not compare_lists(sorted(self._vertices[vertex]), sorted(other._vertices[vertex])):
                return False

        return True

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for vertex in self._vertices:
            result += '\n' + str(vertex) + ': '
            for adj in self._vertices[vertex]:
                result += str(adj) + ", "
            if result.endswith(", "):
                result = result[:-2]
        return result

    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        for vertex in self._vertices.keys():
            visited[vertex] = False

        for vert in self._vertices.keys():
            if not visited[vert]:
                self._bfs(vert, visited)
            if False in visited.values():
                return False
        return True

    # Function to do a BFS of graph
    def _bfs(self, vertex, visited):
        # This function does the BFS traversal of a graph
        queue = [vertex]
        visited[vertex] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for adj in self._vertices[s]:
                if not visited[adj]:
                    queue.append(adj)
                    visited[adj] = True

    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 is None or v2 is None:
            return False
        if v1 == v2:
            return False
        if v1 not in self._vertices or v2 not in self._vertices:
            return False
        if v1 not in self._vertices[v2] or v2 not in self._vertices[v1]:
            return False

        # There are two ways of approaching this final step of the algorithm:
        # 1. We can create a copy of the graph and remove the edge and check if the copied graph is connected
        #    This is more efficient as we do not need to add the edge back again
        # 2. We can use the original graph and remove the edge and check if the original graph is connected and
        #    add the edge back to the original graph
        # First option is faster, but it is not always possible to create a copy of the graph, as it might be a database
        # or a file and memory is finite.
        # Second option is slower, but it is always possible to delete the edge and then adding it back, which is
        # slower but consumes double the memory
        # As asked in the exam, we will use the more temporal efficient algorithm

        # First approach (temporal efficient, takes less time):
        cp = copy.deepcopy(self)

        cp.remove_edge(v1, v2)
        a = cp.is_connected()
        if a:
            return False
        else:
            return True

        # Second approach (spacial efficient, consumes less memory)
        # We remove the edge v1-v2 from the original graph
        """self.remove_edge(v1, v2)

        # Using the function previously defined, we check if the graph is connected
        # If cp.is_connected is True, then v1-v2 is not a bridge, as there is still a path
        if self.is_connected():
            self.add_edge(v1, v2)
            return False
        # If it is False, meaning there is no path from v1 to v2, then v1-v2 is a bridge
        else:
            self.add_edge(v1, v2)
            return True"""


if __name__ == '__main__':
    # Create a graph: A<->B<->C<->D
    vertices = ['A', 'B', 'C', 'D']
    g = MyGraph(vertices)
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    print("First graph: ", str(g))
    print()
    print("is_connected()={}\n".format(g.is_connected()))  # True
    # assert g.is_connected()

    u, v = 'A', 'B'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'B', 'A'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'A', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'A', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'B', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'C', 'B'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'B', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'C', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'D', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    # second graph
    print('Second graph:')
    vertices = ['A', 'B', 'C', 'D', 'E']
    g = MyGraph(vertices)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('A', 'D')
    g.add_edge('D', 'E')
    print(g)

    print("is_connected()={}\n".format(g.is_connected()))  # True
    #  assert g.is_connected()

    u, v = 'A', 'B'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'A', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'B', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'A', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'D', 'A'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'D', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'E', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'B', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'A', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    print('Third graph:')
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    g3 = MyGraph(vertices)
    g3.add_edge('A', 'B')
    g3.add_edge('B', 'C')
    g3.add_edge('C', 'D')
    g3.add_edge('C', 'E')
    g3.add_edge('D', 'E')
    g3.add_edge('D', 'F')
    g3.add_edge('D', 'G')
    g3.add_edge('E', 'F')
    print(g3)

    u, v = 'A', 'B'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # assert g3.is_bridge(u, v)

    u, v = 'B', 'A'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # assert g3.is_bridge(u, v)

    u, v = 'B', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # assert g3.is_bridge(u, v)

    u, v = 'D', 'G'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # assert g3.is_bridge(u, v)

    u, v = 'C', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # assert not g3.is_bridge(u, v)

    u, v = 'D', 'F'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # assert not g3.is_bridge(u, v)

    u, v = 'D', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # assert not g3.is_bridge(u, v)

    u, v = 'C', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # assert not g3.is_bridge(u, v)
