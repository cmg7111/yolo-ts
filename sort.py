lines = []
with open('결과 2400_german.txt') as f:
	lines = f.readlines()

lines.pop(0)
lines.pop(0)
lines.pop(0)

lines.pop(-1)
lines.pop(-1)
lines.pop(-1)
lines.pop(-1)
lines.pop(-1)

sorted_lines = sorted(lines, key=lambda line: float(line.split()[-2]))

with open('sorted result.txt', 'w') as f:
	f.writelines(sorted_lines)