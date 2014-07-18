def init():
	jobs = []
	text = open("jobs.txt")
	line = text.readline()
	line = text.readline()
	while line:
		str_line = line.split()
		jobs.append([int(str_line[0]), int(str_line[1])])
		line = text.readline()
	return jobs

def comparator(job1, job2):
	if job1[0] - job1[1] > job2[0] - job2[1]:
		return 1
	elif job2[0] - job2[1] > job1[0] - job1[1]:
		return -1
	else:
		if job1[0] > job2[0]:
			return 1
		elif job1[0] < job2[0]:
			return -1
		else:
			return 0

def run():
	jobs = init()
	jobs = sorted(jobs, cmp = comparator, reverse = True)
	sum = jobs[0][0] * jobs[0][1]
	for index in range(1, len(jobs)):
		jobs[index][1] += jobs[index - 1][1]
		sum += jobs[index][0] * jobs[index][1]
	print sum

run()
