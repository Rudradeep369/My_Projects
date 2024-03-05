#!C:\Users\Rudradeep\AppData\Local\Programs\Python\Python310\python.exe

# import cgi, cgitb

# print ("Content-type:text/html\r\n\r\n")
# print("<html>")
# print("<head>")
# print("<title>Hello World - First CGI Program</title>")
# print("</head>")
# print("<body> <h1>Hello World</h1> ")

# print("</body>")
# print ("</html>")

# ----------------------------------------------------------------------------------------------------------------


#!c:\python37\python.exe
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
nm=form.getvalue('name')
print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
print ("<h2>Data received from client form</h 2>")
print("Name: {}".format(nm))
print ("</br>")
print("</body>")
print ("</html>")

# ---------------------------------------------------------------------------------------------------------