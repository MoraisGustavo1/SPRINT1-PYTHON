import os

# Listas para armazenar os nomes de usuários e senhas
usuarios = []
senhas = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    usuarios.append(usuario)
    senhas.append(senha)

    print("Usuário cadastrado com sucesso!")

# Função para realizar login
def login():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verifica se o usuário existe
    if usuario in usuarios:
        indice = usuarios.index(usuario)
        # Verifica se a senha está correta
        if senhas[indice] == senha:
            print("Login realizado com sucesso!")   
            while True:
                # Limpa a tela
                os.system('cls' if os.name == 'nt' else 'clear')
                # Menu após login bem-sucedido
                print("1. Curiosidade sobre carros")
                print("2. Últimas corridas")
                print("3. Próximas corridas")
                print("4. Times")
                print("5. Sair")
                
                escolha = input("Escolha uma opção: ")
                # Chamadas para as respectivas funções com base na escolha
                if escolha == "1":
                    curiosidades_sobre_carros()
                elif escolha == "2":
                    ultimas_corridas()
                elif escolha == "3":
                    proximas_corridas()
                elif escolha == "4":
                    times()
                elif escolha == "5":
                    print("Saindo...")
                    break   
                else:
                    print("Opção inválida!")
                    input("Pressione Enter para continuar...")
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")

# Função que mostra curiosidades sobre carros de Fórmula E e Fórmula 1
def curiosidades_sobre_carros():
    print("Curiosidades sobre carros de Fórmula E e Fórmula 1:")
    print("1. Velocidade Máxima:")
    print("   - Fórmula 1: Pode ultrapassar 370 km/h.")
    print("   - Fórmula E: Velocidade máxima em torno de 280 km/h.")
    print()
    print("2. Aceleração:")
    print("   - Fórmula 1: Acelera de 0 a 100 km/h em aproximadamente 2.6 segundos.")
    print("   - Fórmula E: Acelera de 0 a 100 km/h em cerca de 2.8 segundos.")
    print()
    print("3. Peso do Carro:")
    print("   - Fórmula 1: Aproximadamente 752 kg sem o piloto e combustível.")
    print("   - Fórmula E: Aproximadamente 900 kg incluindo a bateria.")
    print()
    print("4. Tecnologia de Motor:")
    print("   - Fórmula 1: Utiliza motores híbridos (combustão interna e energia elétrica).")
    print("   - Fórmula E: Totalmente elétrico com baterias de alta capacidade.")
    print()
    print("5. Impacto Ambiental:")
    print("   - Fórmula 1: Maior impacto ambiental devido ao uso de combustíveis fósseis.")
    print("   - Fórmula E: Menor impacto ambiental com zero emissões diretas de CO2 durante a corrida.")
    print()
    input("Pressione Enter para voltar ao menu...")

# Função que mostra as últimas corridas de Fórmula E
def ultimas_corridas():
    print("Últimas corridas de Fórmula E:")
    print("   - 2024 HANKOOK MEXICO CITY E-PRIX.")
    print("   - 2024 DIRIYAH E-PRIX.")
    print("   - 2024 SÃO PAULO E-PRIX.")
    print("   - 2024 TOKYO E-PRIX.")
    print("   - 2024 MISANO E-PRIX.")
    print("   - 2024 MONACO E-PRIX.")
    print("   - 2024 SUN MINIMEAL BERLIN E-PRIX.")
    print("   - 2024 SHANGHAI E-PRIX.")
    print()
    input("Pressione Enter para voltar ao menu...")

# Função que mostra as próximas corridas de Fórmula E
def proximas_corridas():
    print("Próximas corridas de Fórmula E:")
    print("   - 2024 PORTLAND E-PRIX: 29 e 30 de junho.")
    print("   - 2024 LONDRES E-PRIX: 20 e 21 de julho.")
    print()
    input("Pressione Enter para voltar ao menu...")

# Função que mostra os times de Fórmula E e suas vitórias
def times():
    print("Times de Fórmula E:")
    print("   - Nissan - 18 vitórias")
    print("   - Envision Racing - 16 vitórias")
    print("   - Jaguar TCS Racing - 16 vitórias")
    print("   - ABT Cupra - 14 vitórias")
    print("   - Andretti - 11 vitórias")
    print("   - Maserati MSG - 10 vitórias")
    print("   - Tag Heuer Porsche - 9 vitórias")
    print("   - Neom MCLaren - 8 vitórias")
    print("   - Mahindra Racing - 5 vitórias")
    print("   - DS Penske - 3 vitórias")
    print("   - ERT - 2 vitórias")
    print()
    input("Pressione Enter para voltar ao menu...")

# Função principal que mostra o menu inicial e permite cadastro e login de usuários
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            login()
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

# Execução do programa principal
if __name__ == '__main__':
    main()
