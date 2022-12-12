import http.client

connection = http.clients.HTTPSConnection("http://127.0.0.1:14000/index.html")
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason {}".format(response.status, response.reason))
connection.close();