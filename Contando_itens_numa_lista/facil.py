# http://www.practicepython.org/solution/2014/12/14/22-read-from-file-solutions.html

counter_dict = {}
with open('nameslist.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)