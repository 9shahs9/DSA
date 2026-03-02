class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True 
        return False
    
    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices (undirected)."""
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass 
            return True
        return False 

    def remove_vertex(self, v1):
        if v1 not in self.adj_list:
            return False
        
        # Remove this vertex from all neighbors' lists
        for neighbor in list(self.adj_list[v1]):
            self.adj_list[neighbor].remove(v1)
        
        del self.adj_list[v1]
        return True

    def print_graph(self):
        """Print the graph as an adjacency list."""
        print("=" * 50)
        print("Graph (Adjacency List):")
        print("=" * 50)
        for vertex in self.adj_list:
            neighbors = self.adj_list[vertex]
            if neighbors:
                print(f"{vertex} --> {neighbors}")
            else:
                print(f"{vertex} --> []")
        print("=" * 50)


# Test the graph
if __name__ == "__main__":
    g = Graph()
    
    # Add vertices
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    
    # Add edges
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    
    # Print the graph
    g.print_graph()

    g.remove_edge('C', 'A')
    g.print_graph()
