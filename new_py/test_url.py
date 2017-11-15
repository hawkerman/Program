#import urllib3

#from bs4 import BeautifulSoup

#http = urllib3.PoolManager()

#r=http.request('GET','http://yahoo.co.jp/')
#print(r.status)
#rawdata = urllib3.urlopen('http://yahoo.co.jp/').read()
import chardet



from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = 'http://yahoo.co.jp/'
response = http.request('GET', url)
soup = BeautifulSoup(response.data,"html.parser")

print(soup)
#print(type(soup))
print(type(response))
#print(chardet.detect(str(response)))
#print(chardet.detect(str.encode(response.data)))
