def soma_matrizes (m1, m2):
    # Recebe duas matrizes e caso tenham dimensões iguais e valores interos
    # retorna a soma das duas, caso contrário retorna False 
    
    soma =  []
    col_m1, col_m2 = len(m1), len(m2)
    lin_m1, lin_m2 = len(m1[0]), len(m2[0])

    assert (
        col_m1 == col_m2
        and lin_m1 == lin_m2
        and all(len(linha) == lin_m1 for linha in m1) 
        and all(len(linha) == lin_m2 for linha in m2)
    ), 'Não é possivel somar'
    for i in range(col_m1):
        linha_soma =[]
        for j in range(lin_m1):
            try:
                linha_soma.append(m1[i][j] + m2[i][j])
            except TypeError:
                return False
        soma.append(linha_soma)
    return soma
    
if __name__ == "__main__":
    m1 = [[2, 3, 5], [5, 6, 7]]
    m2 = [[5, 6, 7], [2, 3, 5]]
    m3 = [[1, 2], [4, 5]]


    print(soma_matrizes(m1, m2))
    print(soma_matrizes(m2, m3))