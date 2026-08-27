purchase_amount = float(input("Ingrese el monto de la compra: ")) 

if purchase_amount >= 200   : discount = 0.15 
elif purchase_amount >= 100 : discount = 0.10 
else                        : discount = 0 

final_price = purchase_amount - (purchase_amount * discount) 

print(f"Monto original: ${purchase_amount}")
print(f"Descuento aplicado: {int(discount*100)}%") 
print(f"Precio final: ${final_price}")