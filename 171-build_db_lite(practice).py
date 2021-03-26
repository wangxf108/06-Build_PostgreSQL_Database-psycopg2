import sqlite3             

def create_table():
    conn=sqlite3.connect("lite.db")         # 1.first of all, need to build a connection. and a database will be built by this code.
    cur=conn.cursor()                       # 2.cursor method is a method of the connection object.
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTERGE, pirce REAL)")      #3.Actual SQL code. the contents in the db.
    cur.execute("INSERT INTO store VALUES ('Wine Glass')")       # REMEMBER: SQL code always goes inside quotes.  As a string to the execute method of the cursor object on the sqlite3 library.
    conn.commit()                           #4. Commit the connection and close it in the next step
    conn.close()

def insert(item,quantity,price):            # 5.another function
    conn=sqlite3.connect("lite.db")         # fixed code
    cur=conn.cursor()                       # fixed code
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))     # 6.question marks will be replaced by what user input
    conn.commit()                           # fixed code
    conn.close()                            # fixed code

insert("Water Glass",10,5)

def view():                                 #7. By this function, you can see the data 
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")      #8.select all the data 
    rows=cur.fetchall()                     
    conn.close()
    return rows

print(view())
