shipping_cost_per_kg = 1.20
customer_basket_cost = float(input("Introduzca aqui el precio de su cesta por favor:"))
customer_basket_weight = float(input("Indroduzca aqui el peso de su envio por favor:"))

if customer_basket_cost < 0 or customer_basket_weight <= 0:
    print("Los datos introducidos no son correctos, intentelo de nuevo mas tarde.")
else:
    if (customer_basket_cost >= 100):
        print ("¡Usted tiene envio gratis! El precio total de su pedido es de" + str(customer_basket_cost) + "euros")
    else:
        shipping_cost = customer_basket_weight * shipping_cost_per_kg
        customer_cost = shipping_cost + customer_basket_cost
        print ("El precio total de su pedido asciende a la cantidad de" + str(customer_cost) + "euros")

#Salida:¡Usted tiene envio gratis! El precio total de su pedido es 101 euros.
#Si el valor introducido es <100 el mensaje sera el mismo mas la suma del coste envio. 