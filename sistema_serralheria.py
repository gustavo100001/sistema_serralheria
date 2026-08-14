banco_usuarios = []
usuarios_logados = None

def cadastro_usuarios():

                print("\n -- Cadastro de Usuários --")

       
                nome = input("\n Insira seu nome: ")
                
                cpf = input(" Digite seu CPF(será seu usuario de acesso): ")
                
                senha = input(" Crie uma senha de acesso: ")

                novo_usuario = {"nome": nome, "cpf": cpf, "senha": senha}
                banco_usuarios.append(novo_usuario)

def checklist_ferramentas():
        
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


def calcular_material_servico():

        print("\n -- Calcular material e serviço --\n")
        
        
        custo_total = 0.0 

        while True: # loop para inserir os nomes e preços dos mateiais
                nomes = input("\n Nome do material: ")

                try: 
                        precos = float(input("\n Valor dos materiais R$: ").replace(",", "."))
                except ValueError:
                        print("Valor invalido, tente novamente!")
                        continue
                
                custo_total += precos # onde ocorre a soma dos preços
                continuar = input("\n Inserir mais material, sim ou não? ")
                if continuar in ["não", "nao", "n"]:
                        preco_venda = custo_total * 2 # calculo de porcentagem da mão de obra
                        print(f"\n Custo total de materiais: {custo_total:.2f}")
                        print(f" Custo de venda total: {preco_venda:.2f}\n")
                        break

def organizar_cortes():
        
        print("\n -- Organizar cortes -- ")
        
        cortes = [] 

        while True: # esse while é um loop para controlar os cm que o usuario ira escrever
            try:
                cortando = float(input("\n Insira o tamanho em centimetros do corte atual: ").replace(",", "."))
            except ValueError:
                print("Valor invalido, tente novamente!")
                continue
                            
            cortes.append(cortando) # esse append anexa os cortes do usuario na lista (cortes)
            continuar = input(" Vai continuar cortando, sim ou não? ")

            if continuar == "não":
                tamanhos = ", ".join(map(str, cortes))
                print(f"\n Todos os tamanhos cortados são esses: {tamanhos}")
                break # este break finaliza o loop quando digita 0
            
def sair_sistema():
        
        print("\n Saindo do sistema...\n")

def menu_principal():

       while True:
                print("\n\n\n --Sistema de gerenciamento para serralheria--\n")
                
                print(" Menu de opções \n")

                print("\n 1. Checklist de ferramentas:")
                print("\n 2. Calcular material e serviço:")
                print("\n 3. Organizar cortes:")
                print("\n 4. Sair:\n")

                print("-----------------------------------------------")
                opcao = input(" Digite o número de uma opção do menu: ")

                if opcao == "1":
                       checklist_ferramentas()

                elif opcao == "2":
                        calcular_material_servico()

                elif opcao == "3":
                        organizar_cortes()

                elif opcao == "4":
                       sair_sistema()
                       break

                else :
                        print("\n Opção errada, tente novamente! ")    

def entrar_conta():

       

              cpf = input("\n Informe seu usuário: ")
              senha = input(" Digite a senha: ")
              login_sucesso = False
              for x in banco_usuarios:
                         if cpf == x["cpf"] and senha == x["senha"]:
                                print("\n comfirmado")
                                usuarios_logados = x
                                login_sucesso = True
                                menu_principal() 
                                break
                                
                         
              if login_sucesso == False:
                      print("\n Usuário ou senha incorreto! ")
          
def entrar_cadastrar():

       while True:

              print("\n -- Bem vindo ao Sistema para serralheria -- ")

              print("\n 1. Entrar com sua conta: ")
              print(" 2. Cadastrar: ")

              opcao = input("\n Digite um número das opções acima: ")

              if opcao == "1":
                        entrar_conta()

              elif opcao == "2":
                        cadastro_usuarios()

                
                        
entrar_cadastrar()

                     
