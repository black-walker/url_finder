import sys
import re
import urllib2
import urlparse
import os
import time

#version should match with r_con framework
ver="1.0"
currentv = ".".join(map(str, sys.version_info[:3]))
def menu():
	#banner
	os.system("clear")
	print "*"*80
	print "Someone add a banne for me \n"
	print " Mail me at lazysam49@gmail.com\n"
	print "*"*80
	time.sleep(1)
	os.system("clear")

	
def usage():
	print ""
	print "usage -> python " + sys.argv[0] + " (option)"
	print " Available options :"
	print " -h 			                         Display help page\n"
	print " -up 		                         Update urlparser \n" #not yet started
	print " -u=(url)			                 Url of webpage\n"              
	print " -f=(filename))					     Fetch urls from a file\n"
	print " -n 									 New features to be included in next version\n"

def main_check(url):
	tosearch = set([url])
	crawled = set([])
	kdreg = re.compile('<meta\sname=["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')
	lnkreg = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')

	while 1:
		try:
			searching = tosearch.pop()
			print searching
		except KeyError:
			raise StopIteration
		url = urlparse.urlparse(searching)
		try:
			response = urllib2.urlopen(searching)
		except:
			continue
		msg = response.read()
		startPos = msg.find('<title>')
		if startPos != -1:
			endPos = msg.find('</title>', startPos+7)
			if endPos != -1:
				title = msg[startPos+7:endPos]
				print title
		keywordlist = kdreg.findall(msg)
		if len(keywordlist) > 0:
			keywordlist = keywordlist[0]
			keywordlist = keywordlist.split(", ")
			print keywordlist
		links = lnkreg.findall(msg)
		crawled.add(searching)
		for link in (links.pop(0) for _ in xrange(len(links))):
			if link.startswith('/'):
				link = 'http://' + url[1] + link
			elif link.startswith('#'):
				link = 'http://' + url[1] + url[2] + link
			elif not link.startswith('http'):
				link = 'http://' + url[1] + '/' + link
			if link not in crawled:
				tocrawl.add(link)


if len(sys.argv)>1:
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		menu()
		usage()
	elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
		menu()
		print "Current version is :" + ver
		print "-> Required version is 2.X"
		print "-> Current  version  is " + currentv 
	elif sys.argv[1] == "-up" or sys.argv[1] == "--update":
		menu()
		print "*"*80
		print "Will add this new features in r_con framework \n "
		print " keep flooding lazysam49@gmail.com with ur demands \n"
		print "*"*80
	elif sys.argv[1] == "-n" or sys.argv[1] == "--new":
		menu()
		#for survey purpose only
		print "We havnt decided what to add yet \n It is a part of r_con framework \n If u want some function to be added to this mail us at lazysam49@gmail.com"
	else:
		url = sys.argv[1].replace("-u=", "").replace("--url=", "")
		main_check(url)
		if len(url) == 0:
			fname = sys.argv[2].replace("-f=", "").replace("--fname=", "")
			f = open(fname)
			lines = f.readline()
			for line in lines:
				line = url
				print "> looking up in " + url + " :"
				main_check(url)
			f.close()
		else:
			menu()
			main_check(url)	
else:
	menu()
	print "Add some arguments and check requirement.txt \n"
	time.sleep(2)
	print" use pip install -r requirements.txt"
	os.system("clear") 
	print " quiting now!!!!!!!"
	usage()
