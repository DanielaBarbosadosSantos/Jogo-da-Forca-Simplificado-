# ----------------------------------------------------------------              
# Script: jogo_forca.py
# Objetivo: Jogo da Forca interativo via console com controle de estado.
# ----------------------------------------------------------------
00

import random

def inicializar_jogo():
    """
    Sorteia a palavra secreta e prepara a estrutura de lacunas para o jogo.

    Returns:
        tuple: Uma tupla contendo a palavra_secreta (str) em caixa alta
               e a lista de letras_descobertas (list) preenchida com underscores.
    """
    banco_palavras = ["PYTHON", "DESENVOLVEDOR", "LOGICA", "ALGORITMO", "VARIAVEL"]
    palavra = random.choice(banco_palavras)
    lacunas = ["_"] * len(palavra)
    return palavra, lacunas


def processar_tentativa(letra, palavra_secreta, letras_descobertas):
    """
    Varre a palavra secreta e atualiza as lacunas caso a letra esteja correta.

    Args:
        letra (str): O palpite atual do jogador (caractere único em maiúsculo).
        palavra_secreta (str): A palavra a ser adivinhada.
        letras_descobertas (list): A lista atual de lacunas e acertos.

    Returns:
        bool: True se o jogador acertou a letra, False caso contrário.
    """
    acertou = False
    for indice, caractere in enumerate(palavra_secreta):
        if caractere == letra:
            letras_descobertas[indice] = letra
            acertou = True
    return acertou


def executar_jogo():
    print("========================================")
    print("      BEM-VINDO AO JOGO DA FORCA        ")
    print("========================================")

    # Inicializa os estados do jogo a partir da função modularizada
    palavra_secreta, letras_descobertas = inicializar_jogo()
    
    erros_restantes = 6

    # JUSTIFICATIVA TÉCNICA PARA A ESCOLHA DO SET (CONJUNTO):
    # Optou-se por usar um 'set' em vez de 'list' para o histórico de palpites por dois motivos:
    # 1. Eliminação nativa de duplicatas: o método .add() rejeita repetições sem precisar de condicionais complexas.
    # 2. Eficiência de Busca (O(1)): a checagem 'if palpite in letras_tentadas' é instantânea, via tabelas hash, 
    #    enquanto na lista exigiria uma busca linear item por item (O(n)), economizando processamento.
    letras_tentadas = set()

    # Motor principal do jogo: roda enquanto houver chances e a palavra não for descoberta
    while erros_restantes > 0 and "_" in letras_descobertas:
        print(f"\nPalavra atual: {' '.join(letras_descobertas)}")
        print(f"Letras já tentadas: {', '.join(sorted(letras_tentadas)) if letras_tentadas else '{}'}")
        print(f"Chances restantes: {erros_restantes}")
        
        # Captura o palpite e padroniza para maiúsculo
        palpite = input("Digite uma letra: ").strip().upper()

        # Validação básica de entrada de dados
        if len(palpite) != 1 or not palpite.isalpha():
            print("[AVISO] Por favor, digite apenas uma letra válida!")
            continue

        # Validação de palpite repetido utilizando a alta performance do set
        if palpite in letras_tentadas:
            print(f"[AVISO] Você já tentou a letra '{palpite}'. Escolha outra!")
            continue

        # Adiciona o novo palpite ao conjunto de histórico
        letras_tentadas.add(palpite)

        # Processa a tentativa através da função especialista
        if processar_tentativa(palpite, palavra_secreta, letras_descobertas):
            print(f"Muito bem! A letra '{palpite}' faz parte da palavra.")
        else:
            erros_restantes -= 1
            print(f"Que pena! A letra '{palpite}' não está na palavra.")

    # Telas finais de encerramento avaliadas fora do laço
    print("\n========================================")
    if "_" not in letras_descobertas:
        print(f"PARABÉNS! Você descobriu a palavra '{palavra_secreta}' e venceu! 🏆")
    else:
        print(f"GAME OVER! Suas chances acabaram. A palavra era: '{palavra_secreta}'.")
    print("========================================")


if __name__ == "__main__":
    executar_jogo()