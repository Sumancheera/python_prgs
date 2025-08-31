graph={
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1,4,5],
    4: [2,3,5],
    5: [3,4,6],
    6: [5]
}
def print_all_paths(graph, current, tar, path, visited):
    if current == tar:     # Base case: if the source is the target, a complete path is found
        print(path)
        return
    if current in graph:     # Recursive step: explore neighbors
        for neighbor in graph[current]:
            # Check if the neighbor has already been visited in this path
            if neighbor not in visited:
                visited.add(neighbor) # Mark as visited
                print_all_paths(graph, neighbor, tar, path + "->" + str(neighbor), visited) # Recursive call for the neighbor
                visited.remove(neighbor) # Backtracking step: unmark the neighbor to explore other paths
initial_visited={0} # Initially, the source node is visited
print(type(initial_visited))
print_all_paths(graph, 0, 5, str(0), initial_visited) # Start the path finding from node 0 to node 5

