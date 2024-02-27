import sqlite3


def create_connection(file):
    """创建SQLite连接"""
    conn = None
    try:
        conn = sqlite3.connect(file)
        print(f'Successfully connected to SQLite database: {file}')
    except sqlite3.Error as e:
        print(e)
    return conn

def execute_query(conn, query):
    """执行SQL查询"""
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print('Query executed successfully')
    except sqlite3.Error as e:
        print(e)
def execute_query_by_args(conn, query,args):
    """执行SQL查询"""
    try:
        cursor = conn.cursor()
        cursor.execute(query,args)
        conn.commit()
        print('Query executed successfully')
    except sqlite3.Error as e:
        print(e)

def execute_read_query(conn, query):
    """执行SQL查询并返回结果"""
    result = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(e)
def execute_in_file(file,func):
    try:
        connection=create_connection(file)
        res=func(connection)
        connection.close()
        return res
    except Exception as e:
        print("db run error: {}".format(e))
def run_sql(file,sql):
    execute_in_file(file,lambda cnn:(
        execute_query(cnn,sql)
    ))
def run_sql_select(file,sql):
     return execute_in_file(file,lambda cnn:(
        execute_read_query(cnn,sql)
    ))
def run_sql_insert(file,sql,args):
    execute_in_file(file,lambda cnn:(
        execute_query_by_args(cnn,sql,args)
    ))

