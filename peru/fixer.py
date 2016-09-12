from os import walk
from os import listdir
from os.path import isfile, join

directory = '/home/keffbello/Downloads/emp_website/empleatron.github.io/peru'
ln = len(directory)

def fix(pagename):	
	depth = len(pagename[ln+1:].split('/')) - 1
	prefix = ''
	for i in range(depth):
		prefix = prefix + '../'
	# Reading and replacing	
	page = open(pagename, 'r')
	lines = page.read()
	print("FIXING:", pagename[ln+1:], prefix)
	lines = lines.replace('http://127.0.0.1:8000', prefix)
	lines = lines.replace('<li><a href="' + prefix + 'nosotros/index.html"       > Nosotros</a></li>', '')
	lines = lines.replace('<li><a href="' + prefix + 'index.html"               > Inicio</a></li>', '')
	lines = lines.replace('<li><a href="' + prefix + 'soluciones/index.html"           > Soluciones</a></li>', '')
	lines = lines.replace('<li class="has-sub"><a href="' + prefix + 'panorama/index.html"> Panorama Laboral</a>', '')
	lines = lines.replace('<li><a href="' + prefix + 'contacto/index.html"   > Contacto</a></li>', '')
	lines = lines.replace('<li><a href="' + prefix + 'panorama/demanda-laboral/index.html">Panorama de la demanda laboral peruana</a></li>', '')
	lines = lines.replace('<li><a href="' + prefix + 'panorama/interrelacion-carreras.html">Interrelación entre carreras en el Perú</a></li>', '')
	#lines = lines.replace('', '')
	#lines = lines.replace('', '')


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


