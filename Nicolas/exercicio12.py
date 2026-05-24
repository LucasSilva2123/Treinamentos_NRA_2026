nome : str = input("Nome completo\n");
nome_sem_espacos = nome.replace(" ", "");
primeiro_nome = nome.split(" ")[0];

print(f"Nome = {nome}");
print(f"NOME = {nome.upper()}");
print(f"nome = {nome.lower()}");
print(f"Nº letras = {len(nome_sem_espacos)}");
print(f"Primeiro nome = {primeiro_nome}");
print(f"Nº letras do primeiro nome = {len(primeiro_nome)}")