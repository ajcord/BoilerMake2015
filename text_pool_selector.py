import numpy as np

def getRandomQuote():
	file = open("text_pool.txt")
	num_lines = sum(1 for line in file)
	randChoice = np.random.randint(0,num_lines-1)
	i = 0
	file.close()
	file = open("text_pool.txt")
	while(i < randChoice):
		lo = file.readline()
		i += 1
	returnline = file.readline()[0:-1]
	return returnline

print getRandomQuote()