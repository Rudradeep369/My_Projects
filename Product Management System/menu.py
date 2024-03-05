#!C:\Users\Rudradeep\AppData\Local\Programs\Python\Python310\python.exe

#!c:\python37\python.exe
# Import modules for CGI handling
import cgi, cgitb
import random
import string

import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(
    host="localhost", user="root", password="4A7$278!9#", database="product"
)

mycursor = con.cursor()

# ---------------------------------------------------------------------------------------------------------------------------------------

# mycursor.execute("CREATE TABLE product (pid VARCHAR(255) PRIMARY KEY, pname VARCHAR(255), pmrp VARCHAR(255), phsn VARCHAR(255), ppr VARCHAR(255))")

# sql = "Insert into product (pid , pname , pmrp , phsn , ppr  ) values (%s , %s , %s , %s , %s )"
# print("\n Table created 😎")

# ---------------------------------------------------------------------------------------------------------------------------------------


cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
a1=form.getvalue('pid')
# a2=form.getvalue('pname')
n3=form.getvalue('pmrp')
a3=form.getvalue('phsn')
a2=form.getvalue('pname')
a4=form.getvalue('ppr')

print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
# print('<link rel="stylesheet" href="m.css">')

print("</head>")
print("<body>")


source =  string.digits
a1=str()+''.join((random.choice(source) for i in range(4)))

sql = (
    "Insert into product (pid , pname , pmrp , phsn , ppr ) values ( '" + a1 + "','" + a2 + "','" + n3 + "','" + a3 + "','" + a4 + "')"
)
mycursor.execute(sql)
mycursor.execute("SELECT * FROM product")
myresult = mycursor.fetchall()
con.commit()


cursor = con.cursor()
cursor.execute("SELECT * FROM product")
result_set = cursor.fetchall()
print('<meta http-equiv="refresh" content="0;url='+str("http://localhost/rudra/redirect_menue.py")+'" />') 

# ------------------------------------------------------------------------------------------------------------------------------------

# print("<center style='font-size:60px ; color: white;text-shadow: 2px 2px 4px #000000'>New Product Added </center><br><br>")
# print("<p>")
# print(mycursor.rowcount, "record Added")
# print("</p>")
# print("<table>")
# print("<tr>")

# print("<th>")
# print("Product ID")
# print("</th>")

# print("<th>")
# print("Product Name")
# print("</th>")

# print("<th>")
# print("Product MRP")
# print("</th>")

# print("<th>")
# print("Product HSN")
# print("</th>")

# print("<th>")
# print("Product Purchase Rate")
# print("</th>")

# print("</tr>")

# for row in result_set:

   
#     print("<td>","<center>")
#     print(row[0])
#     print("</td>","</center>")

#     print("<td>","<center>")
#     print(row[1])
#     print("</td>","</center>")

#     print("<td>","<center>")
#     print(row[2])
#     print("</td>","</center>")

#     print("<td>","<center>")
#     print(row[3])
#     print("</td>","</center>")

#     print("<td>","<center>")
#     print(row[4])
#     print("</td>","</center>")
#     print("</tr>")

# print("</table>")
# print ("</br>")
# print("</body>")
# print ("</html>")
