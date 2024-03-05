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

print("</head>")
print("<body style='background-image:url(food_images.jpg);background-size: cover'>")

# ------------------------------------------------------------------------------------------------------------------------------------

source =  string.digits
a1=str()+''.join((random.choice(source) for i in range(4)))

sql = (
    "Insert into product (pid , pname , pmrp , phsn , ppr ) values ( '" + a1 + "','" + a2 + "','" + n3 + "','" + a3 + "','" + a4 + "')"
)
mycursor.execute(sql)
mycursor.execute("SELECT * FROM product")
myresult = mycursor.fetchall()
con.commit()

# print(f"\33[32m"+tabulate(myresult, headers=['Product_Id', 'Product_Name' , 'Product_MRP', 'Product_HSN', 'Product_Purchase_Rate'], tablefmt='psql'))

# -------------------------------------------------------------------------------------------------------------------------------------

print("<center style='font-size:60px ; color: white;text-shadow: 2px 2px 4px #000000'>New Product Added </center><br><br>")
print("<center>","<table border = 1px width=50% >")

print("<tr>")
print("<th style='background-color: rgba(241, 239, 239);height: 500px ; width:900px'>")
print ("<h1 style='color:black'>Product ID :   </h 1>")
print(format(a1))
print ("<h1 style='color:black'>Product Name :  </h 1>")
print(format(a2))
print ("<h1 style='color:black'>Product MRP :  </h 1>")
print(format(n3))
print ("<h1 style='color:black'>Product HSN :  </h 1>")
print(format(a3))
print ("<h1 style='color:black'>Product Purchease Rate :  </h 1>")
print(format(a4))
print("</th>")
print("</tr>")


print("</center>","</table>")

print ("</br>")
print("</body>")
print ("</html>")


# print(mycursor.rowcount, "record(s) affected")








# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------------------------------------------------------------------------------------------------------------


# import os

# os.system("\033[96m")
# os.system('cls||clear')
# import getpass
# import random
# import string

# import colorama
# from colorama import Back, Fore, Style

# colorama . init(autoreset=True)

# import mysql.connector
# from tabulate import tabulate

# con = mysql.connector.connect(
#     host="localhost", user="root", password="4A7$278!9#", database="product"
# )

# mycursor = con.cursor()


# # ---------------------------------------------------------------------------------------------------------------------------------------


# print("Product Id is : ", end =" ")
# source =  string.digits
# a1=str()+''.join((random.choice(source) for i in range(4)))
# print(f"\33[32m"+a1)
# a2 = input("Enter Product Name : ")
# print(f"\33[32m"+a2)
# n3 = input("Enter Product MRP : ")  # For inserting in data base
# print(f"\33[32m"+n3)
# a3 = input("Enter Product HSN : ")
# print(f"\33[32m"+a3)
# a4 = input("Enter Product Purchase Rate : ")
# print(f"\33[32m"+a4)
# sql = (
#     "Insert into product (pid , pname , pmrp , phsn , ppr ) values ( '" + a1 + "','" + a2 + "','" + n3 + "','" + a3 + "','" + a4 + "')"
# )
# mycursor.execute(sql)
# mycursor.execute("SELECT * FROM product")
# myresult = mycursor.fetchall()

# print(f"\33[32m"+tabulate(myresult, headers=['Product_Id', 'Product_Name' , 'Product_MRP', 'Product_HSN', 'Product_Purchase_Rate'], tablefmt='psql'))
# con.commit()
# print(mycursor.rowcount, "record(s) affected")

# # ---------------------------------------------------------------------------------------------------------------------------------------

   