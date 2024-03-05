#!C:\Users\Rudradeep\AppData\Local\Programs\Python\Python310\python.exe




# ----------------------------------------------------------------------------------------------------------------


#!c:\python37\python.exe
# Import modules for CGI handling
import cgi, cgitb
import pywhatkit

cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields

# Get data from fields
# nm=form.getvalue('pname')
# pn=form.getvalue('phone')
# hr=int(form.getvalue('hr'))
# min=int(form.getvalue('min'))
# message=form.getvalue('message')
print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Send Page</title>")
print("</head>")
print("<body>")

# pywhatkit.sendwhatmsg("+919830141522", "Hello sir", 17, 29)
pywhatkit.sendwhatmsg(form.getvalue('phone'), form.getvalue('message') , int(form.getvalue('hr')) , int(form.getvalue('min')))
print("</body>")
print ("</html>")