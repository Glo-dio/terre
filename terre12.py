import sys

if len(sys.argv) == 2 and len(sys.argv[1]) == 7:
	if sys.argv[1][0:2].isdigit() == False or int(sys.argv[1][0:2]) > 12:
		print("error.1")
	elif sys.argv[1][3:5].isdigit() == False or int(sys.argv[1][3:5]) > 59:
		print("error.2")
	elif sys.argv[1][2] != ":":
		print("error.3")
	elif sys.argv[1][5:7] != "AM" and sys.argv[1][5:7] != "PM":
		print("error.4")
	elif int(sys.argv[1][0:2]) == 12 and sys.argv[1][5:7] == "AM":
		print("%02d:%02d" % (int(sys.argv[1][0:2]) - 12, int(sys.argv[1][3:5])))
	elif int(sys.argv[1][0:2]) == 12 and sys.argv[1][5:7] == "PM":
		print("%02d:%02d" % (int(sys.argv[1][0:2]), int(sys.argv[1][3:5])))
	elif sys.argv[1][5:7] == "PM":
		print("%02d:%02d" % (int(sys.argv[1][0:2]) + 12, int(sys.argv[1][3:5])))
	else:
		print("%02d:%02d" % (int(sys.argv[1][0:2]), int(sys.argv[1][3:5])))
else:
	print("error.")
