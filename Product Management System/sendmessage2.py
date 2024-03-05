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
nm=form.getvalue('pname')
pn=form.getvalue('phone')
hr=int(form.getvalue('hr'))
min=int(form.getvalue('min'))
message=form.getvalue('message')
print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Send Page</title>")
print("</head>")
print("<body>")
# print ("<p>Data received from client form</p>")
# print("Name : {} <br>".format(nm))
# print("Phone number : {}<br>".format(pn))
# print("Hour : {}<br>".format(hr))
# print("Minute : {}<br>".format(min))
# print("Message : {}<br>".format(message))
print ("</br>")
# pywhatkit.sendwhatmsg("+919830141522", "Hello sir", 17, 29)
pywhatkit.sendwhatmsg(pn , message , hr , min)

# print('<meta http-equiv="refresh" content="0;url='+str("http://localhost/rudra/sendmessagerough.py")+'" />') 

print("</body>")

print ("</html>")
# pywhatkit.sendwhatmsg(pn , message , hr , min)