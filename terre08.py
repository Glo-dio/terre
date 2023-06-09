import sys

if len(sys.argv) == 3:
    if sys.argv[2][0] == "-" or sys.argv[2].isalpha() == True or sys.argv[1].isalpha() == True:
        print("error.")
    if sys.argv[1][0].isdigit() == False and sys.argv[2][0].isdigit() == True:
        print("error.")
    elif sys.argv[1][0] == "-" and sys.argv[1][1].isdigit() == True:
        print(int(sys.argv[1]) ** int(sys.argv[2]))
    elif sys.argv[1].isdigit() == True and sys.argv[2].isdigit() == True:
        print(int(sys.argv[1]) ** int(sys.argv[2]))
    else:
        print("error.")
else:
	print("error.")