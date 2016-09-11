from os import walk
from os import listdir
from os.path import isfile, join

directory = '/home/keffbello/Downloads/emp_website/127.0.0.1_8000/peru'
ln = len(directory)

def fix(pagename):	
	depth = len(pagename[ln+1:].split('/'))
	prefix = ''
	for i in range(depth):
		prefix = prefix + '../'
	# Reading and replacing	
	page = open(pagename, 'r')
	lines = page.read()
	lines = lines.replace('http://127.0.0.1:8000', prefix)
	page.close()
	# Writing
	page = open(pagename, 'w')
	page.write(lines)
	page.close()
	

#pagename = 'index.html'
#fix(pagename)


file_paths = [] 

for root, directories, files in walk(directory):
    for filename in files:
    	if filename.endswith('.html'):
 	       filepath = join(root, filename)
 	       file_paths.append(filepath) 

cc = 0
for ff in file_paths:
	if ff.endswith('.html'):
		fix(ff)
		cc += 1
		if cc % 1000 == 0:
			print(cc)


