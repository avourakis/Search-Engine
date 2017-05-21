#!/usr/bin/python3.5
import cgi, cgitb

# Query entered by user
query = form.getvalue("query_field")

print("content-type:text/html")
print("<html>")
print("<head>")
print("<title>CGI Program</title>")
print("</head>")
print("<body>")
print("Your query is: ")
print(query)
print("</body>")
print("</html>")

