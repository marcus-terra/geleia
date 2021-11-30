import copy
import random
import numpy.random as npr

# probs = probalidades de seguir cada um dos caminhos

def funcao_objetivo(aulas, grade):
    return

def calcula_eta(aulas, grade, eta_atual, caminhos_possiveis):
    for (i in len(caminho_possiveis)):
        grade_possivel = copy.deepcopy(grade)
        grade_possivel.append(cp)
        eta[i] = # heuristica/fitness aula, grade_possivel
    return eta

def calcula_probabilidades(tau, eta, alfa, beta, caminhos_possiveis): 
    return

def aco_construcao(aulas, tau, alfa, beta):
    solucao = [[],float("inf")]
    grade = []
    caminhos_possiveis = #vetor de 0 a 49
    eta_atual = 0
    posicao_inicial = random.randrange(len(aulas))
    grade.append(posicao_inicial)
    caminhos_possiveis.remove(posicao_inicial)
    posicao_atual = posicao_inicial
    while (caminho_possiveis > 0):
        eta = calcula_eta(aulas, grade, eta_atual, caminhos_possiveis)
        probabilidades = calcula_probabilidades(tau[posicao_atual], eta, alfa, beta, caminhos_possiveis) # o tau sera somente da linha da posicao_atual
        proxima_posicao = npr.choice(len(probabilidades), p=probabilidades)] # roleta
        grade.append(proxima_posicao)
        caminhos_possiveis.remove(proxima_posicao)
        eta_atual = eta[proxima_posicao]
    solucao[0] = grade
    solucao[1] = funcao_objetivo(aulas,grade)
    return solucao

def deposita_feromonio(Q,delta_tau,melhor_solucao):
    return

def atualiza_feromonios(tau, ro, delta_tau):
    return


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
              qtde_formigas = 50):
    contador = 0
    melhor_solucao = solucao_inicial
    delta_tau = 
    tau = 
    while (contador < max_iteracoes and melhor_solucao[1]>limite):
        for (i in range(qtde_formigas)):
            solucao = aco_construcao(aulas, tau, alfa, beta)
            if (solucao[1] < melhor_solucao[1]):
                melhor_solucao = solucao
            delta_tau = deposita_feromonio(Q, delta_tau, melhor_solucao)
        tau = atualiza_feronomios(tau, ro, delta_tau)
        contador += 1
        print('Iteracao =', contador, '-> Custo Solucao =', melhor_solucao[1])
    return melhor_solucao
