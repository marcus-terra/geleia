import copy
import constantes as const

### FUNCAO OBJETIVO (FITNESS)
### AS FORMAS DO CALCULO ESTAO DEFINIDAS NOS COMENTARIOS DENTRO DA FUNCAO
### É UMA FUNCAO DE MINIMIZACAO QUE RETORNA VALOR ENTRE 0 E 1 
def funcao_objetivo(grade):
    
    violacoes = 0;
# A mesma sala não poderá ter mais de uma aula ao mesmo tempo;
# Essa restrição é atendida sempre devido a forma como a grade é montada

# 1) A mesma aula não poderá acontecer simultaneamente em salas diferentes;
# 2) Um professor não poderá dar 2 ou mais aulas ao mesmo tempo;
# A premissa 2) já engloba a premissa 1) pois cada disciplina
# tem sempre o mesmo professor
    
    for dia in range(const.TOTAL_DIAS):
        for horario in range(const.TOTAL_HORARIOS_DIA):
            for sala_atual in range(const.TOTAL_SALAS):
                evento_atual = dia*const.TOTAL_DIAS*const.TOTAL_HORARIOS_DIA+horario*const.TOTAL_SALAS+sala_atual 
                professor_atual = grade[evento_atual][const.INDICE_PROFESSOR]
                if (professor_atual != const.HORARIO_VAGO):
                    for proxima_sala in range(sala_atual+1,const.TOTAL_SALAS):
                        proximo_evento = dia*const.TOTAL_DIAS*const.TOTAL_HORARIOS_DIA+horario*const.TOTAL_SALAS+proxima_sala
                        proximo_professor = grade[proximo_evento][const.INDICE_PROFESSOR]
                        if (professor_atual == proximo_professor):
                            violacoes += const.PESO_PROF_MESMO_HORARIO
                            # evita a recontagem quando o mesmo professor 
                            # aparece mais de 2 vezes no mesmo dia e horario
                            break


# Caso a carga horária de uma aula seja maior que um 1 horário por semana,
# é desejável que as aulas não sejam na sequência imediata (mesmo dia);
# Como é uma premissa desejável e não obrigatória o peso da violacao é 0.1
    
    for dia in range(const.TOTAL_DIAS):
        for sala_h1 in range(const.TOTAL_SALAS):
            evento_h1 = dia*const.TOTAL_DIAS*const.TOTAL_HORARIOS_DIA+sala_h1
            disciplina_h1 = grade[evento_h1][const.INDICE_DISCIPLINA]
            if (disciplina_h1 != const.HORARIO_VAGO):
                for sala_h2 in range(const.TOTAL_SALAS):
                    evento_h2 = dia*const.TOTAL_DIAS*const.TOTAL_HORARIOS_DIA+sala_h2+const.TOTAL_SALAS
                    disciplina_h2 = grade[evento_h2][const.INDICE_DISCIPLINA]
                    if (disciplina_h1 == disciplina_h2): # a mesma disciplina acontece no mesmo dia
                        if (sala_h1 == sala_h2): # se for na mesma sala a penalizacao reduz pela metade
                            violacoes+=const.PESO_DISC_MESMO_DIA_SALA_IGUAL
                        else:
                            violacoes+=const.PESO_DISC_MESMO_DIA_SALA_DIFER
                        # a regra anterior já penaliza a mesma disciplina no mesmo horário
                        # assim para não penalizar novamente o laço é interrompido
                        break 
    

# É desejável que não existam buracos (horários/salas sem aula)
# na grade de horário
# Considera-se o número total de posicoes da grade (salas*dias*horarios) = 50 
# Como é uma premissa desejável e não obrigatória o peso da violacao é:
# 0.1 Se o horário vago for o primeiro do dia
# 0.05 Se o horario vago for o segundo do dia
    
    posicao_final = const.TOTAL_HORARIOS_GRADE - 1;
    while (posicao_final > -1 and grade[posicao_final][const.INDICE_PROFESSOR] == const.HORARIO_VAGO):
        posicao_final -= 1
    for i in range(0, posicao_final+1):
        if (grade[i][const.INDICE_PROFESSOR] == const.HORARIO_VAGO):
            if ((i // const.TOTAL_SALAS) % 2 == 0): # o horario sem aula é o primeiro do dia
               violacoes+=const.PESO_PRIMEIRO_HORARIO_VAGO
            else:
               violacoes+=const.PESO_SEGUNDO_HORARIO_VAGO # o horario sem aula é o segundo do dia (penalização menor)


# OBS: Uma questao importante é saber se o peso da violacao 
# de deixar um horario vago deve ser o mesmo que 
# colocar a mesma disciplina em sequencia no dia

# O fitness (funcao objetivo) será :
# Melhor - quanto mais se aproximar de 0 (menos violacoes)
# Pior - quanto mais se aproximar de 1 (mais violacoes)
    fitness = 1 - 1 / (1 * violacoes + 1);
    return fitness
