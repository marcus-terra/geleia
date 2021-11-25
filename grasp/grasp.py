import copy
import random
import fitness

### FUNCAO AUXILIAR DA "CALCULA_RCL" QUE DETERMINA O CUSTO DE SELEÇÃO DO
### PROXIMO PROFESSOR PARA A GRADE
### O CUSTO É BASEADO NA QUANTIDADE DE AULAS (HORARIOS) QUE UM PROFESSOR PRECISA
### MINISTRAR
### QUANTO MAIS AULAS -> MENOR O CUSTO PARA ESCOLHER ESSE PROFESSOR

def calcula_custos(candidatos):
    custos = []
    professores = []
    for i in range(0, len(candidatos)):
        if (candidatos[i][0] != 'VAGO'):
            professores.append(candidatos[i][0])
    for i in range(0, len(candidatos)):
        custo = 50 - professores.count(candidatos[i][0])
        custos.append(custo)
    return custos


### FUNCAO AUXILIAR DA "GRASP_CONSTRUCAO" QUE CONSTROI A LISTA RESTRITA DE
### CANDIDATOS - RCL (restricted candidate list) 
### A FUNCAO AVALIA OS CUSTOS DE CADA AULA CANDIDATA COM BASE NOS CUSTOS
### MÍNIMO E MÁXIMO ATUAIS E NO FATOR DE ALEATORIEDADE (ALFA_RCL)
### ALFA_RCL PRÓXIMO A ZERO -> BUSCA MAIS GULOSA
### ALFA_RCL PRÓXIMO A UM   -> BUSCA MAIS ALEATORIA 

def calcula_rcl(candidatos, custos, custo_min, custo_max, alfa_rcl):
    rcl = []
    for i in range(0, len(candidatos)):
        if (custos[i] <= custo_min + alfa_rcl*(custo_max - custo_min)):
            rcl.append(candidatos[i])
    return rcl

### FUNCAO DE CONSTRUCAO DE UMA SOLUCAO [GRADE DE HORARIOS,FITNESS DA SOLUCAO] 
### UTILIZANDO A META-HEURÍSTICA GRASP 
### (GREEDY RANDOMIZED ADAPTIVE SEARCH PROCEDURE)
### COM BASE NO CONJUNTO DE AULAS NECESSARIAS (DISCIPLINA, PROFESSOR)
### E NO FATOR DE ALEATORIEDADE DA RCL (ALFA_RCL)
### ALFA_RCL PRÓXIMO A ZERO -> BUSCA MAIS GULOSA
### ALFA_RCL PRÓXIMO A UM   -> BUSCA MAIS ALEATORIA 

def grasp_construcao(aulas, alfa_rcl):
    solucao = [[],float("inf")]
    candidatos = copy.deepcopy(aulas)
    custos = calcula_custos(candidatos)
    while (len(candidatos) > 0):
        custo_min = min(custos)
        custo_max = max(custos)
        rcl = calcula_rcl(candidatos, custos, custo_min, custo_max, alfa_rcl)
        elemento = rcl[random.randrange(len(rcl))]
        solucao[0].append(elemento)
        candidatos.remove(elemento)
        calcula_custos(candidatos)
    solucao[1] = fitness.funcao_objetivo(solucao[0])
    return solucao


### FUNCAO QUE, A PARTIR DE UMA SOLUCAO INICIAL, CALCULA UMA SOLUCAO VIZINHA
### O CALCULO É FEITO TROCANDO UMA ÚNICA POSICAO DA GRADE POR OUTRA DE FORMA 
### ALEATORIA (EX.: TROCA DO PRIMEIRO HORÁRIO DA SEGUNDA PELO ÚLTIMO DA SEXTA)

def calcula_vizinho(solucao_inicial):
    # Randomizacao apenas trocando as aulas no mesmo dia
    #horarios = random.sample(list(range(0,10)), 2)
    #sala = random.randrange(5)
    #trocas = [horarios[0]+10*sala, horarios[1]+10*sala]

    # Randomizacao trocando todas as posicoes na grade
    trocas = random.sample(list(range(0,len(solucao_inicial[0]))), 2)
    solucao = copy.deepcopy(solucao_inicial)
    auxiliar = solucao[0][trocas[0]]
    solucao[0][trocas[0]] = solucao[0][trocas[1]]
    solucao[0][trocas[1]] = auxiliar
    solucao[1] = fitness.funcao_objetivo(solucao[0])
    return solucao


### FUNCAO QUE A REALIZA UMA BUSCA LOCAL PELA MELHOR SOLUCAO 
### [GRADE DE HORARIOS,FITNESS DA SOLUCAO] A PARTIR DE UMA 
### SOLUCAO INICIAL. ESTA BUSCA LOCAL UTILIZA O ALGORITMO HILL CLIMBING.
### A QUANTIDADE PADRAO MÁXIMA DE SOLUCOES VIZINHAS CALCULADAS 
### PARA CADA NOVA MELHOR SOLUCAO ENCONTRADA É 1000 (MAX_ITERACOES)
### E O LIMITE PADRAO (THRESHOLD) PARA ENCERRAR A BUSCA LOCAL É ZERO

def busca_local(solucao_inicial, max_iteracoes = 1000, limite = 0):
    contador = 0
    melhor_solucao = copy.deepcopy(solucao_inicial)
    while (contador < max_iteracoes and melhor_solucao[1]>limite):
        solucao = calcula_vizinho(melhor_solucao)
        if (solucao[1] < melhor_solucao[1]):
            contador = 0
            melhor_solucao = copy.deepcopy(solucao)
        else: 
            contador = contador + 1 
    return melhor_solucao


### FUNCAO DE BUSCA DA MELHOR SOLUCAO GLOBAL [GRADE DE HORARIOS,FITNESS DA SOLUCAO] 
### UTILIZANDO A META-HEURÍSTICA GRASP 
### (GREEDY RANDOMIZED ADAPTIVE SEARCH PROCEDURE)
### COM BASE NO CONJUNTO DE AULAS NECESSARIAS (DISCIPLINA, PROFESSOR)
### NUMA SOLUCAO INICIAL (QUE PODE SER VAZIA)
### NUM NUMERO MÁXIMO DE ITERACOES DE BUSCA (MAX_ITERACOES - PADRAO = 5000)
### NO FATOR DE ALEATORIEDADE DA RCL (ALFA_RCL - PADRAO = 0.5) 
### ALFA_RCL PRÓXIMO A ZERO -> BUSCA MAIS GULOSA
### ALFA_RCL PRÓXIMO A UM   -> BUSCA MAIS ALEATORIA 
### E NO LIMITE (THRESHOLD) PARA ENCERRAR A BUSCA GLOBAL (LIMITE - PADRAO = 0)

def grasp_grade(aulas, solucao_inicial = [[],float("inf")], max_iteracoes = 5000, alfa_rcl = 0.5, limite = 0):
    contador = 0
    melhor_solucao = copy.deepcopy(solucao_inicial)
    while (contador < max_iteracoes and melhor_solucao[1]>limite):
        solucao = grasp_construcao(aulas, alfa_rcl)
        solucao = busca_local(solucao, max_iteracoes = 100, limite = limite)
        if (solucao[1] < melhor_solucao[1]):
            melhor_solucao = copy.deepcopy(solucao) 
        contador = contador + 1
        print('Iteracao =', contador, '-> Custo Solucao =', melhor_solucao[1])
    return melhor_solucao
