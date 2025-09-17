def multiplica_matrizes (m1, m2):

    # Recebe duas matrizes e caso tenham dimensões iguais e valores interos
    # retorna a soma das duas, caso contrário retorna False 

    num_colunas_m1, num_linhas_m1 = len(m1), len(m1[0])
    num_colunas_m2, num_linhas_m2 = len(m2), len(m2[0])  


    assert num_colunas_m1 == num_linhas_m2, 'Não é possivel realizar a operação'
    vet_multiplicação =  []

    for linha in range(num_linhas_m1):
        vet_multiplicação.append([])
        for coluna in range(num_colunas_m2):
            vet_multiplicação[linha].append(0)
            for i in range(num_colunas_m1):
                vet_multiplicação[linha][coluna] += m1[linha][i] * m2[i][coluna]




if __name__ == "__main__":
    m1 = [[2, 3, 5],
          [5, 6, 7],
          [8, 9, 10]]
    
    m2 = [[8, 9, 10],
          [5, 6, 7],
          [2, 3, 5]]
    



    print(multiplica_matrizes(m1, m2))