#!C:\Users\Rudradeep\AppData\Local\Programs\Python\Python310\python.exe

import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
nm=form.getvalue('username')
print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
print ("<h2>User name : </h 2>")
print(" {}".format(nm))
print ("</br>")
print("</body>")
print ("</html>")