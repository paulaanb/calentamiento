f = open("flag.txt", "w")
f.write("Ruben es el mejor profe del mundo mundial<3.")
f.close()

f = open("flag.txt", "r")
print(f.read())
f.close()
#Salida: Ruben es el mejor profe del mundo mundial<3.