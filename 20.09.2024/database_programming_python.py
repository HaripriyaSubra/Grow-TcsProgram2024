import sqlite3

# creating a database connection and connecting to the database using sqlite
def create_db_connection(db_name):
    sc=sqlite3.connect(db_name)
    print("Databse "+ db_name + " is connected")
    return sc

# creating a table in the database
def create_table(database_connection,table_name):
    print("creating database table " + table_name)
    create_table_query = "create table if not exists "+table_name+"(id number primary key, name varchar(100) not null)"
    cursor=database_connection.cursor()
    cursor.execute(create_table_query)
    database_connection.commit()
    print("Table " + table_name+ " is created")

# inserting data to the table in the database
def insert_data(database_connection,table_name):
    print("inserting data into the table " + table_name)
    insert_query="insert into "+table_name+" values (?,?)"
    cursor=database_connection.cursor()
    print("Please enter id")
    id=int(input())
    print("Please give name")
    name=input()
    data =(id,name)
    cursor.execute(insert_query,data)
    database_connection.commit()
    print("data is inserted into " + table_name)

 # reading the data from the table
def view_data(database_connection,table_name):
    print("viewing the data from the table " + table_name)
    select_query = "select * from "+ table_name
    cursor=database_connection.cursor()
    cursor.execute(select_query)
    records=cursor.fetchall()
    if(len(records)!=0):
        print("Fetching the data")
        for i in records:
            print("Id : "+str(i[0])+"\nName : "+i[1])
    else:
        print('There are no records present in the table '+ table_name)


# updating the data in the table
def update_data(database_connection,table_name):
    print("updating data in the table " + table_name)
    query="update "+table_name+" set name = ? where id= ?"
    print("Please enter your id")
    id=int(input())
    print("Please give name to update")
    name=input()
    cursor=database_connection.cursor()
    data=(name,id)
    cursor.execute(query,data)
    database_connection.commit()
    print("Data in" +table_name+ " is updated")

# deleting the data in the table
def delete_data(database_connection,table_name):
    print("deleting data from the table " + table_name)
    query = "delete from "+table_name+" where id = ?"
    print("enter the id to delete ")
    id=int(input())
    data= (id,)
    database_connection.execute(query,data)
    database_connection.commit()
    print("data is removed")

