graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ["I"],
    'E': [],
    "F": [],
    'G': [],
    "I": []
}
visit_complete = [] 
def bfs(visit_complete, graph, current_node):
    visit_complete.append(current_node)
    queue = [] 
    queue.append(current_node)
    while queue:
        s = queue.pop(0)
        print(s)
        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)
bfs(visit_complete, graph, 'A')
