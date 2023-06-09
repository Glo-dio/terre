import sys

i = 0
if len(sys.argv) == 2:
	print(sys.argv[1][::-1])
else:
	print("error.")