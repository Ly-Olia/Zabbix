import mysql.connector

from app.schema import UserLogin


# function to execute a database query and returns the result
def run_query(query, param, is_update):
    cnx = mysql.connector.connect(user='mysql', password='root', host='localhost', port=3307, database='user')
    cursor = cnx.cursor()
    cursor.execute(query, param)
    if is_update:
        cnx.commit()
        return
    return cursor.fetchall()


# function to check if a user exists in the database
def check_user(data: UserLogin):
    query = """SELECT email, password FROM users 
    where email=%s and password=%s"""
    val = (data.email, data.password)
    result = run_query(query, val, is_update=False)
    if not result:
        return False
    return True


# function to set the active status of a user in the database
def set_active(user: UserLogin, value: bool):
    query = """UPDATE users 
       SET is_active = %s
       where email=%s and password=%s"""
    val = (int(value), user.email, user.password)
    run_query(query, val, is_update=True)
