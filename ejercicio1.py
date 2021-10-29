def bitcoinToEuros (bitcoin_amount, bitcoin_value_euros): 
   euros_value = bitcoin_amount * bitcoin_value_euros
   if euros_value < 30000:
        print ("Bitcoin amount is going down")
    elif euros_value > 30000:
        print("Bitcoin amount is going up")

    return (euros_value)

def new_func(euros_value):
    return euros_value

bitcoinToEuros(1,25000)

