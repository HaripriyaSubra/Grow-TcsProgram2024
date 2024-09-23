from database_programming_python import *

database_connection = create_db_connection('personsdb')

create_table(database_connection,"persons")

#insert_data(database_connection,"persons")

view_data(database_connection,"persons")

# update_data(database_connection,"persons")

#delete_data(database_connection,"persons")








