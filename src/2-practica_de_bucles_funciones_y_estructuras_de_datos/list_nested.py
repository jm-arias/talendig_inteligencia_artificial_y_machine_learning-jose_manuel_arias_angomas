seats = [
    ["L", "X", "L"],
    ["X", "X", "L"],
    ["L", "L", "X"],
]

print(seats[0])
print(seats[1][2])

for row in seats:
    print(row)

agents_sales = [
    ["Marta", 320, 450, 275],
    ["Julio", 180, 200, 210],
]

for agent in agents_sales:
    nombre = agent[0]
    ventas = agent[1:]
    total = sum(ventas)
    print(f"{nombre}: total de ventas ${total}")