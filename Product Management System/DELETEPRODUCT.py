#!C:\Users\Rudradeep\AppData\Local\Programs\Python\Python310\python.exe

#!c:\python37\python.exe
# Import modules for CGI handling

import mysql.connector
con = mysql.connector.connect(
    host="localhost", user="root", password="4A7$278!9#", database="product"
)

mycursor = con.cursor()




print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Delete Product</title>")
print('<link rel="stylesheet" href="m.css">')
print('<link rel="stylesheet" href="ADDPRODUCT.css">')

print("</head>")
print("<body>")

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


print("<div class='split left'>")
print("<center>")
print("<h1> Add Product Deetails </h1><br><br>")
print("</center>")
print("<div class='transperent_box'>")
print("<fieldset>")
            
print(" <table width='100%'>")
print("<form action='menu.py' method='get' autocomplete='off''>")

                   

print("<tr>")
print("<th> <label for='pname'>")
print("<h3>Product Name:</h3>")
print("</label></th>")

print("<th> <input onkeydown='return /[a-z]/i.test(event.key)' type='text' id='pname' name='pname' placeholder='Product Name...' name='pname' required><br><br></th>")

print("</tr>")
print("<tr>")
print("<th> <label for='pmrp'>")
print("<h3>Product MRP:</h3>")
print("</label></th>")

print("<th><input type='number' min='0' id='pmrp' MRP='pmrp' placeholder='Product MRP...' name='pmrp' required><br><br></th>")
print("</tr>")
print("<tr>")
print("<th> <label for='phsn'>")
print("<h3>Product HSN:</h3>")
print("</label></th>")

print("<th><input type='number' min='0' id='phsn' HSN='phsn' placeholder='Product HSN...' name='phsn'  required><br><br></th>")

print("</tr>")

print("<tr>")
print("<th><label for='ppr'>")
print("<h3>Product Purchase Rate:</h3>")
print("</label></th>")

print("<th><input type='number' min='0' id='ppr' PPR='ppr' placeholder='Product Purchase Rate...'  name='ppr' required><br><br><br></th>")
print("</tr>")
print("</table>")
print("<center><input type='submit' value='Submit'></center>")

print("</form>")

print("</fieldset>")
print("</div>")
print("</div>")




# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

cursor = con.cursor()
cursor.execute("SELECT * FROM product")
result_set = cursor.fetchall()


print("<div class='split right'>")
print("<center style='font-size:40px ; color: white;text-shadow: 2px 2px 4px #000000'>Delete Product </center>")


print("<div class='newlist'>")

print("<span>")
print("<form action='DELETEPRODUCT2.py' method='get' autocomplete='off''>")
print("<input type='text' id='myInput'name='myInput'  placeholder='Write ID to delete...' >")
print("</form>")
print("</div>")
print("</span>")
print(cursor.rowcount, "Record Added")


print("<div class='scrollit'>")
print("<div class='mytable'>")
print("<table style='border-collapse: collapse ;  width: 100% '>")
print("<tr>")

print("<th style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px ; padding-top: 12px ; padding-bottom: 12px ; background-color: #04AA6D ; color: white'>")
print("Product ID")
print("</th>")

print("<th style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px ; padding-top: 12px ; padding-bottom: 12px ; background-color: #04AA6D ; color: white'>")
print("Product Name")
print("</th>")

print("<th style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px ; padding-top: 12px ; padding-bottom: 12px ; background-color: #04AA6D ; color: white'>")
print("Product MRP")
print("</th>")

print("<th style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px ; padding-top: 12px ; padding-bottom: 12px ; background-color: #04AA6D ; color: white'>")
print("Product HSN")
print("</th>")

print("<th style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px ; padding-top: 12px ; padding-bottom: 12px ; background-color: #04AA6D ; color: white'>")
print("Product Purchase Rate")
print("</th>")

print("</tr>")


for row in result_set:

   
    print("<td style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px'>","<center>")
    print(row[0])
    print("</td>","</center>")

    print("<td style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px'>","<center>")
    print(row[1])
    print("</td>","</center>")

    print("<td style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px'>","<center>")
    print(row[2])
    print("</td>","</center>")

    print("<td style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px'>","<center>")
    print(row[3])
    print("</td>","</center>")

    print("<td style='-moz-text-size-adjust: 20% ; border: 1px solid black ; padding: 8px'>","<center>")
    print(row[4])
    print("</td>","</center>")
    print("</tr>")

print("</table>")
print("</div>")
print("</div>")
print("</div>")

print ("</br>")
print("</body>")
print ("</html>")
