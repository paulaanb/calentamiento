bitcoin_amount = float(input("Introduzca aquí por favor la cantidad de BTC que tiene usted actualmente: "))
bitcoin_value_euros = float(input("Introduzca aquí por favor el valor actual de 1 BTC/EUR: "))

def BitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value
investment_in_euros = BitcoinToEuros(bitcoin_amount, bitcoin_value_euros)

if investment_in_euros <= 30000:
    print("¡Su inversión está por debajo de 30,000 euros! Le recomendamos vender inmediatamente.")
else:
    print("Su inversión está por encima de 30,000 euros. ¡Enhorabuena!")

#Output:¡Su inversión está por debajo de 30,000 euros! Le recomendamos vender inmediatamente. 
