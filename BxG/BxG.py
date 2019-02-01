B = 100, 200, 500, 1000, 1500, 2000
G = [10, 20, 50, 75, 100, 200, 500, 1000]

g_list = [open('../GTSRB_converted/train_%d.txt' % name).readlines() for name in G]
b_list = [open('../BelgiumTSD/training_%d.txt' % name).readlines() for name in B]

for b, lb in zip(B, b_list):
	for g, lg in zip(G, g_list):
		with open('training_%d_%d.txt' % (b, g), 'w') as f:
			f.writelines(lb + lg)
