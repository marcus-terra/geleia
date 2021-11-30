import copy
import random
import numpy as np


# probs = probalidades de seguir cada um dos caminhos

def funcao_objetivo(aulas, posicoes_grade):
    
# CONFIGURACAO DA GRADE ESCOLAR
    TOTAL_DIAS = 5
    TOTAL_SALAS = 5
    TOTAL_HORARIOS_DIA = 2
    TOTAL_HORARIOS_GRADE = TOTAL_DIAS * TOTAL_SALAS * TOTAL_HORARIOS_DIA

# INDICES (POSICOES) DOS ELEMENTOS NO VETOR AULAS [PROFESSOR, DISCIPLINA]
    INDICE_PROFESSOR = 0
    INDICE_DISCIPLINA = 1

# REPRESENTACAO HORARIO VAGO NA GRADE
    HORARIO_VAGO = 'HV'

# PESO DAS VIOLACOES NA FUNCAO OBJETIVO (FITNESS)
    PESO_PROF_MESMO_HORARIO = 1
    PESO_DISC_MESMO_DIA_SALA_DIFER = 0.1
    PESO_DISC_MESMO_DIA_SALA_IGUAL = 0.05
    PESO_PRIMEIRO_HORARIO_VAGO = 0.1
    PESO_SEGUNDO_HORARIO_VAGO = 0.05
    
    grade = [HORARIO_VAGO] * TOTAL_HORARIOS_GRADE # preencher todas as 50 posicoes com o mesmo valor 'HV'
    for (i in range(posicoes_grade)):
        grade[i] = aulas[posicoes_grade[i]]
        
    violacoes = 0;
    
# A mesma sala não poderá ter mais de uma aula ao mesmo tempo;
# Essa restrição é atendida sempre devido a forma como a grade é montada

# 1) A mesma aula não poderá acontecer simultaneamente em salas diferentes;
# 2) Um professor não poderá dar 2 ou mais aulas ao mesmo tempo;
# A premissa 2) já engloba a premissa 1) pois cada disciplina
# tem sempre o mesmo professor
    
    for dia in range(TOTAL_DIAS):
        for horario in range(TOTAL_HORARIOS_DIA):
            for sala_atual in range(TOTAL_SALAS):
                evento_atual = dia*TOTAL_DIAS*TOTAL_HORARIOS_DIA+horario*TOTAL_SALAS+sala_atual 
                professor_atual = grade[evento_atual][INDICE_PROFESSOR]
                if (professor_atual != HORARIO_VAGO):
                    for proxima_sala in range(sala_atual+1,TOTAL_SALAS):
                        proximo_evento = dia*TOTAL_DIAS*TOTAL_HORARIOS_DIA+horario*TOTAL_SALAS+proxima_sala
                        proximo_professor = grade[proximo_evento][INDICE_PROFESSOR]
                        if (professor_atual == proximo_professor):
                            violacoes += PESO_PROF_MESMO_HORARIO
                            # evita a recontagem quando o mesmo professor 
                            # aparece mais de 2 vezes no mesmo dia e horario
                            break


# Caso a carga horária de uma aula seja maior que um 1 horário por semana,
# é desejável que as aulas não sejam na sequência imediata (mesmo dia);
# Como é uma premissa desejável e não obrigatória o peso da violacao é 0.1
    
    for dia in range(TOTAL_DIAS):
        for sala_h1 in range(TOTAL_SALAS):
            evento_h1 = dia*TOTAL_DIAS*TOTAL_HORARIOS_DIA+sala_h1
            disciplina_h1 = grade[evento_h1][INDICE_DISCIPLINA]
            if (disciplina_h1 != HORARIO_VAGO):
                for sala_h2 in range(TOTAL_SALAS):
                    evento_h2 = dia*TOTAL_DIAS*TOTAL_HORARIOS_DIA+sala_h2+TOTAL_SALAS
                    disciplina_h2 = grade[evento_h2][INDICE_DISCIPLINA]
                    if (disciplina_h1 == disciplina_h2): # a mesma disciplina acontece no mesmo dia
                        if (sala_h1 == sala_h2): # se for na mesma sala a penalizacao reduz pela metade
                            violacoes+=PESO_DISC_MESMO_DIA_SALA_IGUAL
                        else:
                            violacoes+=PESO_DISC_MESMO_DIA_SALA_DIFER
                        # a regra anterior já penaliza a mesma disciplina no mesmo horário
                        # assim para não penalizar novamente o laço é interrompido
                        break 
    

# É desejável que não existam buracos (horários/salas sem aula)
# na grade de horário
# Considera-se o número total de posicoes da grade (salas*dias*horarios) = 50 
# Como é uma premissa desejável e não obrigatória o peso da violacao é:
# 0.1 Se o horário vago for o primeiro do dia
# 0.05 Se o horario vago for o segundo do dia
    
    posicao_final = TOTAL_HORARIOS_GRADE - 1;
    while (posicao_final > -1 and grade[posicao_final][INDICE_PROFESSOR] == HORARIO_VAGO):
        posicao_final -= 1
    for i in range(0, posicao_final+1):
        if (grade[i][INDICE_PROFESSOR] == HORARIO_VAGO):
            if ((i // TOTAL_SALAS) % 2 == 0): # o horario sem aula é o primeiro do dia
               violacoes+=PESO_PRIMEIRO_HORARIO_VAGO
            else:
               violacoes+=PESO_SEGUNDO_HORARIO_VAGO # o horario sem aula é o segundo do dia (penalização menor)


# OBS: Uma questao importante é saber se o peso da violacao 
# de deixar um horario vago deve ser o mesmo que 
# colocar a mesma disciplina em sequencia no dia

# O fitness (funcao objetivo) será :
# Melhor - quanto mais se aproximar de 0 (menos violacoes)
# Pior - quanto mais se aproximar de 1 (mais violacoes)
    fitness = 1 - 1 / (violacoes + 1);
    return fitness
    

def calcula_eta(aulas, posicoes_grade, caminhos_possiveis):
    eta = [0] * len(caminhos_possiveis)# tamanho do caminhos_possiveis
    for (i in len(caminhos_possiveis)):
        grade_possivel = copy.deepcopy(posicoes_grade)
        grade_possivel.append(caminhos_possiveis[i])
        eta[i] = 1 - funcao_objetivo(aulas,grade_possivel) # heuristica/fitness (aula, grade_possivel)
    return eta

def calcula_probabilidades(tau_i, eta, alfa, beta, caminhos_possiveis): 
    probabilidade = [0]*len(caminho_possiveis)
    somatorio = 0
    for (l in len(caminhos_possiveis))
        somatorio = somatorio + ((tau_i[caminhos_possiveis[l]]**alfa) * (eta[l]**beta))
    for (j in len(caminhos_possiveis))
        probabilidade[j] = (tau_i[caminhos_possiveis[j]]**alfa * eta[j]**beta)/somatorio
    return probabilidade

def aco_construcao(aulas, tau, alfa, beta):
    solucao = [[],float("inf")]
    posicoes_grade = []
    caminhos_possiveis = list(range(50)) #vetor de 0 a 49
    posicao_inicial = random.randrange(len(aulas))
    posicoes_grade.append(posicao_inicial)
    caminhos_possiveis.remove(posicao_inicial)
    posicao_atual = posicao_inicial
    while (caminho_possiveis > 0):
        eta = calcula_eta(aulas, grade, caminhos_possiveis)
        probabilidades = calcula_probabilidades(tau[posicao_atual,:], eta, alfa, beta, caminhos_possiveis) # o tau sera somente da linha da posicao_atual
        proxima_posicao = np.random.choice(len(probabilidades), p=probabilidades)] # roleta
        posicoes_grade.append(proxima_posicao)
        caminhos_possiveis.remove(proxima_posicao)
    solucao[0] = posicoes_grade
    solucao[1] = funcao_objetivo(aulas,grade)
    return solucao

def deposita_feromonio(Q,delta_tau,melhor_solucao):
    delta_tau_novo = [[0 for col in range(50)] for lin in range(50)]
    for (c in range(0,len(melhor_solucao[0])-1)):
        i = melhor_solucao[0][c]
        j = melhor_solucao[0][c+1]
        delta_tau_novo[i][j] = delta_tau[i][j] + Q/melhor_solucao[1]
    return delta_tau_novo

def atualiza_feromonios(tau, ro, delta_tau):
    tau_novo = copy.deepcopy(tau)
    for (i in range(50)):
        for (j in range(50)):
            tau_novo[i][j] = ro*tau[i][j] + delta_tau[i][j]
    return tau_novo


# Q = quantidade de feromônio excretada por uma formiga a cada iteração (Padrão = 1)
# tau_0 = valor inicial para todos os feronômios (Padrão = 1)
# ro = taxa de evaporação de feromônio entre [0,1] (Padrão = 0.5)
# eta = visilibilidade ou heurística dos caminhos 
# alfa = grau de influência do feromônio
# beta = grau de influência da heuristica
def aco_grade(aulas,
              solucao_inicial = [[],float("inf")],
              max_iteracoes = 1000,
              limite = 0,
              Q = 1,
              tau_0 = 1,
              ro = 0.5,
              qtde_formigas = 5):
    contador = 0
    melhor_solucao = solucao_inicial
    delta_tau = [[0 for col in range(50)] for lin in range(50)]
    tau = [[tau_0 for col in range(50)] for lin in range(50)]
    while (contador < max_iteracoes and melhor_solucao[1]>limite):
        for (i in range(qtde_formigas)):
            solucao = aco_construcao(aulas, tau, alfa, beta)
            if (solucao[1] < melhor_solucao[1]):
                melhor_solucao = solucao
            # elitista, reforça sempre a melhor solucao, mas nao sei se deposita sempre ou só quando encontra uma nova melhor solução     
            delta_tau = deposita_feromonio(Q, delta_tau, melhor_solucao) 
            # atualiza delta_tau para todas as solucoes
            # delta_tau = deposita_feromonio(Q, delta_tau, solucao) 
        tau = atualiza_feromonios(tau, ro, delta_tau)
        contador += 1
        print('Iteracao =', contador, '-> Custo Solucao =', melhor_solucao[1])
    return melhor_solucao
