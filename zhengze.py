#coding=utf-8
import re
import sys
# from bs4 import BeautifulSoup


def check(url):
	#用来排除掉里面夹杂的其他字符串
	rl = str(url)
	# print rl
	a = re.findall('/download',rl)
	# print len(a)
	if len(a) > 0:
		# print rl
		b=re.findall('600FinalReleaseNotes.txt/download',rl)
		if len(b) == 0:
			# print rl,
			a1 = rl.replace('/download','')  #替换
			print a1,




if __name__ == '__main__':
	with open ('jboss_ture_url.txt') as f:
		for url in f:
			check(url)




