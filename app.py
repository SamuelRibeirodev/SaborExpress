import os

restaurantes = ["Pizza", "Macarrão"]

def exibirNomeDoPrograma():
    print("Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n")

def exibirOpcoes():
    print("=== Opções do APP ===")

    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair")


def finalizarApp():
    exibirSubtitulo("Finalizar APP")

def voltarAoMenu():
    input("\nDigite uma tecla para voltar ao menu: ")
    main()

def opcaoInvalida():
    print("Opção Inválida!\n")
    voltarAoMenu()

def exibirSubtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def cadastrarNovoRestaurante():
    os.system("cls")
    exibirSubtitulo("Cadastro de Novos Restaurantes")
    nomeDoRestaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nomeDoRestaurante)
    print(f"O restaurante {nomeDoRestaurante} foi cadastrado com sucesso!")
    voltarAoMenu()

def listarRestaurante():
    exibirSubtitulo("Listando os restaurantes")

    for restaurante in restaurantes:
        print(f".{restaurante}")

    voltarAoMenu()
    

def escolherOpcao():
    try:
        opcaoEscolhida = int(input("Escolha uma das opções: "))

        if opcaoEscolhida == 1:
            cadastrarNovoRestaurante()
        elif opcaoEscolhida == 2:
            listarRestaurante()
        elif opcaoEscolhida == 3:
            print("Ativar Restaurante")
        elif opcaoEscolhida == 4:
            finalizarApp()
        else:
            opcaoInvalida()
    except:
        opcaoInvalida()

def main():
    os.system("cls")
    exibirNomeDoPrograma()
    exibirOpcoes()
    escolherOpcao()

if __name__ == "__main__":
    main()