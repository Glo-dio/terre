import sys

if len(sys.argv) == 2:
    compteur = 0
    if sys.argv[1][0] == '-' or sys.argv[1][0] == '+':
        print("erreur.")
    elif sys.argv[1].isnumeric() == False:
        for i in sys.argv[1]:
            compteur += 1
        print(compteur)
    else:
        print("erreur.")
else:
    print("erreur.")