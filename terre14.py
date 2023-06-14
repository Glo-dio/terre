import sys

def args_is_digit(len_args):
    for element in range(1, len_args):
        if sys.argv[element].isdigit() != True:
            return False


if len(sys.argv) < 3:
    print("error.")
else :
    i = 1
    for n in range(2,len(sys.argv)):
        if args_is_digit(len(sys.argv)) == False:
            print("error.")
            sys.exit()
        elif (sys.argv[n-i].isdigit() == True and sys.argv[n].isdigit() == True) and int(sys.argv[n-i]) > int(sys.argv[n]):
            print("Pas triée !")
            break
        if n == len(sys.argv) - 1:
            print("Triée !")
