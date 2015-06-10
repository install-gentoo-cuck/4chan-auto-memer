from random import choice, randint
chanVerbs = ['tips fedora ', 'kill yourself ', 'desu ', 'jew ', 'nigger-rigged ', 'cucked ', 'tfw ', 'ITT: ', 'memed ', 'fizz buzzed ']
chanObjects = ['fedora ', 'jew ', 'nigger ', 'cuck ', 'reddit ', 'tumblr ', 'bane ', 'ITT: ', 'faggot ','meme ', 'autist ', 'waifu ', 'semen demon ', 'fizz buzz ', 'trap ',': the thread ', 'doge ', 'pleb ', 'feel ']
chanObjectModifiers = ['a shit', 'fedora tipping ', 'an-heroing ', 'JUST ', 'jew ', 'nigger ', 'cuck ', 'based ', 'reddit-tier ', 'tumblr-tier ', 'baneposting ', 'literally ', 'faggot ','meme ', 'autistic ', 'fizz buzz-tier ', 'shit tier ', 'god tier ',':the thread ', 'pleb ', 'for free ','objectively ']
chanGarbage = ['Argentina is white', 'jet fuel can\'t melt steel beams','install gentoo', 'ayy lmao', 'it\'s happening', 'REEEEEEEEEEEEEEEEEEEEEEEEEEE', 'huehuehuehuehue', 'umad?', '''>>>/pol/''']
	
out = ''
i=0; j=0; k=0
while i < randint(3,10):
	out=choice(chanObjects)
	while j < randint(2,5):
		out+=choice(chanObjectModifiers)
		j+=1
	out+=choice(chanVerbs) 
	out+= choice(chanObjects)
	while k < randint(0,2):
		out+=choice(chanObjectModifiers)
		k+=1
	print out, '.',
	i+=1
print choice(chanGarbage), '.',
print '\n/thread'
