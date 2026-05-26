# Jogo da Forca (Console)🎮

Um jogo da forca interativo desenvolvido em Python, executado diretamente no terminal. O projeto foi construído focando em modularização, tratamento de dados de entrada e otimização de estruturas de dados.

## 🚀 Funcionalidades
- **Sorteio Dinâmico:** Palavras escolhidas aleatoriamente de um banco de dados integrado.
- **Validação de Entradas:** Sistema que impede caracteres inválidos ou palpites repetidos de consumirem tentativas.
- **Histórico de Palpites:** Exibição em tempo real das letras já testadas pelo jogador.

## 🧠 Justificativa Técnica
Para o gerenciamento das letras já tentadas pelo usuário, optou-se pela utilização da estrutura de dados Set (Conjunto) em vez de uma lista tradicional.
- **Eficiência de Busca ($O(1)$):** A verificação se uma letra já foi digitada ocorre de forma instantânea via tabelas hash, enquanto em uma lista exigiria uma busca linear ($O(n)$).
- **Garantia de Unicidade:** O método .add() impede nativamente a inserção de elementos duplicados.

## 🛠️ Como Executar o Projeto
Certifique-se de ter o Python 3.x instalado em sua máquina.

1. Clone o repositório:
```bash
git clone https://github.com/DanielaBarbosadosSantos/Jogo_da_Forca_Simplificado.git
````
2. Acesse a pasta do projeto:
```
cd Jogo_da_Forca_Simplificado
```
3. Execute o jogo:
```
python jogo_forca.py
```

## 📝 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
