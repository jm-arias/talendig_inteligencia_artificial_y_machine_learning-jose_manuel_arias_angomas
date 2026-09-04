def calculate_shipping_costs(peso, distancia):
    cost = peso * 0.5 + distancia * 0.1
    return cost

result = calculate_shipping_costs(12, 80)
print(f"Costo: {round(result, 2)}")

def rate_shipping(costo):
    if costo < 10:
        return "Económico"
    elif costo < 25:
        return "Estándar"
    else:
        return "Premium"
    
print(rate_shipping(result))