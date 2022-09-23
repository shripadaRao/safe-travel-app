""" Functions: Simple Login.
    This File takes in user_name and password as input.
    Interacts with db/Auth database. """

#Currently using sqlite3.

import sqlite3
from flask import Flask

def connect_db():
    try:
        create_db = sqlite3.connect("/home/shripad/Projects/bootcamp/safe-trip/db/Auth/auth.db") #DOESNT WORK WHEN RELATIVE FILE PATH IS GIVEN.
        print("Database connected")
        return(create_db)
    except Exception as e:
        print("Expection in creating db: "+ e.message)

def create_auth_table():   
    """ Function creates a table(Auth). Columns of db - name, password """
    #create_table = "create table Auth (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, password TEXT NOT NULL)"
    create_table = "create table Auth (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, password TEXT NOT NULL)"
    try:
        connect_db().execute(create_table)
        print("Table created successfully")  
    except Exception as e:
        print("Expection in creating auth table: "+ e.message)
    finally:
        connect_db().close()


#-----------------------------------------------------------------------------------#

app = Flask(__name__)

@app.route("/insert/<name>:<password>")
def insert_row(name,password):
    """ This takes in name, password and inserts into db """
    try:
        with connect_db() as con:
            cur = con.cursor()
            cur.execute("INSERT into Auth (name,password) values (?,?)", (name,password) )
            con.commit()
            return("inserted data")
    except Exception as e:
        return("Expection Error: "+ e.message)


@app.route("/view")
def view_rows():
    """ View all records """
    try:
        cursor = connect_db().cursor()
        query_auth = "select * from Auth"
        cursor.execute(query_auth)
        return(str(cursor.fetchall()))  # returns a list -> str(list)
    except Exception as e:
        return("Expection Error: "+ e.message)

@app.route("/<name>:<password>")  #<name>:<password>
def verify_user(name,password):
    """ Checks username and password in the database """
    try:
        cursor = connect_db().cursor()   
        query_user = "select name, password from Auth"
        get_users = cursor.execute(query_user).fetchall()
    except Exception as e:
        return("Expection Error: "+ e.message)

    # """Check whether GetName_Password is same as input"""
    input_list = (name,password)
    for user in get_users:
        if user == input_list:
            return("Your Verified!") 
        else:
            return(str(get_users)+" are the right credentials" + " but got " +str(input_list))

if __name__ == "__main__":  
    app.run(debug = True)