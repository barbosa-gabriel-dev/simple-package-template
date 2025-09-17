def imprime_matriz(minha_matriz):
    # Recebe uma matriz como parâmetro
    # e imprime a matriz linha por linha
    
    for lista in minha_matriz:
        for i in range(len(lista)):
            if i < len(lista)-1:
                print(lista[i], end=" ")
            else:
                print(lista[i], end="")
        print()