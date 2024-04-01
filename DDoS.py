import os

def mc(editar):
    try:
        caminho_mcbot = "/storage/emulated/0/McBot/McBot.py"

        with open(caminho_mcbot, 'r') as arquivo:
            linhas = arquivo.readlines()

        for idx, linha in enumerate(linhas):
            if 'c =' in linha:
                linhas[idx] = f"c = {editar}\n"
                break

        with open(caminho_mcbot, 'w') as arquivo:
            arquivo.writelines(linhas)
        os.system("clear")
    except Exception as e:
        print(f"Erro ao editar o arquivo 'McBot.py': {e}")

def inicio():
    while True:
        os.system("pyfiglet -c green -f big B-14")
        print("\033[1;32mB-14 : Opções\n\n")
        print("1. Mc-Bot")
        print("")
        print("2. Quantidade De BOTS")
        print("")
        print("3. DDoS")
        print("")
        print("4. Resolver Erros")
        print("")
        print("5. Criar Nick")
        print("")
        print("")
        
        opcao = input("\033[1;34mESCOLHA:\033[1;0m ")

        if opcao == "1":
            os.system("python McBot/McBot.py")
        elif opcao == "2":
            os.system("clear")
            quantidade_bots = input("\033[1;32mQuantidade: \033[1;0m")
            mc(quantidade_bots)
        elif opcao == "3":
            os.system("python3 /storage/emulated/0/McBot/DDoS.py")
        elif opcao == "4":
            os.system("/storage/emulated/0/b-14/script4.py")
        elif opcao == "5":
            os.system("/storage/emulated/0/b-14/script5.py")
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

class Colors:
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Orange = "\033[33m"
    Blue = "\033[34m"
    Purple = "\033[35m"
    Cyan = "\033[36m"
    LightGrey = "\033[37m"
    DarkGrey = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    Yellow = "\033[93m"
    LightBlue = "\033[94m"
    Pink = "\033[95m"
    LightCyan = "\033[96m"
    Reset = "\033[0m"

if __name__ == "__main__":
    inicio()
