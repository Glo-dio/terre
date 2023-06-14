import sys

if len(sys.argv) == 4:
    if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False or sys.argv[3].isdigit() == False:
        print("error.")
    elif int(sys.argv[1]) == int(sys.argv[2]) or int(sys.argv[2]) == int(sys.argv[3]) or int(sys.argv[1]) == int(sys.argv[3]):
        print("error.")
    elif int(sys.argv[1]) < int(sys.argv[2]) and int(sys.argv[2]) < int(sys.argv[3]):
        print(int(sys.argv[2]))
    elif int(sys.argv[1]) < int(sys.argv[2]) and int(sys.argv[2]) > int(sys.argv[3]):
        if int(sys.argv[1]) < int(sys.argv[3]):
            print(int(sys.argv[3]))
        else:
            print(int(sys.argv[1]))
    elif int(sys.argv[1]) > int(sys.argv[2]) and int(sys.argv[2]) < int(sys.argv[3]):
        if int(sys.argv[1]) > int(sys.argv[3]):
            print(int(sys.argv[3]))
        else:
            print(int(sys.argv[1]))
    elif int(sys.argv[1]) > int(sys.argv[2]) and int(sys.argv[2]) > int(sys.argv[3]):
        print(int(sys.argv[2]))
else:
    print("error.")