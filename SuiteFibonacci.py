def fibonacci(n):
    if n <= 0:
        return "Le nombre doit être supérieur à 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

n = int(input("Quel terme de la suite de Fibonacci veux-tu ? "))
resultat = fibonacci(n)

print(f"Le {n}ᵉ terme de la suite de Fibonacci est : {resultat}")
