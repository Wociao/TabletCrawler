import urllib.request

response=urllib.request.urlopen('http://www.youtube.com')
result=response.read().decode('utf-8')
#print(result)
print("guabi")

