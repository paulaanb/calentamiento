edad = int(input("Introduzca aqui su edad por favor: "))
dinero_inicial = int(2000)
precio_inicial_helado = 100
porcentaje = 1.2
precio_helado_1 = 100*porcentaje
precio_helado_2 = 100*(porcentaje**2)
precio_helado_3 = 100*(porcentaje**3)
precio_helado_4 = 100*(porcentaje**4)
precio_helado_5 = 100*(porcentaje**5)
precio_helado_6 = 100*(porcentaje**6)
precio_helado_7 = 100*(porcentaje**7)
precio_helado_8 = 100*(porcentaje**8)
precio_helado_9 = 100*(porcentaje**9)
precio_helado_10 = 100*(porcentaje**10)
hambre_inicial = int(0 + edad)

if edad>=85:
    print("No tienes la edad suficiente para comer helado, vuelve a intentarlo el año que viene.")
elif edad<0:
    print("Casi pero no Ruben, te quiero :)")
else:
    if precio_inicial_helado<=dinero_inicial and hambre_inicial<=85:
        hambre_inicial = 2*edad
        dinero_inicial = dinero_inicial - precio_inicial_helado
        print ("Esta persona se come 1 helado")
    if precio_helado_2<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 3*edad
       dinero_inicial = dinero_inicial - precio_helado_2
       print ("Esta persona se come 2 helados")  
    if precio_helado_3<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 4*edad
       dinero_inicial = dinero_inicial - precio_helado_3
       print ("Esta persona se come 3 helados") 
    if precio_helado_4<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 5*edad
       dinero_inicial = dinero_inicial - precio_helado_4
       print ("Esta persona se come 4 helados") 
    if precio_helado_5<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 6*edad
       dinero_inicial = dinero_inicial - precio_helado_5
       print ("Esta persona se come 5 helados") 
    if precio_helado_6<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 7*edad
       dinero_inicial = dinero_inicial - precio_helado_6
       print ("Esta persona se come 6 helados") 
    if precio_helado_7<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 8*edad
       dinero_inicial = dinero_inicial - precio_helado_7
       print ("Esta persona se come 7 helados") 
    if precio_helado_8<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 9*edad
       dinero_inicial = dinero_inicial - precio_helado_8
       print ("Esta persona se come 8 helados") 
    if precio_helado_9<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 10*edad
       dinero_inicial = dinero_inicial - precio_helado_9
       print ("Esta persona se come 9 helados") 
    if precio_helado_10<=dinero_inicial and hambre_inicial<=85:
       hambre_inicial = 11*edad
       dinero_inicial = dinero_inicial - precio_helado_10
       print ("Esta persona se come 10 helados")
    if hambre_inicial>100:
       hambre_inicial=100
          
print ("A usted le quedan" + str(dinero_inicial) + "euros y se siente saciado en un" + str(hambre_inicial) + "%")

