import sys

if len(sys.argv) == 3:
	if int(sys.argv[2]) == 0 or int(sys.argv[1]) // int(sys.argv[2]) == 0:
		print("erreur.")
	else:
		print("resultat: %d" % (int(sys.argv[1]) / int(sys.argv[2])))
		print("reste: %d" % (int(sys.argv[1]) % int(sys.argv[2])))
else:
	print("erreur.")