import os

numbers = []
with open('ind_to_img.txt') as f:
    numbers = dict([pair.split() for pair in f.readlines()])

os.chdir('label_img')

for new, old in numbers.items():
    os.rename(old, new + '.jpg')
