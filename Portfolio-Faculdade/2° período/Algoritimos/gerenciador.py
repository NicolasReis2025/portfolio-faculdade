def adicionar_lista(lista, variavel):
    lista.append(variavel)
    return lista

nomes = []
idades = []

while True:
    print(
        "\n[1] Adicionar pessoa\n" 
        "[2] mostrar pessoas\n" 
        "[3] Classificar por faixa etária\n" 
        "[4] Procurar pessoa\n" 
        "[0] Sair\n")

    try: 
        opcao = int(input("Digite uma opção: "))

    except ValueError:
        print("Digite apenas numeros!") 
        continue   

    if opcao == 0:
        print("programa encerrado!")   
        break

    if opcao == 1:
        nome = str(input("Digite um nome: ")).lower()
        
        if nome in nomes:
            print(f"O nome {nome} já está na lista!")
        else: 
            try:   
                idade = int(input(f"Digite a idade de(a) {nome}: "))
                adicionar_lista(nomes, nome)
                adicionar_lista(idades, idade)
            except ValueError:
                print("Digite apenas números para a idade.")    
        
    if opcao == 2:
        for pessoa, idade in zip(nomes, idades):
            print(f"\nNome: {pessoa} | Idade: {idade}")
    
    if opcao == 3:
        criancas, adolescentes, adultos, idosos = [], [], [], []
    
        for indice, idade in enumerate(idades):  
            nome = nomes[indice]

            if idade <= 12:
                criancas.append(nome)

            elif 13 <= idade <= 17:
                adolescentes.append(nome)

            elif 18 <= idade <= 59:
                adultos.append(nome)

            else:
                idosos.append(nome)

        print("\n=== Classificação por Faixa Etária ===")
        print(f"Crianças: {criancas}")
        print(f"Adolescentes: {adolescentes}")
        print(f"Adultos: {adultos}")
        print(f"Idosos: {idosos}")
    
    if opcao == 4:
        buscar_nome = str(input("Digite o nome: ")).lower()        
        if buscar_nome in nomes:
            print(f"O nome {buscar_nome} foi encontrado!")
        else:
            print(f"O nome {buscar_nome} não foi encontrado!")    






