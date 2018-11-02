from BeautifulSoup import BeautifulSoup
import time, datetime
import urllib2

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

action = ["GOLL4", "PETR4", "GGBR4"] # Onde seleciona as acoes
t = 0

while t < 1:
	now = datetime.datetime.now()
	for a in action:
		req = urllib2.Request("https://www.google.com/search?q=" + a, headers=hdr)
		pageFile = urllib2.urlopen(req)
		pageHtml = pageFile.read()
		pageFile.close()
		soup = BeautifulSoup("".join(pageHtml))
		for i in soup.findAll("div", {"class": "gsrt"}):
			print "[{}:{}] {}: {} ({}".format(now.hour, now.minute, a, i.text[0:5], i.text.split("(",1)[1] )
	print "\n"
	time.sleep(60)

