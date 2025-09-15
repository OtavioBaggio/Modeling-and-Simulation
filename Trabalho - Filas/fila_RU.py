import numpy as np
import matplotlib.pyplot as plt

def analisar_fila(nome_servico, horario, servidores, chegadas, tempos_atendimento):
    # Cálculo de λ (taxa de chegada)
    total_chegadas = sum(chegadas)
    lambda_taxa = total_chegadas / len(chegadas)

    # Cálculo de μ (taxa de atendimento por servidor)
    tempo_medio_atendimento = np.mean(tempos_atendimento)
    mu_taxa = 1 / tempo_medio_atendimento

    # Cálculo de ρ (ocupação)
    capacidade_total = servidores * mu_taxa
    p = lambda_taxa / capacidade_total

    # Interpretação
    if p < 0.5:
        interpretacao = "Sistema SUBUTILIZADO - Muitos servidores ociosos."
    elif p < 0.8:
        interpretacao = "Sistema EFICIENTE - Boa utilização e pouca espera."
    elif p < 1.0:
        interpretacao = "Sistema NO LIMITE - Risco de filas longas."
    else:
        interpretacao = "Sistema EM COLAPSO - A fila cresce infinitamente!"

    # Saída de resultados
    print(f"\nANÁLISE DE FILAS - {nome_servico}")
    print(f"Horário: {horario}")
    print("=====================================")
    print(f"• Total de chegadas em 30 min: {total_chegadas} pessoas")
    print(f"• Número de servidores: {servidores}")
    print(f"• Tempo médio de atendimento: {tempo_medio_atendimento:.2f} minutos")
    print("\nCÁLCULOS:")
    print(f"• λ (taxa de chegada): {lambda_taxa:.2f} pessoas/minuto")
    print(f"• μ (taxa de atendimento): {mu_taxa:.2f} atendimentos/minuto")
    print(f"• ρ (ocupação): {p:.2f}")
    print("\nINTERPRETAÇÃO:")
    print(f"• {interpretacao}")

    # Análise pessoal
    print("\nANÁLISE PESSOAL:")
    print("O RU da faculdade está em colapso, pois a taxa de chegada de estudantes é maior que a capacidade de atendimento. Isso gera filas longas e torna o serviço insatisfatório no horário de pico.")

    # ===== Gráficos =====
    minutos = np.arange(1, len(chegadas) + 1)

    plt.figure(figsize=(12,5))

    # Gráfico de chegadas
    plt.subplot(1,2,1)
    plt.bar(minutos, chegadas, color="skyblue", edgecolor="black")
    plt.title(f"Chegadas por Minuto - {nome_servico}")
    plt.xlabel("Minuto de Observação")
    plt.ylabel("Pessoas")

    # Gráfico de tempos de atendimento
    plt.subplot(1,2,2)
    plt.plot(minutos, tempos_atendimento, marker="o", color="orange")
    plt.axhline(tempo_medio_atendimento, color="red", linestyle="--", 
                label=f"Média = {tempo_medio_atendimento:.2f} min")
    plt.title(f"Tempo de Atendimento - {nome_servico}")
    plt.xlabel("Atendimento")
    plt.ylabel("Tempo (minutos)")
    plt.legend()

    plt.tight_layout()
    plt.show()


# ================== DADOS RU ==================
chegadas_ru = [3,4,2,5,3,4,3,3,2,4,3,3,5,4,3,2,3,3,4,3,2,3,4,3,3,2,4,3,3,3]
tempos_ru = [2.1, 2.0, 2.2, 1.8, 2.5, 1.9, 2.3, 2.1, 2.0, 2.4] * 3

analisar_fila("RU da Faculdade", "12h às 12h30", servidores=3,
              chegadas=chegadas_ru, tempos_atendimento=tempos_ru)

