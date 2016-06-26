# coding: utf8
#!/usr/bin/python

import getopt
import sys

def usage():
	print "usage:"
	print "-l, --long, -s, --simple后面必须跟参数"
	print '-a, -b, -c, --abc, --cba, --bac 后面绝对不能带参数'
	sys.exit(0)

def main():
	if not len(sys.argv[1:]):
		usage()

	try:
		opts, args = getopt.getopt(sys.argv[1:], "l:s:abc",["long", "simple", "abc", "bac", "cba"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	print opts, args

	print u'请输入数据, 退出输入： CRTL-D'
	buffer = sys.stdin.read()

	print u'你输入的是：', buffer

main()
