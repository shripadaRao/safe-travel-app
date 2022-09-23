""" This API takes in 'from' and 'to' parameters. Outputs a list of lists (all routes). """


from flask import Flask, request, jsonify
app = Flask(__name__)

# graph = {'A': ['B', 'C'],
#          'B': ['C', 'D'],
#          'C': ['D'],
#          'D': ['C'],
#          'E': ['F'],
#          'F': ['C']}

all_routes = []
def find_all_paths(graph, start, end, path=[]) -> list:
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
#print(find_all_paths(graph,'A','C'))

