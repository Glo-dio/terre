import sys

def nb_premier(nb):
	i = 2
	if nb <= 1:
		return (print("Non, %d n'est pas un nombre premier." % int(sys.argv[1])))
		
	else:
		while i <= nb / i:
			if nb % i == 0:
				return (print("Non, %d n'est pas un nombre premier." % int(sys.argv[1])))
			i += 1
	return (print("Oui, %d est un nombre premier." % int(sys.argv[1])))


if len(sys.argv) == 2:
	if sys.argv[1].isdigit() == True:
		nb_premier(int(sys.argv[1]))
	else:
		print("error.")
else:
	print("error.")
