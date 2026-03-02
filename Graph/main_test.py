import pytest
from io import StringIO
import sys
from main import Graph


class TestGraphInit:
    """Test cases for Graph initialization."""
    
    def test_graph_init(self):
        """Test graph initialization creates empty adjacency list."""
        g = Graph()
        assert g.adj_list == {}
        assert isinstance(g.adj_list, dict)


class TestAddVertex:
    """Test cases for add_vertex method."""
    
    def test_add_single_vertex(self):
        """Test adding a single vertex to the graph."""
        g = Graph()
        result = g.add_vertex('A')
        assert result is True
        assert 'A' in g.adj_list
        assert g.adj_list['A'] == []
    
    def test_add_multiple_vertices(self):
        """Test adding multiple vertices."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        
        assert len(g.adj_list) == 3
        assert 'A' in g.adj_list
        assert 'B' in g.adj_list
        assert 'C' in g.adj_list
    
    def test_add_duplicate_vertex(self):
        """Test that adding duplicate vertex returns False."""
        g = Graph()
        result1 = g.add_vertex('A')
        result2 = g.add_vertex('A')
        
        assert result1 is True
        assert result2 is False
        assert len(g.adj_list) == 1
    
    def test_add_vertex_different_types(self):
        """Test adding vertices with different data types."""
        g = Graph()
        g.add_vertex(1)
        g.add_vertex('A')
        g.add_vertex(2.5)
        
        assert 1 in g.adj_list
        assert 'A' in g.adj_list
        assert 2.5 in g.adj_list
    
    def test_add_vertex_initializes_empty_list(self):
        """Test that added vertex has empty adjacency list."""
        g = Graph()
        g.add_vertex('A')
        assert isinstance(g.adj_list['A'], list)
        assert len(g.adj_list['A']) == 0


class TestAddEdge:
    """Test cases for add_edge method."""
    
    def test_add_edge_between_two_vertices(self):
        """Test adding an edge between two vertices."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        result = g.add_edge('A', 'B')
        
        assert result is True
        assert 'B' in g.adj_list['A']
        assert 'A' in g.adj_list['B']
    
    def test_add_edge_both_directions(self):
        """Test that edge is added in both directions (undirected)."""
        g = Graph()
        g.add_vertex('X')
        g.add_vertex('Y')
        g.add_edge('X', 'Y')
        
        assert 'Y' in g.adj_list['X']
        assert 'X' in g.adj_list['Y']
    
    def test_add_multiple_edges(self):
        """Test adding multiple edges."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'C')
        
        assert len(g.adj_list['A']) == 2
        assert len(g.adj_list['B']) == 2
        assert len(g.adj_list['C']) == 2
    
    def test_add_edge_nonexistent_vertex(self):
        """Test adding edge with nonexistent vertex returns False."""
        g = Graph()
        g.add_vertex('A')
        result = g.add_edge('A', 'Z')
        
        assert result is False
        assert 'Z' not in g.adj_list['A']
    
    def test_add_edge_both_nonexistent(self):
        """Test adding edge with both vertices nonexistent."""
        g = Graph()
        result = g.add_edge('X', 'Y')
        assert result is False
        assert len(g.adj_list) == 0
    
    def test_add_edge_duplicate_edge(self):
        """Test adding the same edge multiple times creates duplicates."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        
        g.add_edge('A', 'B')
        g.add_edge('A', 'B')
        
        # Note: Current implementation allows duplicate edges
        assert g.adj_list['A'].count('B') == 2
        assert g.adj_list['B'].count('A') == 2
    
    def test_add_edge_self_loop(self):
        """Test adding an edge from vertex to itself."""
        g = Graph()
        g.add_vertex('A')
        result = g.add_edge('A', 'A')
        
        assert result is True
        assert 'A' in g.adj_list['A']


class TestRemoveEdge:
    """Test cases for remove_edge method."""
    
    def test_remove_existing_edge(self):
        """Test removing an existing edge."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_edge('A', 'B')
        
        result = g.remove_edge('A', 'B')
        
        assert result is True
        assert 'B' not in g.adj_list['A']
        assert 'A' not in g.adj_list['B']
    
    def test_remove_edge_removes_both_directions(self):
        """Test that removing edge removes from both directions."""
        g = Graph()
        g.add_vertex('X')
        g.add_vertex('Y')
        g.add_edge('X', 'Y')
        
        g.remove_edge('X', 'Y')
        
        assert 'Y' not in g.adj_list['X']
        assert 'X' not in g.adj_list['Y']
    
    def test_remove_nonexistent_edge(self):
        """Test removing nonexistent edge returns True (handles gracefully)."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        
        result = g.remove_edge('A', 'B')
        assert result is True
    
    def test_remove_edge_nonexistent_vertex(self):
        """Test removing edge with nonexistent vertex."""
        g = Graph()
        g.add_vertex('A')
        result = g.remove_edge('A', 'Z')
        
        assert result is False
    
    def test_remove_edge_both_nonexistent(self):
        """Test removing edge with both nonexistent vertices."""
        g = Graph()
        result = g.remove_edge('X', 'Y')
        assert result is False
    
    def test_remove_multiple_edges(self):
        """Test removing one edge doesn't affect others."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'C')
        
        g.remove_edge('A', 'B')
        
        assert 'B' not in g.adj_list['A']
        assert 'C' in g.adj_list['A']
        assert 'C' in g.adj_list['B']
    
    def test_remove_self_loop(self):
        """Test removing a self-loop edge."""
        g = Graph()
        g.add_vertex('A')
        g.add_edge('A', 'A')
        
        result = g.remove_edge('A', 'A')
        
        assert result is True
        assert 'A' not in g.adj_list['A']


class TestRemoveVertex:
    """Test cases for remove_vertex method."""
    
    def test_remove_single_vertex(self):
        """Test removing a single vertex with no edges."""
        g = Graph()
        g.add_vertex('A')
        result = g.remove_vertex('A')
        
        assert result is True
        assert 'A' not in g.adj_list
    
    def test_remove_vertex_with_edges(self):
        """Test removing a vertex also removes all its edges."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        
        result = g.remove_vertex('A')
        
        assert result is True
        assert 'A' not in g.adj_list
        assert 'A' not in g.adj_list['B']
        assert 'A' not in g.adj_list['C']
    
    def test_remove_vertex_cleans_all_references(self):
        """Test that removing vertex removes all references from other vertices."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_vertex('D')
        
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('B', 'D')
        
        g.remove_vertex('B')
        
        assert 'B' not in g.adj_list
        assert 'B' not in g.adj_list['A']
        assert 'B' not in g.adj_list['C']
        assert 'B' not in g.adj_list['D']
    
    def test_remove_nonexistent_vertex(self):
        """Test removing nonexistent vertex returns False."""
        g = Graph()
        g.add_vertex('A')
        result = g.remove_vertex('Z')
        
        assert result is False
    
    def test_remove_vertex_from_empty_graph(self):
        """Test removing vertex from empty graph returns False."""
        g = Graph()
        result = g.remove_vertex('A')
        assert result is False
    
    def test_remove_vertex_with_self_loop(self):
        """Test removing a vertex that has a self-loop."""
        g = Graph()
        g.add_vertex('A')
        g.add_edge('A', 'A')
        
        result = g.remove_vertex('A')
        
        assert result is True
        assert 'A' not in g.adj_list
    
    def test_remove_multiple_vertices(self):
        """Test removing multiple vertices sequentially."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        
        g.remove_vertex('A')
        g.remove_vertex('B')
        
        assert len(g.adj_list) == 1
        assert 'C' in g.adj_list


class TestPrintGraph:
    """Test cases for print_graph method."""
    
    def test_print_empty_graph(self, capsys):
        """Test printing an empty graph."""
        g = Graph()
        g.print_graph()
        
        captured = capsys.readouterr()
        assert "Graph (Adjacency List):" in captured.out
        assert "=" * 50 in captured.out
    
    def test_print_single_vertex(self, capsys):
        """Test printing graph with single vertex."""
        g = Graph()
        g.add_vertex('A')
        g.print_graph()
        
        captured = capsys.readouterr()
        assert "A --> []" in captured.out
    
    def test_print_vertices_with_edges(self, capsys):
        """Test printing graph with connected vertices."""
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_edge('A', 'B')
        g.print_graph()
        
        captured = capsys.readouterr()
        assert "A -->" in captured.out
        assert "B -->" in captured.out
        assert "'B'" in captured.out or "B" in captured.out
    
    def test_print_graph_format(self, capsys):
        """Test print_graph output format."""
        g = Graph()
        g.add_vertex('X')
        g.add_vertex('Y')
        g.add_edge('X', 'Y')
        g.print_graph()
        
        captured = capsys.readouterr()
        lines = captured.out.split('\n')
        
        assert any("=" * 50 in line for line in lines)
        assert any("Graph (Adjacency List):" in line for line in lines)
        assert any("X -->" in line for line in lines)
        assert any("Y -->" in line for line in lines)


class TestGraphIntegration:
    """Integration tests for Graph operations."""
    
    def test_build_complete_graph(self):
        """Test building a complete graph (all vertices connected)."""
        g = Graph()
        vertices = ['A', 'B', 'C', 'D']
        
        for v in vertices:
            g.add_vertex(v)
        
        for i, v1 in enumerate(vertices):
            for v2 in vertices[i+1:]:
                g.add_edge(v1, v2)
        
        # In complete graph, each vertex connects to all others
        assert len(g.adj_list['A']) == 3
        assert len(g.adj_list['B']) == 3
        assert 'B' in g.adj_list['A']
        assert 'C' in g.adj_list['A']
        assert 'D' in g.adj_list['A']
    
    def test_graph_operations_sequence(self):
        """Test a sequence of graph operations."""
        g = Graph()
        
        # Add vertices
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        
        # Add edges
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        
        assert len(g.adj_list['A']) == 1
        assert len(g.adj_list['B']) == 2
        
        # Remove edge
        g.remove_edge('B', 'C')
        assert len(g.adj_list['B']) == 1
        
        # Remove vertex
        g.remove_vertex('A')
        assert 'A' not in g.adj_list
        assert 'A' not in g.adj_list['B']
    
    def test_complex_graph_structure(self):
        """Test a more complex graph structure."""
        g = Graph()
        
        # Create vertices
        for v in range(1, 6):
            g.add_vertex(v)
        
        # Add edges: 1-2, 1-3, 2-4, 3-4, 4-5
        edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
        for v1, v2 in edges:
            g.add_edge(v1, v2)
        
        assert len(g.adj_list[1]) == 2  # 1 connects to 2, 3
        assert len(g.adj_list[4]) == 3  # 4 connects to 2, 3, 5
        assert len(g.adj_list[5]) == 1  # 5 connects to 4
    
    def test_graph_isolation(self):
        """Test isolated vertices in a graph."""
        g = Graph()
        
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_vertex('D')
        
        g.add_edge('A', 'B')
        g.add_edge('C', 'D')
        
        # A-B and C-D are separate components
        assert 'B' in g.adj_list['A']
        assert 'D' in g.adj_list['C']
        assert 'C' not in g.adj_list['A']
        assert 'D' not in g.adj_list['A']


class TestEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_operations_on_empty_graph(self):
        """Test various operations on empty graph."""
        g = Graph()
        
        assert len(g.adj_list) == 0
        assert g.remove_edge('A', 'B') is False
        assert g.remove_vertex('A') is False
    
    def test_numeric_vertices(self):
        """Test graph with numeric vertex identifiers."""
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        
        assert 2 in g.adj_list[1]
        assert 3 in g.adj_list[2]
    
    def test_string_vertices(self):
        """Test graph with string vertex identifiers."""
        g = Graph()
        g.add_vertex("Node-A")
        g.add_vertex("Node-B")
        
        result = g.add_edge("Node-A", "Node-B")
        
        assert result is True
        assert "Node-B" in g.adj_list["Node-A"]
    
    def test_large_graph(self):
        """Test graph with many vertices."""
        g = Graph()
        n = 100
        
        # Add 100 vertices
        for i in range(n):
            g.add_vertex(i)
        
        # Add edges: each vertex connects to next 3 vertices
        for i in range(n - 3):
            g.add_edge(i, i + 1)
            g.add_edge(i, i + 2)
            g.add_edge(i, i + 3)
        
        assert len(g.adj_list) == n
        assert len(g.adj_list[0]) == 3
        assert len(g.adj_list[50]) == 6  # Connected to 4 before and 3 after (with overlap)
