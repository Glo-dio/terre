import sys

if len(sys.argv) == 2 and len(sys.argv[1]) == 5:
	if sys.argv[1][0:2].isdigit() == False or int(sys.argv[1][0:2]) > 23:
		print("error.")
	elif sys.argv[1][3:5].isdigit() == False or int(sys.argv[1][3:5]) > 59:
		print("error.")
	elif sys.argv[1][2] != ":":
		print("error.")
	elif int(sys.argv[1][0:2]) > 12:
		print("%02d:%dPM" % (int(sys.argv[1][0:2]) - 12, int(sys.argv[1][3:5])))
	elif int(sys.argv[1][0:2]) == 0:
		print("%02d:%dAM" % (int(sys.argv[1][0:2]) + 12, int(sys.argv[1][3:5])))
	elif int(sys.argv[1][0:2]) == 12:
		print("%02d:%dPM" % (int(sys.argv[1][0:2]), int(sys.argv[1][3:5])))
	else:
		print("%02d:%dAM" % (int(sys.argv[1][0:2]), int(sys.argv[1][3:5])))
else:
	print("error.")