# 🐍 Este código está escrito em Python, uma linguagem de programação de alto nível,
# conhecida por sua simplicidade e legibilidade. Python é amplamente utilizado
# para desenvolvimento web, automação, análise de dados, inteligência artificial,
# entre outras áreas.

# 💻 Este código foi escrito numa IDE chamada Visual Studio Code.
# IDE (Integrated Development Environment) é um ambiente de desenvolvimento integrado
# que fornece ferramentas abrangentes para escrever, testar e depurar código.
# Visual Studio Code é uma IDE popular que suporta várias linguagens de programação
# e oferece recursos como destaque de sintaxe, autocompletar, e integração com sistemas de controle de versão.

# 👤 Este código foi escrito e codificado por João Teixeira
# github.com/joaocvteixeira
# linkedin.com/in/joaocvteixeira

# 🎯 Objetivo do código:
# O objetivo deste código é solicitar ao usuário que insira dois números e uma operação matemática,
# realizar a operação entre os números fornecidos e exibir o resultado no console.
# Este exemplo é útil para entender conceitos básicos de entrada, processamento e saída em Python.

# 🤔 Uma string é uma sequência de caracteres, como palavras ou frases. 
# No Python, strings são delimitadas por aspas simples ('') ou duplas ("").

# 🔡 Variável: Uma variável é um espaço na memória que armazena um valor.
# No Python, você pode criar uma variável simplesmente atribuindo um valor a um nome.
# Exemplo: x = 10
# Aqui, 'x' é uma variável que armazena o valor 10.

# ⌨️ Solicitação das entradas de dados do usuário
# A função input() é usada para capturar a entrada do usuário.
# O texto dentro dos parênteses é exibido como um prompt para o usuário.
# float(): Converte uma string ou número em um número de ponto flutuante (decimal).
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

# 🔡 Variável: Uma variável é um espaço na memória que armazena um valor.
# No código acima, 'numero1', 'numero2' e 'operacao' são variáveis que armazenam
# as entradas fornecidas pelo usuário.

# ➗ Realiza a operação matemática entre os números fornecidos
# if: Verifica uma condição. Se a condição for verdadeira, o bloco de código associado ao if será executado.
if operacao == '+':
    resultado = numero1 + numero2
# elif: Abreviação de "else if". Verifica outra condição se a condição anterior (if ou elif) for falsa.
elif operacao == '-':
    # abs(): A função abs() retorna o valor absoluto de um número, que é o número sem seu sinal.
    resultado = abs(numero1 - numero2)
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
# else: Executa um bloco de código se todas as condições anteriores (if e elif) forem falsas.
else:
    resultado = "Erro: Operação inválida."

# Diferença entre = e ==:
# 👍 = : É o operador de atribuição. Ele é usado para atribuir um valor a uma variável.
# Exemplo: numero1 = 5
# 🤝 == : É o operador de igualdade. Ele é usado para comparar dois valores e retorna True se eles forem iguais.
# Exemplo: if numero1 == 5:

# 🖨️ Exibe o resultado da operação
# A função print() é usada para exibir a saída no console.
# Console é a interface onde os resultados do código são exibidos.
print("Resultado:", resultado)

# ▶️ Como rodar este código:
# 1. Requer instalar Python:
#    - Acesse o site oficial do Python: https://www.python.org/
#    - Baixe e instale a versão mais recente do Python.
#    - Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.
# 2. Abra o Visual Studio Code.
# 3. Abra o terminal integrado pressionando `Ctrl + `` (Ctrl + acento grave) ou indo em `Terminal` > `Novo Terminal`
#    geralmente encontrado na parte superior da tela. Certifique-se que o terminal está definido para Python
#    (e não PowerShell por exemplo...)
# 4. Navegue até o diretório onde o arquivo `ope_mat.py` está localizado usando o comando `cd`.
#    Exemplo: cd C:/Users/usuário/OneDrive/Desktop
# 5. Execute o código Python usando o comando `python` seguido do nome do arquivo.
#    Exemplo: python ope_mat.py
# 6. Interaja com o programa inserindo dois números e uma operação matemática quando solicitado.
# 7. Veja o resultado exibido no console.