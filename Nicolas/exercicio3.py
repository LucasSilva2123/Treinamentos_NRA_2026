MAXIMA_PORCENTAGEM_SALARIO = 0.3;

while True:
    try:
        valor_casa = float(input("Qual o valor da casa?\n"));
        n_prestacoes = int(input("Quantas prestações?\n"));
        salario = float(input("Qual seu salário?\n"));
        break;
    except ValueError:
        print("Input inválido, tente novamente");

valor_prestacao : float = valor_casa / n_prestacoes;

if valor_prestacao / salario > MAXIMA_PORCENTAGEM_SALARIO:
    print("O valor da prestação é muito alta. EMPRESTIMO NEGADO");

else:
    print(f"O valor da prestação será: R${valor_prestacao : .2f}. EMPRESTIMO ACEITO");