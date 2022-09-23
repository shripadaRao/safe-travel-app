""" Given 'n' parameters as input, output a score and store it in database. """

import sqlite3
from flask import Flask, request, jsonify
app = Flask(__name__)


#api to insert the calculated safety score
@app.route('/safetyscore/insert',methods = ["GET","POST"])
def insert_record():
    # conn = sqlite3.connect('/home/shripad/Projects/bootcamp/safe-trip/db/Graph/SafetyScore.db')
    # cursor = conn.cursor()
    request_data = request.get_json()
    print(request_data)
    node = request_data['node']
    next_node = request_data['next_node']
    score = request_data['score']  
    # cursor.execute('''INSERT INTO SafetyScore(node, next_node, score) VALUES(?,?,?) ''',(node,next_node, score))
    # conn.commit()
    return(jsonify(str(request_data)+" inserted successfully"))
#{"node" : "" , "next_node" : "", "score" :"}


# function to parse geographical data. data is fetched from the client.
def parse_geo_data():
    pass


# Logic for calculating safety score for the given geographical data
def math_formula(*args): 
    pass

def main():
    ss_predication= math_formula(parse_geo_data())
    return(ss_predication)

if __name__ == "__main__":
    app.run(debug = True)