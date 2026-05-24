while True:
    while True:
        try:
            n = int(input("n = ")); 
            break;
        except ValueError:
            print("Input inválido, tente novamente");

    if n < 0:
        break;

    for i in range(1, 16):
        print(f"{n} x {i} = {n * i}");