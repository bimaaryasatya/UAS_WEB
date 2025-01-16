import pymysql

conn = pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
                       database="latihancrud")
cursor = conn.cursor()

def text_add(text_value):
    cursor.execute("INSERT INTO tabelcrud(id, text) VALUES(DEFAULT,%s)", (text_value))
    conn.commit()
    return 1

def get_data():
    cursor.execute("SELECT * FROM tabelcrud")
    data = cursor.fetchall()
    return data
