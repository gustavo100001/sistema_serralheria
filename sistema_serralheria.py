while True:
    print("\n\n\n --Sistema de gerenciamento para serralheria--\n")
    
    print(" Menu de opções \n")
    
    print(" 1. Checklist de ferramentas:")
    print("\n 2. Calcular material e serviço:")
    print("\n 3. Organizar cortes:")
    print("\n 4. Sair:\n")
    
    print("-----------------------------------------------")
    opção = input(" Digite o número de uma opção do menu: ")

    # Primeira opção do menu
    if opção == "1":
        lista_ferramentas = ["solda", "lixadeira", "furadeira", "extensão", "manuais"] # lista dos itens
        faltando = [] # variável com lista para guardar oque está faltando

        print("\n -- Checklist de ferramentas no carro -- \n")

        for x in lista_ferramentas: # loop para perguntar sobre cada ferramenta da lista de itens
            resposta = input(f"A ferramenta: {x} está no carro, s(sim) ou n(não) ? ") # pede sim ou não e guarda na resposta
            if resposta == "n": # se for n faça isso
                faltando.append(x) # anexe(cole) esse x (iten) na lista faltando, o append significa guardar ou gravar

        if len(faltando) == 0: # len é para contar ou verificar cada iten da lista
                print("\n Está tudo no carro! \n")
        else:
                itens_faltando = ", ".join(faltando) # join junta os itens faltando a frase separando com a virgula q foi definida
                print(f"\n Pegue a(o) {itens_faltando} e coloque no carro! \n")

    # Segunda opção do menu
    elif opção == "2":
        
        print("\n -- Calcular material e serviço --\n")
        
        custo_total = 0.0 

        while True: # loop para inserir os nomes e preços dos mateiais
            nomes = input("\n Nome do material: ")
            precos = float(input("\n Valor dos materiais R$: "))
            custo_total += precos # onde ocorre a soma dos preços
            continuar = input("\n Inserir mais material, sim ou não? ")
            if continuar in ["não", "nao", "n"]:
                preco_venda = custo_total * 2 # calculo de porcentagem da mão de obra
                print(f"\n Custo total de materiais: {custo_total:.2f}")
                print(f" Custo de venda total: {preco_venda:.2f}\n")
                break
    
    # terceira opção
    elif opção == "3":
        
        print("\n -- Organizar cortes -- ")
        
        cortes = [] 

        while True: # esse while é um loop para controlar os cm que o usuario ira escrever
            cortando = input("\n Insira o tamanho em centimetros do corte atual: ")
            cortes.append(cortando) # esse append anexa os cortes do usuario na lista (cortes)
            continuar = input(" Vai continuar cortando, sim ou não? ")

            if continuar == "não":
                tamanhos = ", ".join(cortes)
                print(f"\n Todos os tamanhos cortados são esses: {tamanhos}")
                break # este break finaliza o loop quando digita 0
            
    elif opção == "4":
        
        print("\n Saindo do sistema...\n")
        break
        
       

        
