def database():
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='siddharthmysql')
    cur = mydb.cursor()
    cur.execute('create database brainstorm;')
    print('Database Created')


database()