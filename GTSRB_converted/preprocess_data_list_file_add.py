import re
import random

size_list = [10, 20, 50, 75]

train_labels = {30: 0,
193: 1,
40: 2,
79: 3,
75: 4,
41: 5,


210: 7,
211: 8,
212: 9,
213: 10,
214: 11,
216: 12,
217: 13,
225: 14, # speed 50

} 


WIDTH, HEIGHT = 1628, 1236

WD_PATH = 'C:/Users/SOSC2/YOLO/GTSRB_converted/'

G2B = None
with open('label_img/G2B_bak.txt') as f:
	G2B = dict([line.split() for line in f.readlines()])


print('train set begins')

for size in size_list:
	print('size %d begins' % size)
	file_name_to_labels = {}

	for label in range(43):
		b_label = float(G2B[str(label)])
		if b_label not in train_labels:
			continue

		print('class %d begins' % label)	
		with open('../GTSRB/Final_Training/images/%05d/GT-%05d.csv' % (label, label)) as f:
			
			lines = f.readlines()
			lines.pop(0)

			lines = random.sample(lines, min(size, len(lines)))
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

				file_name_to_labels[file_name] = (train_labels[int(G2B[str(label)])], x, y, w, h)


	print('writing train.txt')
	with open('train_%d.txt' % size, 'w') as f:
		for file_name in file_name_to_labels:
			f.write(WD_PATH + 'Final_Training/images/' + file_name + '\n')

	print('writing label files')
	for file_name, labels in file_name_to_labels.items():
		with open('Final_Training/images/' + file_name.replace('.jpg', '.txt'), 'w') as f:
			f.write('%s %f %f %f %f\n' % labels)
			if int(labels[0]) in (7, 8, 9, 10, 11, 12, 13, 14):
				f.write('6 %f %f %f %f\n' % labels[1:])
					


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
