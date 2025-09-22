    Código:

# Se o usuário entrou com λ e μ, podemos calcular as demais métricas
    if lam is not None and mu is not None:
        rho = a / c
        Wq = p / (c * mu - lam)
        Lq = lam * Wq
        W  = Wq + 1 / mu
        L  = lam * W

        print(f"ρ  = {rho:.4f}")
        print(f"Wq = {Wq:.4f} unidades de tempo")
        print(f"Lq = {Lq:.4f} clientes")
        print(f"W  = {W:.4f} unidades de tempo")
        print(f"L  = {L:.4f} clientes")
    else:
        print("Obs: Para calcular Wq, Lq, W e L é necessário fornecer λ e μ.")


EXPLICAÇÃO:
Não utilizei por funções, mas sim por uma condição para implementar as métricas pedidas.