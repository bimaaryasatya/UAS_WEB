import pymysql
import pymysql.cursors

conn = pymysql.connect(host="localhost", user="root", passwd="", database="uasweb")
cursor = conn.cursor()

def add_contact(name, email, pesan):

    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "INSERT INTO uas (name, email, pesan) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, pesan))
            print("Data berhasil dimasukkan:", name, email, pesan)

        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def update_pesan(id, name, email, pesan):
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "UPDATE uas SET name=%s, email=%s, pesan=%s WHERE id=%s"
            cursor.execute(sql, (name, email, pesan, id))
            conn.commit()
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def delete_pesan(id):
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "DELETE FROM uas WHERE id=%s"
            cursor.execute(sql, (id,))
            conn.commit()
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def get_last_pesan():
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM uas ORDER BY id DESC LIMIT 1"
            cursor.execute(sql)
            pesan = cursor.fetchone()
            return pesan
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_pesan(id):
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM uas WHERE id=%s"
            cursor.execute(sql, (id,))
            pesan = cursor.fetchone()
            return pesan
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_all_pesan():
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM uas"
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
        return []