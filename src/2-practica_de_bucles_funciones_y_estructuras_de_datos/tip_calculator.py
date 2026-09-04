import math

bill_amount = float(input("Ingrese el monto de la cuenta: ")) 
customers_amount = int(input("Ingrese la cantidad de personas: ")) 

if bill_amount < 20                             : tip_percentage = 0.10 
elif bill_amount >= 20 and bill_amount <= 50    : tip_percentage = 0.15
elif bill_amount > 50                           : tip_percentage = 0.20

if customers_amount > 4: tip_percentage += 0.05

tip                     = bill_amount * tip_percentage
total_payment           = bill_amount + tip
payment_by_customers    = total_payment / customers_amount

ceiled_tip                  = math.ceil(tip* 100) / 100
ceiled_total_payment        = math.ceil(total_payment* 100) / 100
ceiled_payment_by_customers = math.ceil(payment_by_customers* 100) / 100

print(f"Propina: ${ceiled_tip}")
print(f"Total a pagar: ${ceiled_total_payment}")
print(f"Cada persona paga: ${ceiled_payment_by_customers}")