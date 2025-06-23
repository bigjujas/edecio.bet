import random
import time
from colorama import just_fix_windows_console
from colorama import init
from colorama import Fore, Back, Style
just_fix_windows_console()
init(autoreset=True)

def menu():
    print(Fore.CYAN + "=== Edecio.Bet ===")
    print(Fore.CYAN + "1 - Depositar 💳")
    print(Fore.CYAN + "2 - Apostar na Roleta 🔴⚫")
    print(Fore.CYAN + "3 - Checar Saldo 🪙")
    print(Fore.CYAN + "4 - Ver Ranking 🏆")
    print(Fore.CYAN + "5 - Fechar App ❌")

def depositar(balance):
    try:
        deposito = float(input(Fore.BLUE + "Digite o valor desejado para depósito: "))
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

def apostar_roleta(balance):
    try:
        valor_aposta = float(input(Fore.BLUE + "Digite o valor que deseja apostar: "))
        if valor_aposta <= 0:
            print(Fore.RED + "Erro! O valor da aposta deve ser positivo.")
            return balance
        if valor_aposta > balance:
            print(Fore.RED + "Erro! Valor da aposta maior que o saldo disponível.")
            return balance
    except ValueError:
        print(Fore.RED + "Erro! Digite um número válido para a aposta.")
        return balance

    print(Fore.CYAN + "\n--- Roleta de Cores ---")
    print(Fore.CYAN + "Aposte em Preto (P) ou Vermelho (V).")
    cor_escolhida_input = input(Fore.YELLOW + "Sua aposta (P/V): ").upper()

    if cor_escolhida_input not in ['P', 'V']:
        print(Fore.RED + "Erro! Escolha inválida. Por favor, digite 'P' para Preto ou 'V' para Vermelho.")
        return balance

    cores_roleta_emojis = {'Vermelho': '🔴', 'Preto': '⚫'}
    cores_roleta_texto = list(cores_roleta_emojis.keys())
    cor_sorteada_texto = random.choice(cores_roleta_texto)
    cor_sorteada_emoji = cores_roleta_emojis[cor_sorteada_texto]

    print(Fore.MAGENTA + f"\nGirando a roleta...")

    num_simbolos_inicial = 9
    for i in range(num_simbolos_inicial, 1, -1):
        linha_roleta = []
        for _ in range(i):
            linha_roleta.append(random.choice(list(cores_roleta_emojis.values())))
        print(" ".join(linha_roleta))
        time.sleep(0.15)
    
    print(cor_sorteada_emoji)
    time.sleep(0.2)

    print(Fore.BLUE + f"A roleta parou em: {cor_sorteada_texto} {cor_sorteada_emoji}")

    if (cor_escolhida_input == 'V' and cor_sorteada_texto == 'Vermelho') or \
       (cor_escolhida_input == 'P' and cor_sorteada_texto == 'Preto'):
        ganho = valor_aposta * 2
        balance += ganho
        print(Fore.GREEN + f"Parabéns! Você ganhou ${ganho:.2f}!")
    else:
        balance -= valor_aposta
        print(Fore.RED + f"Que pena! Você perdeu ${valor_aposta:.2f}.")

    return balance

def salvar_ranking(nome_jogador, saldo_final):
    try:
        with open("ranking.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Jogador: {nome_jogador}, Saldo Final: ${saldo_final:.2f}\n")
        print(Fore.GREEN + "Seu resultado foi salvo no ranking!")
    except IOError:
        print(Fore.RED + "Erro ao salvar o ranking. Verifique as permissões do arquivo.")

def ler_ranking():
    jogadores_ranking = []
    try:
        with open("ranking.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    partes = linha.split(", Saldo Final: $")
                    if len(partes) == 2:
                        nome_raw = partes[0].replace("Jogador: ", "")
                        try:
                            saldo = float(partes[1])
                            jogadores_ranking.append((saldo, nome_raw))
                        except ValueError:
                            pass
        
        jogadores_ranking.sort(key=lambda x: x[0], reverse=True)

        print(Fore.CYAN + "\n--- Ranking de Jogadores ---")
        if not jogadores_ranking:
            print(Fore.YELLOW + "O ranking está vazio. Jogue para adicionar resultados!")
        else:
            for i, (saldo, nome) in enumerate(jogadores_ranking):
                print(f"{i+1}º - Jogador: {nome}, Saldo Final: ${saldo:.2f}")
        print(Fore.CYAN + "---------------------------")

    except FileNotFoundError:
        print(Fore.YELLOW + "O ranking ainda não foi criado. Jogue para salvar seu resultado!")
    except IOError:
        print(Fore.RED + "Erro ao ler o ranking. Verifique as permissões do arquivo.")

def main():
    balance = 0.0
    
    nome_jogador = input(Fore.LIGHTBLUE_EX + "Bem-vindo(a) ao Edecio.Bet! Por favor, digite seu nome: ")
    if not nome_jogador.strip():
        nome_jogador = "Jogador Anônimo"
        print(Fore.YELLOW + "Nome inválido. Você será identificado como 'Jogador Anônimo'.")
    
    print(Fore.CYAN + f"\nOlá, {nome_jogador}!")

    while True:
        menu()
        escolha = input(Fore.YELLOW + "Qual opção deseja (1-5): ")
        
        if escolha == "1":
            balance = depositar(balance)
        elif escolha == "2":
            if balance == 0:
                print(Fore.RED + "Erro! Você não tem saldo disponível, deposite por favor")
            else:
                balance = apostar_roleta(balance)
        elif escolha == "3":
            print(Fore.GREEN + f"Saldo atual: ${balance:.2f}")
        elif escolha == "4":
            ler_ranking()
        elif escolha == "5":
            salvar_ranking(nome_jogador, balance)
            print(Fore.BLUE + f"Programa finalizado! Saldo final de {nome_jogador}: ${balance:.2f}")
            break
        else:
            print(Fore.RED + "Escolha Inválida!")
            
main()