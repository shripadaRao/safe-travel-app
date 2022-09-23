
import sqlite3
from flask import Flask, request, jsonify
app = Flask(__name__)


# safety_score =[{'i': 'A', 'i+1': 'B', 'Score': 5},
# {'i': 'A', 'i+1': 'C', 'Score': 5},
# {'i': 'B', 'i+1': 'C', 'Score': 1},
# {'i': 'B', 'i+1': 'D', 'Score': 1},
# {'i': 'C', 'i+1': 'D', 'Score': 10}, 
# {'i': 'D', 'i+1': 'C', 'Score': 9},
# {'i': 'E', 'i+1': 'F', 'Score': 9},
# {'i': 'F', 'i+1': 'C', 'Score': 8},
# ]

import sqlite3
def db_conn():
    con = sqlite3.connect('/home/shripad/Projects/bootcamp/safe-trip/db/Graph/SafetyScore.db')
    cur = con.cursor()
    return cur

def make_node_pairs(route_list) :
    sub_list = []
    for j in range(len(route_list)-1):
        start_node = route_list[j]
        next_node = route_list[j+1]
        sub_list.append([start_node,next_node])
    print("sub-list: ",sub_list)
    return(sub_list)

sub_list = [['A', 'B'], ['B', 'C'], ['C', 'D']]

def get_safety_score(node_mov):  
    i_th = node_mov[0]
    next_node = node_mov[1]

    # for count in range(len(safety_score)):
    #     if(safety_score[count]["i"] == i_th and safety_score[count]["i+1"] == next_node):
    #         return(safety_score[count]["Score"])

    safety_score = db_conn().execute('SELECT node, next_node , score FROM SafetyScore WHERE node = ? AND next_node = ?', (i_th, next_node))
    for count in safety_score:
        return(int(count[2]))

def calculate_safety_score(sub_list):
    total_safety_score = 0
    ss = 0

    for node_mov in sub_list:
        print("i node to i+1 node: ",node_mov)
        ss = get_safety_score(node_mov)
        total_safety_score += ss
    return(total_safety_score/len(sub_list))


@app.route('/calculate_safety_score',methods = ["GET","POST"])
def main():
    route_data = request.json['route_list']
    print("route: ",route_data)
    sub_list = make_node_pairs(route_data)
    return(jsonify(calculate_safety_score(sub_list)))



if __name__ == "__main__":
    app.run(debug=True, port = 8000)