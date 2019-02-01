import re

map_str = """0 2 : 110
1 6 : 53
2 11 : 166
3 25 : 119
4 30 : 337
5 33 : 159
6 34 : 81
7 38 : 126
8 40 : 320
9 41 : 383
10 49 : 57
11 56 : 157
12 60 : 120
13 64 : 837
14 74 : 51
15 75 : 371
16 78 : 100
17 79 : 285
18 80 : 196
19 81 : 242
20 83 : 148
21 86~100 
22 117
23 150"""

lines = map_str.split('\n')
terms = [line.split(' ') for line in lines]
train_labels = {term[1]: term[0] for term in terms}
train_labels.pop('86~100')
for i in range(86, 101):
	train_labels[i] = 21

train_labels = {int(k): int(v) for k, v in train_labels.items()}

print(train_labels)


# train_labels = {30: 0,
# 193: 1,
# 40: 2,
# 79: 3,
# 75: 4,
# 41: 5,

# 64: 6, # speed general
# } 

WIDTH, HEIGHT = 1628, 1236

WD_PATH = 'C:/Users/SOSC2/YOLO/dataset/'

img_list_files = ['training', 'testing']

bin_num = 50
bin_size = 1 / bin_num
bin_func = lambda x: max(int(x * bin_num) - 1, 0)


for img_list_file_name in img_list_files:
	print(img_list_file_name + ' begins')

	file_name_to_labels = {}
	small_labels_files = {}
	with open('BelgiumTSD_annotations/BTSD_%s_GTclear.txt' % (img_list_file_name,)) as f:
		
		lines = f.readlines()
		for line in lines:
			tokens = re.split(';|/', line)

			file_name = tokens[1].replace('.jp2', '.jpg')

			x1 = float(tokens[2])
			y1 = float(tokens[3])
			x2 = float(tokens[4])
			y2 = float(tokens[5])

			label = int(tokens[6])

			if label == -1:
				continue

			label -= 1

			if label not in train_labels:
				continue

			label = train_labels[label]


			x = (x1 + x2) / 2 / WIDTH
			y = (y1 + y2) / 2 / HEIGHT

			w = (x2 - x1) / WIDTH
			h = (y2 - y1) / HEIGHT

			s = min(w, h)
			bin_idx = bin_func(s)

# 0.012328 0.049806
# 0.015504 0.027484
# 0.042623 0.074854


			assert x <= 1 and y <= 1 and w <= 1 and h <= 1 and label <= 23
			assert x >= 0 and y >= 0 and w >= 0 and h >= 0 and label >= 0

			labels = file_name_to_labels.get(file_name, [])
			labels.append((label, x, y, w, h))
			file_name_to_labels[file_name] = labels

			if img_list_file_name == 'testing' and bin_idx == 0:
				labels = small_labels_files.get(file_name, [])
				labels.append((label, x, y, w, h))
				small_labels_files[file_name] = labels

		with open(img_list_file_name + '.txt', 'w') as img_list_f:
			for file_name in file_name_to_labels:
				img_list_f.write(WD_PATH + file_name + '\n')

		if img_list_file_name == 'testing':
			with open('small_testing.txt', 'w') as img_list_f:
				for file_name in small_labels_files:
					img_list_f.write(WD_PATH + file_name + '\n')

		print('file list finished')

		for file_name, labels in file_name_to_labels.items():
			with open('../dataset/' + file_name.replace('.jpg', '.txt'), 'w') as file_label_f:
				for label in labels:
					file_label_f.write('%d %f %f %f %f\n' % label)

		print('label files finished')

	print(img_list_file_name + ' finishes')
