def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("informe um número: "))

if fibonacci(numero):
    print(f"o número {numero} pertence à sequência de fibonacci :)")
else:
    print(f"o número {numero} não pertence à sequência de fibonacci :(")
