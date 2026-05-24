def leiaInt(input_texto : str) -> int:
    while True:
        try:
            n = int(input(input_texto));
            return n;
        except ValueError:
            print("Input inválido, tente novamente");

n_jogadores = leiaInt("Número de jogadores = ");

jogadores : list = []

for i in range(n_jogadores):
    jogador = {};

    nome = input("Nome = ");
    n_jogos = leiaInt("Número de jogos = ");

    gols : list = []
    for i in range(n_jogos):
        gols_no_jogo = leiaInt(f"Gols feito no {i+1}º jogo = ");
        gols.append(gols_no_jogo)

    jogador["Nome"] = nome;
    jogador["Numero de jogos"] = n_jogos;
    jogador["Gols"] = gols;

    jogadores.append(jogador);

total_gols : int = 0;

for jogador in jogadores:
    print(jogador);
    total_gols += sum(jogador["Gols"]);

print(f"O time fez {total_gols} gols");