teams = [
    ["Los Rayos", 15, 20, 18],
    ["Estrellas FC", 22, 19, 25],
    ["Team Nova", 10, 12, 8],
    ["Halcones", 12, 14, 10],
    ["Titanes", 30, 28, 15],
    ["Fenix", 18, 16, 20],
]

def rate_team(total):
    if total >= 60:
        return "Campeón"
    elif total >= 40:
        return "Finalista"
    else:
        return "Participante"

champion = 'No definido'
champion_score = 0
final_result = (champion, rate_team(champion_score))

for team in teams:
    total = sum(team[1:])
    print(f"{team[0]}: total {total}, {rate_team(total)}")

    if total > champion_score:
        champion = team[0]
        champion_score = total
        final_result = (champion, rate_team(champion_score))

print(f"Equipo con más puntos: {champion}")

champion_bonus_round_score = champion_score
champion_total_bonus_rounds = 0

while champion_bonus_round_score < 70:
    champion_bonus_round_score += 5
    champion_total_bonus_rounds += 1

print(f"Rondas bonus necesarias para llegar a 70: {champion_total_bonus_rounds}")
print(f"Total final tras ronda bonus: {champion_bonus_round_score}")
print(f"Resultado final: {final_result}")