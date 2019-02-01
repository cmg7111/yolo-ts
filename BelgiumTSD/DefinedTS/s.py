with open('list_defined_TS.txt', 'r') as r:
	with open('ind_to_img.txt', 'w') as w:
		lines = r.readlines()
		assert len(lines) == 420
		for i, line in enumerate(lines):
			if i % 2 == 0:
				w.write(str(int(line) - 1))
				w.write(' ')
			else:
				w.write(line[:-1])
				w.write('\n')
