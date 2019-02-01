import re

WIDTH, HEIGHT = 1628, 1236

WD_PATH = 'C:/Users/SOSC2/YOLO/GTSRB_converted/'

G2B = None
with open('label_img/G2B.txt') as f:
	G2B = dict([line.split() for line in f.readlines()])

file_name_to_labels = {}

print('train set begins')

for label in range(43):
	print('class %d begins' % label)	
	with open('../GTSRB/Final_Training/images/%05d/GT-%05d.csv' % (label, label)) as f:
		
		lines = f.readlines()
		lines.pop(0)

		for line in lines:
			tokens = re.split(';|/', line)

			file_name =  '%05d/' % label + tokens[0].replace('.ppm', '.jpg')

			width = float(tokens[1])
			height = float(tokens[2])

			x1 = float(tokens[3])
			y1 = float(tokens[4])
			x2 = float(tokens[5])
			y2 = float(tokens[6])

			x = (x1 + x2) / 2 / width
			y = (y1 + y2) / 2 / height

			w = (x2 - x1) / width
			h = (y2 - y1) / height

			assert x <= 1 and y <= 1 and w and h <= 1 and label <= 42
			assert x >= 0 and y >= 0 and w >= 0 and h >= 0 and label >= 0

			file_name_to_labels[file_name] = (G2B[str(label)], x, y, w, h)

import random
print('writing train.txt')
with open('train.txt', 'w') as f:
	with open('test.txt', 'w') as f_test:
		for file_name in file_name_to_labels:
			if random.random() < 0.75:
				f.write(WD_PATH + 'Final_Training/images/' + file_name + '\n')
			else:
				f_test.write(WD_PATH + 'Final_Training/images/' + file_name + '\n')
# print('writing label files')
# for file_name, labels in file_name_to_labels.items():
# 	with open('Final_Training/images/' + file_name.replace('.jpg', '.txt'), 'w') as f:
# 		f.write('%s %f %f %f %f\n' % labels)


# file_name_to_labels = {}

# print('test set begins')

# if True:
# 	with open('../GTSRB/Final_Test/images/GT-final_test.test.csv') as f:
		
# 		lines = f.readlines()
# 		lines.pop(0)
		
# 		for line in lines:
# 			tokens = re.split(';|/', line)

# 			file_name =  tokens[0].replace('.ppm', '.jpg')

# 			width = float(tokens[1])
# 			height = float(tokens[2])

# 			x1 = float(tokens[3])
# 			y1 = float(tokens[4])
# 			x2 = float(tokens[5])
# 			y2 = float(tokens[6])

# 			label = tokens[7]

# 			x = (x1 + x2) / 2 / width
# 			y = (y1 + y2) / 2 / height

# 			w = (x2 - x1) / width
# 			h = (y2 - y1) / height

# 			assert x <= 1 and y <= 1 and w and h <= 1 and label <= 42
# 			assert x >= 0 and y >= 0 and w >= 0 and h >= 0 and label >= 0

# 			file_name_to_labels[file_name] = (G2B[str(label)], x, y, w, h)

# print('writing test.txt')
# with open('test.txt', 'w') as f:
# 	for file_name in file_name_to_labels:
# 		f.write(WD_PATH + 'Final_Test/images/' + file_name + '\n')

# print('writing label files for test data')
# for file_name, labels in file_name_to_labels.items():
# 	with open('Final_Test/images/' + file_name.replace('.jpg', '.txt'), 'w') as f:
# 		f.write('%s %f %f %f %f\n' % labels)

# print('finished')
