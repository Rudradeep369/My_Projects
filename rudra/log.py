#!C:\Users\Rudradeep\AppData\Local\Programs\Python\Python310\python.exe

import cgi, cgitb
cgitb.enable()
import requests
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
nm=form.getvalue('uname')
p=form.getvalue('psw')
print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
if nm !="rudra" or p != "123":
    print('<meta http-equiv="refresh" content="0;url='+str("http://localhost/rudra/new_login_2.html")+'" />') 
   # print ("heelo")

else:
    print('<meta http-equiv="refresh" content="0;url='+str("http://localhost/rudra/menu.html")+'" />')


print("</body>")
print ("</html>")

