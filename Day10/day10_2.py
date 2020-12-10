# Day 10 exercise 2

# solved only after hint
# https://www.reddit.com/r/adventofcode/comments/kacdbl/2020_day_10c_part_2_no_clue_how_to_begin/
# geckothegeek's comment

# other links:
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# https://stackoverflow.com/questions/20262712/enumerating-all-paths-in-a-directed-acyclic-graph#:~:text=Finding%20all%20the%20possible%20paths,using%20some%20array%20or%20list.
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# https://www.baeldung.com/cs/simple-paths-between-two-vertices

import day10

def build_graph(nodes):
    graph = dict()
    max_nodes = len(nodes)
    for i in range(max_nodes):
        connections = list()
        if i+1 < max_nodes:
            # i + 1 is always a connection
            connections.append(nodes[i+1])
            if i+2 < max_nodes:
                if nodes[i+2] - nodes[i] <= 3:
                    connections.append(nodes[i+2])
                    if i+3 < max_nodes:
                        if nodes[i+3] - nodes[i] <= 3:
                            connections.append(nodes[i+3])
        graph[nodes[i]] = connections
    return graph
                
# TODO: promote this to common
def pretty_print_dict(name, d):
    print(name)
    for key in d:
        print("{}:{}".format(key, d[key]))



def depth_first_search(node, graph, visited, paths):
    if node in visited:
        return paths
    visited.append(node)
    if node in graph:
        connections = graph[node]
        if len(connections) == 0:
            # print(visited)
            if node in paths:
                paths[node] += 1
            else:
                paths[node] = 1
        else:
            connection_sum = 0
            for connection in connections:
                if connection in paths:
                    connection_sum += paths[connection]
                    visited.append(connection)
                else:
                    paths = depth_first_search(connection, graph, visited.copy(), paths)
                    connection_sum += paths[connection]
            paths[node] = connection_sum
    return paths
    

chargers = day10.read_input_ints("input\\input.txt")
chargers.append(0)
chargers.append(max(chargers)+3)
chargers.sort()

chargers_graph = build_graph(chargers)

# pretty_print_dict("chargers", chargers_graph)
result = dict()
for index in range(len(chargers)-1, -1, -1):
    # print(chargers[index])
    result = depth_first_search(chargers[index], chargers_graph, list(), result)
    # print(result)
print(result[0])
