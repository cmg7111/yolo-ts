import re

WD_PATH = '/content/drive/dataset/'

WIDTH, HEIGHT = 1628, 1236

bin_num = 50
bin_size = 1 / bin_num
bin_func = lambda x: max(int(x * bin_num) - 1, 0)

img_list_files = ['training', 'testing']

counter = dict()
sums = [0, 0, [0] * bin_num, [0] * bin_num]
for idx, img_list_file_name in enumerate(img_list_files):
	print(img_list_file_name + ' begins')

	with open('BelgiumTSD_annotations/BTSD_%s_GTclear.txt' % (img_list_file_name,)) as f:
		lines = f.readlines()
		for line in lines:
			tokens = re.split(';|/', line)

			file_name = tokens[1].replace('.jp2', '.jpg')
			label = int(tokens[6])

			x1 = float(tokens[2])
			y1 = float(tokens[3])
			x2 = float(tokens[4])
			y2 = float(tokens[5])

			w = (x2 - x1) / WIDTH
			h = (y2 - y1) / HEIGHT
			s = min(w, h)
			bin_idx = bin_func(s)

			count = counter.get(label, [0, 0, list(), [0] * bin_num, [0] * bin_num])
			count[idx] += 1
			count[2].append(file_name)

			count[idx + 3][bin_idx] += 1

			counter[label] = count

			sums[idx] += 1
			sums[idx + 2][bin_idx] += 1

items = counter.items()
items = sorted(items, key=lambda pair: pair[1][0])

for k, v in items:
	print('%d: %s, small: %s, %s' % (k - 1, v[:2], v[3][:5], v[4][:5]))

a = list()
for k, v in items:
	a.append((k - 1, v[0]))
	print('%d; %d' % (k - 1, v[0]))

a = sorted(a, key=lambda pair: pair[0])
for pair in a:
	print('%d; %d' % pair)


print('total:' + str(sums))

for k, v in counter.items():
	with open('class_label/%d.txt' % (k,), 'w') as label_f:
		for file_name in v[2]:
			label_f.write(WD_PATH + file_name + '\n')


