color = (120, 200, 50)

print(color)
print(color[0], color[1], color[2])
print(type(color))

color_a = (120, 200, 50)
color_b = (10, 10, 10)

def calculate_glow(c):
    return sum(c) / 3

glow_a = calculate_glow(color_a)
glow_b = calculate_glow(color_b)

print(f"Brillo A: {round(glow_a, 2)}")
print(f"Brillo B: {round(glow_b, 2)}")

if glow_a > glow_b:
    print("El color A es más brillante")
else:
    print("El color B es más brillante")