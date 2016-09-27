#coding=utf-8
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':
	with open('jboss_url.txt') as f:
		for url in f:
			# print url,

			# a=url,
			# print a    			 #显示编码里面的换行符
			a1=url.replace('/\n','') #去除编码问题
			print a1
			# b=a1
			# print b
			# 