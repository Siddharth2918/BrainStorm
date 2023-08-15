def user_login():
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='siddharthmysql', database="brainstorm")
    cur = mydb.cursor()
    query = "select username, user_password from users;"
    run = cur.execute(query)
    output = cur.fetchall()
    return output

def user_signup(username, user_password, email_id, first_name, last_name):   
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='siddharthmysql', database="brainstorm")
    cur = mydb.cursor()
    query1 = "insert into users(username, user_password, email_id, first_name, last_name) values('{0}', '{1}', '{2}', '{3}', '{4}')".format(username, user_password, email_id, first_name, last_name)
    cur.execute(query1)
    query2 = '''create table ''' + username + '''(date varchar(10), gender varchar(10), age int, hypertension varchar(10), heartdisease varchar(10), evermarried varchar(10), 
	    worktype varchar(10), recidencetype varchar(10),glucoselevel float, bmi float, smokingstatus varchar(20), prediction int);'''
    cur.execute(query2)

def input_predict(name, gender, age, hypertension, heartdisease, evermarried, worktype, recidencetype , glucoselevel, bmi, smokingstatus):
    import mysql.connector
    from datetime import date
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='siddharthmysql', database="brainstorm")
    cur = mydb.cursor()
    query = "insert into "+ name +" values('{0}', '{1}', '{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}', '{10}', 0);".format(date.today(), gender, age, hypertension, heartdisease, evermarried, worktype, recidencetype , glucoselevel, bmi, smokingstatus)
    cur.execute(query)
    mydb.commit()
    return 0

def user_tests(name):
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='siddharthmysql', database="brainstorm")
    cur = mydb.cursor()
    query = "select date, age, prediction from {0};".format(name)
    run = cur.execute(query)
    output = cur.fetchall()
    return output