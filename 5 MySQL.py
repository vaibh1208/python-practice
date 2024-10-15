# #to connect python with mysql
# import mysql.connector
# myconn = mysql.connector.connect(host = 'localhost',user = 'root',passwd ='')
# # create cursor object to fire queries
# cur = myconn.cursor()
# print(cur)
# print('CONNECTION DONE')
#
# import mysql.connector
# myconn = mysql.connector.connect(host = 'localhost',user = 'root',passwd ='')
# cur = myconn.cursor()
# print("Cur")
# sql = "CREATE DATABASE IF NOT EXISTS Python30" #fire query
# cur.execute(sql)
# print("Cur")
# print("Connection Succesfully")


# import mysql.connector
# myconn = mysql.connector.connect(host = "localhost",user = "root",passwd = "")
# cur = myconn.cursor()
# sql = "drop  database if exists python30"
# cur.execute(sql)
# print("Database deleted")


# import mysql.connector
# myconn = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '')
# cur = myconn.cursor()
# cur.execute('Create database if not exists Aarush')
# print("Database created")

# import mysql.connector
# myconn = mysql.connector.connect(host = "localhost",user = "root",passwd = "")
# cur = myconn.cursor()
# sql = "create database if not exists vaibhav"
# cur.execute(sql)
# print("Database created")
#
# import mysql.connector
# try:
#     myconn = mysql.connector.connect(host = "localhost",user = "root",passwd = "")
# except Exception as e:
#     print('problem',e)
# else:
#     print('connect success')
#     myconn.close()

# import mysql.connector
# try:
#     myconn = mysql.connector.connect(host = "localhost",user = "root",passwd = "")
#     cur = myconn.cursor()
#     cur.execute("Create database if not exists Vaishnav")
# except Exception as e:
#     print('problem',e)
# else:
#     print('connect success')
#     myconn.close()

# import mysql.connector
# myconn = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '')
# cur = myconn.cursor()
# sql = "DROP DATABASE IF EXISTS Vaishnav"
# cur.execute(sql)
# print("Data Base deleted")

# import mysql.connector
# myconn = mysql.connector.connect(host = 'localhost', user = 'root' , passwd = '')
# cur  = myconn.cursor()
# sql = "CREATE DATABASE IF NOT EXISTS vedant"
# cur.execute(sql)

# import mysql.connector
# myconn = mysql.connector.connect(host = 'localhost' , user = 'root' , passwd = '')
# cur = myconn.cursor()
# sql = "DROP DATABASE IF EXISTS Aggregates"
# cur.execute(sql)
# print('Database Deleted succuesfully')

#TO ADD DATA
# import mysql.connector
#
# try:
#     myconn = mysql.connector.connect(host='localhost', user='root', passwd='', database='vowtech')
#     cur = myconn.cursor()
#     rollno = int(input('Enter the rolno:'))
#     name = input('Enter the name: ')
#     sql = f"insert into python(name,rollno) values('{name}',{rollno})"
#     cur.execute(sql)
#
# except Exception as e:
#     myconn.rollback()
#     print('Problem: ',e)
#
# else:
#     myconn.commit()
#     print('Done!!!')
#     myconn.close()

#TO UPDATE DATA
# import mysql.connector
#
# try:
#     myconn = mysql.connector.connect(host='localhost', user='root', passwd='', database='vowtech')
#     cur = myconn.cursor()
#     rollno = int(input('Enter the rolno:'))
#     name = input('Enter the name: ')
#     sql = f"update python set name = '{name}' where rollno = {rollno}"
#     cur.execute(sql)
#
# except Exception as e:
#     myconn.rollback()
#     print('Problem: ',e)
#
# else:
#     myconn.commit()
#     print('Done!!!')
#     myconn.close()


#To search (login page)
# import mysql.connector
#
# try:
#     myconn = mysql.connector.connect(host='localhost', user='root', passwd='', database='vowtech')
#     cur = myconn.cursor()
#     city = input('Enter the city:')
#     name = input('Enter the name: ')
#     sql = f"select * from python where name ='{name}' and city = '{city}' "
#     cur.execute(sql)
#     res = cur.fetchall()
#     if res:
#         print('Data is in the database')
#     else:
#         print('Data is not in database need to update')
#
# except Exception as e:
#     myconn.rollback()
#     print('Problem: ',e)
#
# else:
#     myconn.commit()
#     print('Done!!!')
#     myconn.close()


