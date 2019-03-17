import itertools
x = ["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
z = 0
while z < 1:
	z += 1
	with open("country.txt", "r") as f1:
		for cn,s in itertools.product(f1,x):
			if cn[:1].lower() == s:
				if z == 0:
					with open(s +".txt", "w") as f2:
						f2.write(cn)
				else:
					with open(s +".txt", "a") as f2:
						f2.write(cn)


