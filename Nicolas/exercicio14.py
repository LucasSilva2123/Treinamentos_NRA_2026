def is_palindromo(texto : str) -> bool:
    texto_normalizado = texto.lower().replace(" ", "")

    for i in range(len(texto_normalizado) // 2):
        if texto_normalizado[i] != texto_normalizado[len(texto_normalizado) - i - 1]:
            return False;

    return True

texto = input("Texto:\n");

print(f"{"É palindromo" if is_palindromo(texto) else "Não é palindromo"}")

