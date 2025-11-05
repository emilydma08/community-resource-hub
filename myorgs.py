import psycopg2

# Database connection details
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "1324"

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn

def get():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM communityresourcehub.orgs;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def getByName(name):
    conn = get_db_connection()
    cur = conn.cursor()
    statement = """SELECT * FROM communityresourcehub.orgs where name = %s ;"""
    cur.execute(statement, (name,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def UpdateByName(name, description, address, email, phone):
    conn = get_db_connection()
    cur = conn.cursor()
    statement = """update communityresourcehub.orgs 
                    set description = %s,
                    address = %s,
                    email = %s,
                    phone = %s
                    where name = %s ;"""
    cur.execute(statement, (description, address, email, phone, name))
    conn.commit()
    cur.close()
    conn.close()

def insert(name, description, address, email, phone):
    conn = get_db_connection()
    cur = conn.cursor()
    statement = """INSERT INTO communityresourcehub.orgs (name, description, address, email, phone) VALUES (%s, %s, %s, %s, %s);"""
    cur.execute(statement, (name, description, address, email, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted successfully.")

def deleteByName(name):
    print("name" + str(name))
    conn = get_db_connection()
    cur = conn.cursor()
    statement = """DELETE FROM communityresourcehub.orgs WHERE name = %s ;"""
    cur.execute(statement, (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("deleted")