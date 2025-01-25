import json


class Graph:
    """
    Class Graph to check Eulerian and Hamiltonian cycles from JSON data.
    """
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def has_eulerian_cycle(self):
        """
        Function to check the graph contains Eulerian cycle or not and making sure it is connected.
        """
        for node, neighbors in self.connections.items():
            if len(neighbors) % 2 != 0:
                return False
        return self.is_connected()

    def backtrack(self, node, path, start_node):
        """
        Helper function to perform backtracking to check for Hamiltonian cycle.
        """
        # Check if the cycle is complete and returns to the start.
        if len(path) == len(self.connections):
            return start_node in self.connections[node]

        # Explore unvisited neighbors.
        for neighbor in self.connections[node]:
            if neighbor not in path:
                path.add(neighbor)
                if self.backtrack(neighbor, path, start_node):
                    return True
                path.remove(neighbor)
        return False

    def has_hamiltonian_cycle(self):
        """
        Function to check the graph contains Hamiltonian cycle or not using backtracking(dfs) technique.
        """
        # Try starting from each node.
        for start_node in self.connections.keys():
            if self.backtrack(start_node, {start_node}, start_node):
                return True
        return False

    def is_connected(self):
        """
        Function to check if the graph is connected using Depth First Search (DFS).
        """
        # If graph is empty return false because empty graph is not connected.
        if not self.connections:
            return False

        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in self.connections[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        start_node = next(iter(self.connections), None)
        if start_node:
            dfs(start_node)

        return len(visited) == len(self.connections)


def load_graphs(json_data):
    """
    Reading JSON data and create Graph objects.
    """
    try:
        data = json.loads(json_data)
        return [Graph(item['name'], item['connections']) for item in data]
    except json.JSONDecodeError as error:
        print(f"Error parsing json data {error}")
        return []


def main():
    """
    Main function to load graphs.
    """
    json_data = """[
        {
            "name": "tree",
            "connections": {
                "a": ["b", "c"],
                "b": ["a"],
                "c": ["a"]
            }
        },
        {
            "name": "triangle",
            "connections": {
                "a": ["b", "c"],
                "b": ["a", "c"],
                "c": ["a", "b"]
            }
        },
        {
            "name": "fan",
            "connections": {
                "a": ["b", "c", "d", "e"],
                "b": ["a", "c"],
                "c": ["a", "b", "d"],
                "d": ["a", "c", "e"],
                "e": ["a", "d"]
            }
        },
        {
            "name": "line",
            "connections": {
                "a": ["b"],
                "b": ["a", "c"],
                "c": ["b"]
            }
        },
        {
            "name": "square",
            "connections": {
                "a": ["b", "d"],
                "b": ["a", "c"],
                "c": ["b", "d"],
                "d": ["a", "c"]
            }
        },
        {
            "name": "empty_graph",
            "connections": {
                
            }
        },
        {
            "name": "self_loops_multiple_edges",
            "connections": { 
                "1": ["1", "2", "2"], 
                "2": ["1", "2"], 
                "3": ["3"] 
            }
        },
        {
            "name": "isolated_nodes",
            "connections": { 
                "1": ["2"], 
                "2": ["1"], 
                "3": [], 
                "4": [] 
            }
        }
    ]
    """

    graphs = load_graphs(json_data)

    for graph in graphs:
        print(
            f"Graph '{graph.name}' {'contains' if graph.has_eulerian_cycle() else 'does not contain'} an Eulerian Cycle.")
        print(
            f"Graph '{graph.name}' {'contains' if graph.has_hamiltonian_cycle() else 'does not contain'} a Hamiltonian Cycle.")
        print("-" * 30)


if __name__ == "__main__":
    main()
