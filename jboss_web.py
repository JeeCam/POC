#coding=utf8
import requests
import re
from bs4 import BeautifulSoup
# url='https://sourceforge.net/projects/jboss/rss?path=/JBoss'
# url = 'https://sourceforge.net/projects/jboss/files/JBoss/jboss-seam-distribution-2.3.0.Final-dist.tar.gz/download'
# r=requests.get(url)
# print r.text


def geturl(url):
	# url = 'https://sourceforge.net/projects/jboss/files/JBoss/JBoss-6.0.0.Final/'
	re = requests.get(url)
	Soup = BeautifulSoup(re.text,'html.parser')
	for link in Soup.find_all('a'):
		try: 
			if str(link['class'][0]) == "name":	#a标签里面class=name
				print link['href']
			else :
				pass #print link['href']
		except KeyError as e:
			pass

if __name__ == '__main__':
	with open('jboss_url.txt') as f:
		for url in f:
			a=url,
			#print a    			 #显示编码里面的换行符
			a1=url.replace('/\n','') #去除编码问题
			b=a1					#换行符没了
			# print b
			geturl(b)
	# geturl()


# key=re.findall('<link>"(.*?)/"</link>',r.text,re.S)
# for each
#  each in key:
# 	print

#爬取FreeBSD 里面的FTP的目录
