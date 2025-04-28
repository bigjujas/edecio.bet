import random
from colorama import just_fix_windows_console
from colorama import init
from colorama import Fore, Back, Style
just_fix_windows_console()
init(autoreset=True)

def menu():
    print(Fore.CYAN + "=== Edecio.Bet ===")
    print(Fore.CYAN + "1 - Depositar 💳")
    print(Fore.CYAN + "2 - Apostar 📈")
    print(Fore.CYAN + "3 - Checar Saldo 🪙")
    print(Fore.CYAN + "4 - Fechar App ❌")

def depositar(balance):
    try:
        deposito = float(input(Fore.YELLOW + "Digite o valor desejado para depósito: "))
        if deposito <= 0:
            print(Fore.RED + "Erro! Valor negativo")
            return balance
        else:
            balance += deposito
            print(Fore.GREEN + f"Valor depositado: ${deposito:.2f} | Novo saldo: ${balance:.2f}")
            return balance
    except ValueError:
        print(Fore.RED + "Digite um número válido por favor!")
        return balance

def apostar(balance):
    try:
        valor = float(input(Fore.YELLOW + "Digite o valor que deseja apostar: "))
        if valor <= 0:
            print(Fore.RED + "Erro! Valor negativo")
            return balance
        if valor > balance:
            print(Fore.RED + "Erro! Valor da aposta maior que o saldo")
            return balance
    except ValueError:
        print(Fore.RED + "Erro! Número inválido")
        return balance
    
    print(Fore.CYAN + "Jogo - Adivinhe o Número!")
    print(Fore.CYAN + "Escolha um número e acerte o numero sorteado entre 1 e o número escolhido")
    print(Fore.CYAN + "Quanto maior o número escolhido, maior o multiplicador da aposta")
    try:
        numero = int(input(Fore.YELLOW + "Digite o número desejado: "))
        if numero <= 1:
            print(Fore.RED + "Erro! O número precisa ser maior que 1")
            return balance
        sorteado = random.randint(1, numero)
        print(Fore.CYAN + f"O número foi sorteado! Agora escolha um número entre 1-{numero}")
        resposta = int(input(Fore.YELLOW + "Digite o número sorteado: "))
        if resposta == sorteado:
            # Multiplicador simples para demonstrar (ex.: multiplicador = numero * 0.1)
            multiplicador = numero * 0.5
            ganho = valor * multiplicador
            balance += ganho
            print(Fore.GREEN + f"Parabéns, você acertou! Ganhou: ${ganho:.2f}")
            return balance
        else:
            print(Fore.RED + f"Perdeu! O número era {sorteado}. Perdeu: ${valor:.2f}")
            balance -= valor
            return balance
    except ValueError:
        print(Fore.RED + "Erro! Número inválido")
        return balance

def main():
    balance = 0.0
    while True:
        menu()
        escolha = input(Fore.YELLOW + "Qual opção deseja (1-4): ")
        
        if escolha == "1":
            balance = depositar(balance)
        elif escolha == "2":
            if balance == 0:
                print(Fore.RED + "Erro! Você não tem saldo disponível, deposite por favor")
            else:
                balance = apostar(balance)
        elif escolha == "3":
            print(Fore.GREEN + f"Saldo atual: ${balance:.2f}")
        elif escolha == "4":
            print(Fore.BLUE + f"Programa finalizado! Saldo final: ${balance:.2f}")
            break
        else:
            print(Fore.RED + "Escolha Inválida!")
            
main()