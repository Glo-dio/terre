import sys

def rac(a,e):
    q = a
    while q - a / q > e:
        q = (q + a / q) // 2
    return int(q)


nb = sys.argv

if len(nb) == 2:
    if nb[1].isdigit() == False or int(nb[1]) < 0:
        print("error.")
    elif nb[1].isdigit() == True:
        print(rac(int(nb[1]),1))
else:
    print("error.")



