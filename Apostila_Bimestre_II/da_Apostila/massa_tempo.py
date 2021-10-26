massai = 0.0; massaf = 0.0; hs = 0; min = 0; seg = 0
massai = float(eval(input("Entre com a massa inicial (em gramas):\n")))
massaf = massai
while (massaf >= 0.05):
		massaf = massaf / 2
		seg = seg + 50
		
hs = seg // 3600
seg = seg % 3600
min = seg // 60
seg = seg % 60
print(" ="*13,"\n")	
print(" Massa inicial: %.2fg\n Massa final: %.2fg\n Tempo: %d:%d:%d" % (massai, massaf, hs, min, seg))	
print("\n","= "*13)