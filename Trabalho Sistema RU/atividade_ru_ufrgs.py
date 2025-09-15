# -*- coding: utf-8 -*-
"""
# Atividade Restaurante Universitário
# Aluno: José Otávio R. Baggio

Simulação do uso do RU (Restaurante Universitário) por alunos da UFRGS.
Objetivos:
- Implementar um modelo discreto por eventos para o fluxo de entrada no RU.
- Consolidar o uso de listas/dicionários, funções e manipulação de estado do sistema.
- Produzir saídas claras para análise e validação.
"""

# Lista de alunos:
alunos = [
    {'matricula': 'UFRGS2025125', 'nome': 'Laura Baggio', 'creditos': 5},
    {'matricula': 'UFRGS2025003', 'nome': 'Casimiro Miguel', 'creditos': 2},
    {'matricula': 'UFRGS2025085', 'nome': 'Naruto Uzumaki', 'creditos': 1},
    {'matricula': 'UFRGS2025045', 'nome': 'Son Goku', 'creditos': 0}
]

# Dicionário que representa o estado atual do RU:
ru = {
    'nome': 'Restaurante Universitário do Campus Litoral Norte',
    'total_atendimentos': 0,
    'total_negados_sem_credito': 0
}

# --- FUNÇÕES ---

def encontrar_aluno(matricula):
    """
    Retorna o dicionário do aluno com a matrícula fornecida,
    ou None se não encontrado.
    """
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None  

def usar_refeicao(matricula):
    """
    Verifica se o aluno tem crédito suficiente para usar o RU.
    Atualiza os contadores de atendimentos e imprime a resposta.
    """
    aluno = encontrar_aluno(matricula)

    if aluno is None:
        print(f"[ERRO] Matrícula {matricula} não encontrada!")
        return

    if aluno['creditos'] >= 1:
        aluno['creditos'] -= 1
        ru['total_atendimentos'] += 1
        print(f"[LIBERADO] {aluno['nome']} ({matricula}) utilizou 1 crédito. Créditos restantes: {aluno['creditos']}")
    else:
        ru['total_negados_sem_credito'] += 1
        print(f"[NEGADO] {aluno['nome']} ({matricula}) sem créditos. Por favor, recarregue o cartão.")

# Lista que simula os eventos de entrada no RU:
eventos_simulados = [
    'UFRGS2025125',  # Laura - OK
    'UFRGS2025899',  # Não cadastrado
    'UFRGS2025085',  # Naruto - OK
    'UFRGS2025003',  # Casimiro - OK
    'UFRGS2025045'   # Goku - NEGADO
]

# Processamento dos eventos simulados:
for matricula in eventos_simulados:
    usar_refeicao(matricula)

# Relatório final:
print("\n--- RELATÓRIO FINAL ---")
print(f"Total de atendimentos liberados: {ru['total_atendimentos']}")
print(f"Total de refeições negadas (sem crédito): {ru['total_negados_sem_credito']}")
print("\nCréditos remanescentes por aluno:")
for aluno in alunos:
    print(f"{aluno['nome']} ({aluno['matricula']}): {aluno['creditos']} créditos")