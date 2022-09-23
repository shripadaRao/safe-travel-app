""" This File serves 2 functionalities.
    1. Query sql data and transform into Graph structure.
    2. Transform Graph into sql data and store it.
    Interacts with db/Graph and RouteAPI """



# Examples of schemes.
# graph = {'A': ['B', 'C'],
#          'B': ['C', 'D'],
#          'C': ['D'],
#          'D': ['C'],
#          'E': ['F'],
#          'F': ['C']}

# safety_scores = {
#     'A' - 5 -> 'B',
#     'C' - 5 -> 'A',
#     'D' - 5 -> 'C',
#     'F' - 5 -> 'E',
#     'C' - 5 -> 'A',
#     'A' - 5 -> 'O',
# }


import sqlite3
def connect_db():
    try:
        create_db = sqlite3.connect("/home/shripad/Projects/bootcamp/safe-trip/db/Graph/SafetyScore.db") #DOESNT WORK WHEN RELATIVE FILE PATH IS GIVEN.
        print("Database connected")
        return(create_db)
    except Exception as e:
        print("Expection in creating db: "+ e.message)
def create_safety_table():   
    """ Function creates a table(safety_score). Schema- Columns: "i'th", "i+1'th", "safety-score".   """
    
    create_table = "create table SafetyScore (id INTEGER PRIMARY KEY AUTOINCREMENT, node TEXT NOT NULL, next_node TEXT NOT NULL, score INTEGER NOT NULL)"
    try:
        connect_db().execute(create_table)
        print("Table created successfully")  
    except Exception as e:
        print("Expection in creating auth table: "+ e.message)
    finally:
        connect_db().close()

#create_safety_table()

