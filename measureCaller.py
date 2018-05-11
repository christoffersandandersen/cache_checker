import os
import matplotlib.pyplot as plt

file_name = 'out.txt'
size_limit = 64000


def open_file(file_name):
	try:
		file_handle = open(file_name)
	except Exception as e:
		print "Error: ", e

	return file_handle


def parse_file(file_handle):
	lines = file_handle.readlines()
	user_time = lines[2]
	user_time = float(user_time[user_time.find('m')+1:len(user_time)-2])
	
	sys_time = lines[3]
	sys_time = float(sys_time[sys_time.find('m')+1:len(sys_time)-2])	

	total_time = user_time + sys_time

	return total_time





# We will just start with a file size of one kb
file_size = 1
times = list()
sizes = list()
while file_size <= size_limit:
	os.system('echo | (time ./cacheMeasure ' + str(file_size) + ' ) &> ' + file_name)
	sizes.append(file_size)
	file_size *= 2
	file_handle = open_file(file_name)
	times.append(parse_file(file_handle))


plt.plot(sizes, times)
plt.ylabel('Time in s')
plt.xlabel('Size in kb')
plt.show()
#print times, "\n", sizes