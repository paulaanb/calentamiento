shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44
if (customer_basket_cost >= 100):
    print("Free shipping")
else:
    shipping_cost = customer_basket_weight * shipping_cost_per_kg
    customer_cost = shipping_cost + customer_basket_cost
    
print ("Total basket cost including shipping is" + str(customer_cost))
shipping_cost_per_kg = 1.20 
customer_basket_cost = 101
customer_basket_weight = 44
if (customer_basket_cost >= 100):
    print("Free shipping")
else:
    shipping_cost = customer_basket_weight * shipping_cost_per_kg
    customer_cost = shipping_cost + customer_basket_cost
    
print ("Total basket cost including shipping is" + str(customer_cost))