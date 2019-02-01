import re

WD_PATH = '/content/drive/dataset/'

img_list_files = ['training', 'testing']
counter = dict()
sums = [0, 0]
for idx, img_list_file_name in enumerate(img_list_files):
	print(img_list_file_name + ' begins')

	with open('BelgiumTSD_annotations/BTSD_%s_GTclear.txt' % (img_list_file_name,)) as f:
		lines = f.readlines()
		for line in lines:
			tokens = re.split(';|/', line)

			file_name = tokens[1].replace('.jp2', '.jpg')
			label = int(tokens[6])

			count = counter.get(label, [0, 0, list()])
			count[idx] += 1
			count[2].append(file_name)
			counter[label] = count

			sums[idx] += 1

for k, v in counter.items():
	print('%d: %s' % (k, v[:2]))

print('total:' + str(sums))

for k, v in counter.items():
	with open('class_label/%d.txt' % (k,), 'w') as label_f:
		for file_name in v[2]:
			label_f.write(WD_PATH + file_name + '\n')