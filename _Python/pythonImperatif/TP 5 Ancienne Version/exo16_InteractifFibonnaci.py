def interactif_fibonacci(rang_N):
    if rang_N == 0 or rang_N ==1:
        return rang_N
    else:
        return interactif_fibonacci(rang_N - 1) + interactif_fibonacci(rang_N - 2)

rang_N = int(input("Entrez un rang N: "))
print("Le nombre de rang", rang_N, "suite Fibonacci:", interactif_fibonacci(rang_N))
