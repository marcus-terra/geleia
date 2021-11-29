import copy
import random

# prob = probalidades de seguir um caminho

def aco_construcao(aulas, tau, eta, alfa, beta):
    grade = []
    caminho_possiveis = copy.deepcopy(aulas)
    qtde_aulas = len(aulas)
    posicao_inicial = random.randrange(qtde_aulas)
    grade.append(aulas[posicao_inicial])
    while (len(grade) < qtde_aulas):
      eta = calcula_eta(grade, caminho_impossiveis)
      prob = calcula_probabilidade(tau, eta, alfa, beta, caminhos_impossiveis) 

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
            deposita_feromonio(Q,delta_tau,melhor_solucao)
        atualiza_feronomios(tau, ro, delta_tau)
        contador += 1
        #print('\rIteracao =', contador, '-> Custo Solucao =', melhor_solucao[const.INDICE_FITNESS], end='')
        print('Iteracao =', contador, '-> Custo Solucao =', melhor_solucao[const.INDICE_FITNESS])
    return melhor_solucao
