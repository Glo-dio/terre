import sys

i = 0
if len(sys.argv) == 2:
	while i < len(sys.argv[1]):
		print(sys.argv[1][len(sys.argv[1]) - 1 - i], end="")
		i+=1
else:
	print("error.")