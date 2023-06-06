import sys

letter = sys.argv[1]
for l in range(ord(letter), 123):
	print(chr(l), end="")
print()
