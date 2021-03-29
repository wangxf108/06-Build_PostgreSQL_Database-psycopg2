#how to interact with PostGreSQL databases. 
#Interact with database by psycopgs.
#和172-delete_update_sql 的明显区别是，‘？’全部被‘%s’替代了。 另外，variable也全部变化了。

import psycopg2        

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres108' host='localhost' port='5432'")         
    cur=conn.cursor()                       
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") 
    cur.execute("INSERT INTO store VALUES ('Wine Glass')")     
    conn.commit()                         

def insert(item,quantity,price):           
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres108' host='localhost' port='5432'")  #与sqlite相比，此处key变化      
    cur=conn.cursor()                       
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item,quantity,price))    
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))       #这是上一句的变形，运行以后，同样可行
    conn.commit()                          
    conn.close()                           

def view():                             
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres108' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")     
    rows=cur.fetchall()                     
    conn.close()
    return rows

def delete(item):                             #delete function 
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres108' host='localhost' port='5432'")  # Again, change the variable
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))       # item=%s  and ',' is needed
    conn.commit()
    conn.close()

def update(quantity, price, item):                             
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres108' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))      
    conn.commit()
    conn.close()


#下面的四个function，运行sqlite 
#update(11,6,"COffee Cup")
#insert("COffee Cup",10,5)
#delete("Water Glass")
#print(view()) 



#下面的function，运行psycogp2，（通过在python中，运行psycopg2 library, 可以连接数据库。使数据库可视化。）
create_table()
insert("Orange",10,15)
delete("Orange")
update(20,15.0,'Apple')
print(view())                 # you can see the result in the terminal directly this time .
