import sqlite3             

def create_table():
    conn=sqlite3.connect("lite.db")         
    cur=conn.cursor()                       
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTERGE, price REAL)") 
    cur.execute("INSERT INTO store VALUES ('Wine Glass')")     
    conn.commit()                         

def insert(item,quantity,price):           
    conn=sqlite3.connect("lite.db")        
    cur=conn.cursor()                       
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))    
    conn.commit()                          
    conn.close()                           

def view():                             
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")     
    rows=cur.fetchall()                     
    conn.close()
    return rows

def delete(item):                             #delete function 
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))       # "," is needed here
    conn.commit()
    conn.close()

def update(quantity, price, item):                             
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,,item))      
    conn.commit()
    conn.close()

update(11,6,"COffee Cup")
#insert("COffee Cup",10,5)
#delete("Water Glass")
print(view())