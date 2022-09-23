""" Server interactions. here"""

from flask import Flask, request, jsonify
from services.GetRoutes import RouteApi
import json
app = Flask(__name__)
import requests

graph_data = json.load(open("db/Graph/graph.json"))


@app.route('/<source_node>-<destination_node>')
def main(source_node,destination_node):
    result = []
    all_routes = RouteApi.find_all_paths(graph_data,source_node, destination_node)
    for route in all_routes:         
        route_json = json.dumps({"route_list" : route}) 
        # print(route_json)  
           
        safety_score = requests.post('http://127.0.0.1:8000/calculate_safety_score',json=json.loads(route_json)).json()
        # print("safety-score for the route: ",safety_score)
        # print("\n")

        route_result = {"route":route, "safety_score": safety_score}
        result.append(route_result)
    return(jsonify(result))



if __name__ == "__main__":
    app.run(debug= True, port = 8080)