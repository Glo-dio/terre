import sys

try:
	if len(sys.argv) == 2:	
		if int(sys.argv[1]) % 2 == 0:
			print("pair")
		else:
			print("impair")
	else:
		print("Tu ne me la mettras pas à l'envers.")
except ValueError:
	print("Tu ne me la mettras pas à l'envers.")