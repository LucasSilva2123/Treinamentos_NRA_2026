total = 0;
for i in range(6):
    while True:
        try:
            n = int(input(f"{i} = "));
            break;
        except:
            print("Input inválido, tente novamente")
    
    if n % 2 == 0:
        total += n;

print(f"Total = {total}");