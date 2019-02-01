size_list = [100, 200, 500, 1000, 1500]

with open('training_2000.txt') as f:
	lines = f.readlines()
	import random
	for size in size_list:
		lines_sample = random.sample(lines, size)
		with open('training_%d.txt' % size, 'w') as f_write:

			f_write.writelines(lines_sample)