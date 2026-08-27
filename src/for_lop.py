study_hours = [2, 3, 1, 4, 2, 5, 3]
total = 0

for h in study_hours:
    total += h

average = total / len(study_hours)

print("Total de horas:", total)
print("Promedio diario:", round(average, 1))

counter = 0
for h in study_hours:
    if h >= 3:
        counter += 1
print("Días con 3 horas o más:", counter)