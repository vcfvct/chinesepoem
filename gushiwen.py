from lxml import html
import requests

result = [];
start=input("Enter the start page: ");
end=input("Enter the end page: ");
for x in range(start, end):
	page = requests.get('http://www.gushiwen.org/mingju_'+ str(x) +'.aspx')
	tree = html.fromstring(page.content)
	#This will get the poem highlight
	tile = tree.xpath('//div[@class="authorTile"]/h1')[0].text.encode('utf8')
	textToWrite = str(x) + ': ' + tile
	print textToWrite
	result.append(textToWrite)

f=open('result.txt','w')
for ele in result:
    f.write(ele+'\n')

f.close()

