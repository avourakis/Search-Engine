#!/usr/bin/python3
#import cgi, cgitb
import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()

query = form.getvalue("query_field")
print("Content-Type: text/html;charset=utf-8")
print("Content-Type: text/html\r\n\r\n")    

print('<html>')
print('<head>')
print('<title>CGI Program</title>')
print('</head>')
print('<body>')
print('Your query is: ')
print(query)
print('</body>')
print('</html>')

