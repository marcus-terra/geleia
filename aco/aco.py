import copy
import random

# probs = probalidades de seguir cada um dos caminhos

def funcao_objetivo(grade):
    return

def calcula_eta(grade, caminho_possiveis):
    return

def calcula_probabilidades(tau, eta, alfa, beta, caminhos_possiveis): 
    return

def roleta(probabilidades):
    return

def aco_construcao(aulas, tau, alfa, beta):
    solucao = [[],float("inf")]
    grade = []
    caminhos_possiveis = copy.deepcopy(aulas)
    posicao_inicial = random.randrange(len(aulas))
    primeira_aula = aula[posicao_inicial]
    grade.append(primeira_aula)
    caminhos_possiveis.remove(primeira_aula)
    while (caminho_possiveis > 0):
        eta = calcula_eta(grade, caminho_possiveis)
        probabilidades = calcula_probabilidades(tau, eta, alfa, beta, caminhos_possiveis) 
        proxima_posicao = roleta(probabilidades)
        proxima_aula = aulas[proxima_posicao]    
        grade.append(proxima_aula)
        caminhos_possiveis.remove(proxima_aula)
    solucao[0] = grade
    solucao[1] = funcao_objetivo(grade)
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
        #print('\rIteracao =', contador, '-> Custo Solucao =', melhor_solucao[const.INDICE_FITNESS], end='')
        print('Iteracao =', contador, '-> Custo Solucao =', melhor_solucao[const.INDICE_FITNESS])
    return melhor_solucao
