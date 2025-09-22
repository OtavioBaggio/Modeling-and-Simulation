# -*- coding: utf-8 -*-
"""
Calculadora de Métricas do Modelo M/M/c

    Nome: José Otávio R. Baggio

Símbolos e fórmulas (M/M/c):
- λ (lambda): taxa de chegadas (clientes/unidade de tempo)
- μ (mi): taxa de atendimento de cada servidor (clientes/unidade de tempo)
- c: número de servidores idênticos

Derivadas:
- a = λ/μ                (Erlangs) → tráfego oferecido
- ρ = a/c = λ/(c μ)      → utilização média por servidor (0 < ρ < 1 p/ estabilidade)

Fórmula de Erlang C (probabilidade de esperar na fila):
            (a^c / c!) * (c / (c − a))
P(wait) = ---------------------------------------------
          Σ_{n=0}^{c−1} (a^n / n!)  +  (a^c / c!) * (c / (c − a))

Métricas adicionais:
- Wq = P(wait) / (c μ − λ)       (tempo médio de espera na fila)
- Lq = λ * Wq                    (nº médio de clientes na fila)
- W  = Wq + 1/μ                  (tempo médio no sistema)
- L  = λ * W                     (nº médio de clientes no sistema)
"""

from math import factorial

def erlang_c(a: float, c: int) -> float:
    """Retorna P(wait) dado o tráfego oferecido a=λ/μ (Erlangs) e c servidores.
    Observação: para estabilidade prática, é necessário a < c.
    """
    if a < 0 or c <= 0:
        raise ValueError("'a' deve ser >= 0 e 'c' > 0.")
    if a >= c:
        return 1.0  # sistema instável: P(wait) tende a 1
    
    soma = sum((a**n) / factorial(n) for n in range(c))
    termo = (a**c) / factorial(c) * (c / (c - a))
    return termo / (soma + termo)

def ler_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).replace(',', '.'))
        except ValueError:
            print('Valor inválido. Tente novamente.')

def ler_int(msg: str) -> int:
    while True:
        try:
            v = int(input(msg))
            if v <= 0:
                print('Digite um inteiro > 0.')
            else:
                return v
        except ValueError:
            print('Valor inválido. Tente novamente.')

def main():
    print('\n=== Calculadora M/M/c ===')
    print('1) Entrar com a (λ/μ) e c')
    print('2) Entrar com λ, μ e c')
    opc = input('Escolha (1/2): ').strip()
    
    if opc == '1':
        a = ler_float('Informe a (λ/μ) em Erlangs: ')
        c = ler_int('Informe c (nº de servidores): ')
        lam = None
        mu = None
    elif opc == '2':
        lam = ler_float('Informe λ (taxa de chegadas): ')
        mu  = ler_float('Informe μ (taxa de atendimento por servidor): ')
        c   = ler_int('Informe c (nº de servidores): ')
        if mu <= 0:
            print('μ deve ser > 0. Encerrando.')
            return
        a = lam / mu
        print(f'a = λ/μ = {a:.6f} Erlangs')
    else:
        print('Opção inválida. Encerrando.')
        return

    # Calcula P(wait)
    p = erlang_c(a, c)
    
    print(f'\nP(wait) = {p:.6f}  ({p*100:.2f}%)')
    
    # Se o sistema for instável
    if a >= c:
        print('Atenção: a ≥ c ⇒ sistema instável (fila explode).')
        return

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

if __name__ == '__main__':
    while True:
        main()
        denovo = input('\nDeseja calcular novamente? (s/n): ').strip().lower()
        if denovo != 's':
            print('Encerrado.')
            break
