apos = chr(39)+chr(39)+chr(39)

def f(x):
	log = []
	log.append("apos = chr(39)+chr(39)+chr(39)")
	log.append(x)
	log.append(''.join(["	[print(entry) for entry in f(", apos, x , apos,")]"]))
	return log

if __name__ == '__main__':
	
	[print(entry) for entry in f('''
def f(x):
	log = []
	log.append("apos = chr(39)+chr(39)+chr(39)")
	log.append(x)
	log.append(''.join(["	[print(entry) for entry in f(", apos, x , apos,")]"]))
	return log

if __name__ == '__main__':
	''')]