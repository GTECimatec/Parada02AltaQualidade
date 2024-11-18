from Calculadora import adicao, subtracao, multiplicacao, divisao, potencia, raiz_quadrada, fatorial, logaritmo_natural, logaritmo_base10

def testar_operacao(nome, funcao, *args, esperado):
    """Executa um teste para uma operação específica e imprime o resultado."""
    try:
        resultado = funcao(*args)
        status = "✅ Passou" if resultado == esperado else "❌ Falhou"
        print(f"[{status}] {nome}: {funcao.__name__}{args} => {resultado} (Esperado: {esperado})")
    except Exception as e:
        print(f"[❌ Falhou] {nome}: {funcao.__name__}{args} => Erro: {str(e)} (Esperado: {esperado})")

def test_operacoes():
    print("\n=== Início dos Testes ===\n")

    # Testes de Adição
    print("🔹 Testando Adição")
    testar_operacao("Adição", adicao, 1, 2, esperado=3)
    testar_operacao("Adição com negativos", adicao, -1, -1, esperado=-2)
    testar_operacao("Adição com zeros", adicao, 0, 0, esperado=0)

    # Testes de Subtração
    print("\n🔹 Testando Subtração")
    testar_operacao("Subtração", subtracao, 5, 3, esperado=2)
    testar_operacao("Subtração com negativos", subtracao, -1, -1, esperado=0)
    testar_operacao("Subtração com zero", subtracao, 0, 5, esperado=-5)

    # Testes de Multiplicação
    print("\n🔹 Testando Multiplicação")
    testar_operacao("Multiplicação", multiplicacao, 3, 2, esperado=6)
    testar_operacao("Multiplicação com zero", multiplicacao, 0, 5, esperado=0)
    testar_operacao("Multiplicação com negativos", multiplicacao, -3, -3, esperado=9)

    # Testes de Divisão
    print("\n🔹 Testando Divisão")
    testar_operacao("Divisão", divisao, 10, 2, esperado=5.0)
    testar_operacao("Divisão não exata", divisao, 5, 2, esperado=2.5)
    testar_operacao("Divisão por zero", divisao, 5, 0, esperado="Valor indeterminado")  # Levanta exceção

    # Testes de Potenciação
    print("\n🔹 Testando Potenciação")
    testar_operacao("Potenciação", potencia, 2, 3, esperado=8)
    testar_operacao("Potência com zero", potencia, 5, 0, esperado=1)
    testar_operacao("Potência unitária", potencia, 1, 100, esperado=1)

    # Testes de Raiz Quadrada
    print("\n🔹 Testando Raiz Quadrada")
    testar_operacao("Raiz Quadrada", raiz_quadrada, 16, esperado=4.0)
    testar_operacao("Raiz Quadrada de zero", raiz_quadrada, 0, esperado=0.0)
    testar_operacao("Raiz Quadrada de negativo", raiz_quadrada, -1, esperado="Erro: Raiz quadrada de número negativo")

    # Testes de Fatorial
    print("\n🔹 Testando Fatorial")
    testar_operacao("Fatorial", fatorial, 3, esperado=6)
    testar_operacao("Fatorial de zero", fatorial, 0, esperado=1)
    testar_operacao("Fatorial de um", fatorial, 1, esperado=1)

    # Testes de Logaritmo Natural
    print("\n🔹 Testando Logaritmo Natural")
    testar_operacao("Logaritmo Natural", logaritmo_natural, 1, esperado=0.0)
    testar_operacao("Logaritmo de e", logaritmo_natural, 2.718281828459045, esperado=1.0)
    testar_operacao("Logaritmo negativo", logaritmo_natural, -1, esperado="Erro: Logaritmo de número não positivo")

    # Testes de Logaritmo Base 10
    print("\n🔹 Testando Logaritmo Base 10")
    testar_operacao("Logaritmo Base 10", logaritmo_base10, 1, esperado=0.0)
    testar_operacao("Logaritmo de 10", logaritmo_base10, 10, esperado=1.0)
    testar_operacao("Logaritmo negativo", logaritmo_base10, -1, esperado="Erro: Logaritmo de número não positivo")

    print("\n=== Fim dos Testes ===")

# Executar os testes manualmente
if __name__ == "__main__":
    test_operacoes()
