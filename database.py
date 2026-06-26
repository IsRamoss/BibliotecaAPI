import sqlite3

#DDL
def ddl():
    query = """CREATE TABLE IF NOT EXISTS livros (
    isbn TEXT PRIMARY KEY,
    titulo TEXT,
    autor TEXT
    );
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

#DML

def connectionCommit(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

def connectionFetch():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    conn.close()

def insertSql(table, dados):
    query = f"""INSERT INTO {table} VALUES {dados} """
    connectionCommit(query)

def dml():
    query = """
    INSERT INTO livros VALUES ('1234','uau', 'jorge');
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()



def dql():
    query = """
    select * from livros ;
    """



if __name__ == '__main__':
    dql()