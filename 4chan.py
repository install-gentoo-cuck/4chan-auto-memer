from urllib2 import urlopen
from urllib import urlencode
from random import choice, randint
from string import ascii_lowercase, ascii_uppercase
from time import sleep
import SimpleHTTPServer, SocketServer, thread

with open("captchapage.html", "w") as capHTML:
	fetch = urlopen("http://a.uguu.se/yjlhye_CaptchaPage.html")
	capHTML.write(fetch.read())

class CaptchaServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/captchapage.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
    def log_message(self, format, *args):
    	pass

def createPost(board, threadid, message, captcha, name='Anonymous'):
	url = 'https://sys.4chan.org/%s/post'  % board
	alphanumeric = ascii_lowercase
	alphanumeric += ascii_uppercase
	alphanumeric += '0123456789'
	pwd = ''
	for n in range(32):
		pwd += choice(alphanumeric)
	form = {
		'MAX_FILE_SIZE':'4194304',
		'pwd': pwd,
		'mode':'regist',
		'resto':threadid,
		'email':'',
		'upfile':'',
		'name':name,
		'com':message,
		'g-recaptcha-response': str(captcha)
	}
	data = urlencode(form)
	result = urlopen(url, data=data)
	return result.getcode()

def hostCaptcha():
	handler = CaptchaServer
	serv = SocketServer.TCPServer(("", 8888), handler)
	print 'Visit localhost:8888 for the captcha.'
	serv.serve_forever()
thread.start_new_thread(hostCaptcha, ())

sleep(1)
while True:
	cap = raw_input('Enter a captcha: ')
	cv = ['tips fedora ', 'kill yourself ', 'desu ', 'jew ', 'nigger-rigged ', 'cucked ', 'tfw ', 'ITT: ', 'memed ', 'fizz buzzed ']
	co = ['fedora ', 'jew ', 'nigger ', 'cuck ', 'reddit ', 'tumblr ', 'bane ', 'ITT: ', 'faggot ','meme ', 'autist ', 'waifu ', 'semen demon ', 'fizz buzz ', 'trap ',': the thread ', 'doge ', 'pleb ', 'feel ']
	com = ['a shit', 'fedora tipping ', 'an-heroing ', 'JUST ', 'jew ', 'nigger ', 'cuck ', 'based ', 'reddit-tier ', 'tumblr-tier ', 'baneposting ', 'literally ', 'faggot ','meme ', 'autistic ', 'fizz buzz-tier ', 'shit tier ', 'god tier ',':the thread ', 'pleb ', 'for free ','objectively ' 'tbh ']
	cg = ['Argentina is white', 'jet fuel can\'t melt steel beams','install gentoo', 'ayy lmao', 'it\'s happening', 'REEEEEEEEEEEEEEEEEEEEEEEEEEE', 'huehuehuehuehue', 'umad?', '''>>>/pol/''']
	go = ''
	out = ''
	i=0; j=0; k=0
	while i < randint(3,10):
		out=choice(co)
		while j < randint(2,5):
			out+=choice(com)
			j+=1
		out+=choice(cv) 
		out+= choice(co)
		while k < randint(0,2):
			out+=choice(com)
			k+=1
		go += out + '\n'
		i+=1
	go += choice(cg) + '.'
	go += '\n\n/thread'
	print "R: " + str(createPost('g', '48431348', go, cap))
