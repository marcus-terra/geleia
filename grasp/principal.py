import copy
import random
import numpy  as np
import pandas as pd
import fitness
import grasp

### GERA UMA SOLUCAO ALEATORIA [GRADE DE HORARIOS,FITNESS DA SOLUCAO] 
### COM BASE NO CONJUNTO DE AULAS NECESSARIAS 
### (DISCIPLINA, PROFESSOR)

def solucao_aleatoria(aulas):
    solucao = [[],float("inf")]
    # Solucao alternativa que gerar uma sequencia aleatorias de 50 numeros 
    # entre 0 e 49 que representam a ordem das aulas
    #sequencia = random.sample(list(range(0,len(aulas))), len(aulas))
    #solucao[0] = sequencia
    #solucao[1] = funcao_objetivo(aulas, sequencia)
    solucao[0] = random.sample(aulas, len(aulas))
    solucao[1] = fitness.funcao_objetivo(solucao[0])
    return solucao

### FUNCAO QUE TRANSFORMA A ESTRUTURA DO TIPO
### [DISCIPLINA, PROFESSOR, QUANTIDADE DE HORARIOS EXIGIDO PELA DISCIPLINA] 
### EM UMA ESTRUTURA (GRADE) DE AULAS NECESSARIAS DO TIPO [DISCIPLINA, PROFESSOR]
### ONDE É REPLICADO O VALOR [DISCIPLINA, PROFESSOR] DE ACORDO COM A QUANTIDADE
### DE HORARIOS DE CADA DISCIPLINA EXIGE, COMO A GRADE COMPORTA ATÉ 50 HORÁRIOS 
### (NUMERO DE DIAS X NUMERO DE HORARIOS NO DIA X NUMERO DE SALAS), 
### CASO QUANTIDADE DE AULAS NECESSARIAS SEJA MENOR QUE O TAMANHO DA GRADE (50)
### O RESTANTE DA GRADE É PREENCHIDO COM VALORES ['VAGO','VAGO']

def gera_aulas(disc_prof_hor):
    # dt = np.dtype([('disciplina', np.unicode_, 4), ('professor', np.unicode_, 4)])
    aulas = [] 
    for i in range(0, disc_prof_hor.shape[0]):
        aula = disc_prof_hor[i] 
        num_periodos = aula[2]
        for j in range(0, num_periodos):
          aulas.append((aula[0],aula[1]))
    # Se a quantidade de aulas < 50 preenche a lista aulas com valores VAGO
    for i in range(len(aulas),50):
        aulas.append(('VAGO','VAGO'))
    return aulas #np.array(aulas,dt)

### FUNCAO QUE IMPRIME UMA SOLUCAO [GRADE DE HORARIOS, FITNESS DA SOLUCAO]
### DE FORMA AMIGÀVEL

def imprime_solucao(solucao):
    dias = ['Segunda','Terça','Quarta','Quinta','Sexta']
    for i in range(0,len(solucao[0])):
        dia = dias[i//10]
        if (i % 10 == 0):
            print('\n\n',dia)
        if (i % 5 == 0):
            print('\nHorario ', 1+ i % 2, '--------------------')
        print(solucao[0][i], end = ' | ')
    print('\nCusto da Solucao = ',solucao[1])    
    return

### METODO PRINCIPAL QUE RECEBE A URL DO CASO DE TESTE E RETORNA 
### A MELHOR SOLUCAO [GRADE DE HORARIOS, FITNESS DA SOLUCAO] ENCONTRADA
### 
def principal(url_caso_de_teste, max_iteracoes = 1000, calcula_solucao_inicial = true):
    disc_prof_hor = pd.read_csv(url_caso_de_teste, sep = ';')
    disc_prof_hor = disc_prof_hor.values
    aulas = gera_aulas(disc_prof_hor)
    if (calcula_solucao_inicial):
        solucao_inicial = solucao_aleatoria(aulas)      
        melhor_solucao = grasp.grasp_grade(aulas, solucao_inicial, max_iteracoes)
    else:
        melhor_solucao = grasp.grasp_grade(aulas, max_iteracoes = max_iteracoes)
    imprime_solucao(melhor_solucao)
    return
