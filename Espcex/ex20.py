time = []
jogador = {}
while True:
    jogador['Nome'] = str(input("Digite o nome do jogador: ")).strip().title()
    jogador['Partidas'] = int(input("Digite quantas partidas o jogador jogou: "))
    gols = []
    for n in range(0, jogador['Partidas']):
        gols.append(int(input(f'Digite o números de gols na partida {n + 1}: ')))
    jogador['Gols'] = gols[:]
    jogador['TotalGols'] = sum(gols)
    time.append(jogador.copy())
    continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()
    if continuar == 'N':
        break
print(time)
print()
for c, v in enumerate(time):
    print(f'O jogador {v['Nome']} jogou {v['Partidas']} partidas.')
    for p, g in enumerate(v['Gols']):
        print(f'Na partida {p + 1} fez {g} gols.')
    print(f'Fez um total de {v['TotalGols']} gols.')
    print()
total = 0
for v in time:
    total += v['TotalGols']
print(f'O time marcou um total de {total} gols.')