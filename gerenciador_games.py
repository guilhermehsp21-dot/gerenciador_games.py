def exibir_lista(colecao_jogos):
    print("--- 🎮 Sua lista de Jogos --- ")
    if not colecao_jogos:
        print("Sua lista está vazia!")
    else:
        for jogo in colecao_jogos:
            print(f"-{jogo["nome"]} -- Status: {jogo["status"]}")


colecao_jogos = []


#------------------opção inicial-------------------------------
while True:
    print("Gostaria de adicionar um jogo ou ver sua lista de jogos?")
    print("1- Ver sua lista de jogos")
    print("2- Adicionar um novo jogo")
    print("0- Sair")


    
    opcao_inicial = input("Escolha uma opção: ")

    if opcao_inicial == "1":
        exibir_lista(colecao_jogos)
        
    elif opcao_inicial == "2":
        nome_jogo = input("Insira o nome do jogo: ")
    
        while True:
                print("\nStatus atual: ")
                print("1 - Quero jogar")
                print("2 - Jogando")
                print("3 - Zerado")
                print("4 - Dropei")
                status = input("Escolha uma opção: ")

                if status == "1":
                    quero_jogar = {
                            "nome": nome_jogo,
                            "status": "Quero jogar"
                        }
                    colecao_jogos.append(quero_jogar)
                    print(f"Anotado! {nome_jogo} já está na sua lista.")
                    
                    print("1- Ver lista")
                    print("2- Voltar")
                                                
                    opcoes_1 = input("")
                    if opcoes_1 == "1":
                            exibir_lista(colecao_jogos)
                            break
                    elif opcoes_1 == "2":
                            break
                    else:
                            print("Opção inválida")
                
                elif status == "2":
                    estou_jogando = {
                            "nome": nome_jogo,
                            "status": "Estou jogando"
                        }
                    colecao_jogos.append(estou_jogando)
                    print(f"{nome_jogo} está em progresso!!")
                    print("Ver sua lista?")
                    print("Sim-1")
                    print("Voltar-0")
                    
                    opcoes_2 = input("")
                    if opcoes_2 == "1":
                        exibir_lista(colecao_jogos)
                        
                    elif opcoes_2 == "0":
                        break
                    else:
                        print("Opção inválida")
                        

                elif status == "3":
                    
                    print("Boa, mais um game zerado!!")
                    nota_jogo = input("Qual nota de 0 a 10 você dá para esse game?: ")
                    horas_zerar = input("Quantas horas levou para zerar esse game?: ")
                    comentario = input("Escreva o que achou do game: ")

                    jogos_zerados = {
                    "nome": nome_jogo,
                    "status": "zerado",
                    "nota": nota_jogo,
                    "horas de jogo": horas_zerar,
                    "comentario": comentario
                    }
                    colecao_jogos.append(jogos_zerados)
                    break

                elif status == "4":
                    print("Eita, esse foi pra gaveta!")
                    motivo_drop = input("Por qual motivo você dropou o game?: ")

                    jogos_dropados = {
                         "nome": nome_jogo,
                         "status": "dropado",
                         "motivo": motivo_drop
                    }
                    colecao_jogos.append(jogos_dropados)
                    break

                else:
                    print("Digite uma opção válida")
                #-------------------------------------------------
    elif opcao_inicial == "0":
            break
    else:
         print("Escolha uma opção válida!")