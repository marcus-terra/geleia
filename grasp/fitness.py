### FUNCAO OBJETIVO (FITNESS)
### AS FORMAS DO CALCULO ESTAO DEFINIDAS NOS COMENTARIOS DENTRO DA FUNCAO
### É UMA FUNCAO DE MINIMIZACAO QUE RETORNA VALOR ENTRE 0 E 1 
def funcao_objetivo(solucao):
    
    violacoes = 0;
# A mesma sala não poderá ter mais de uma aula ao mesmo tempo;
# Essa restrição é atendida sempre devido a forma como a grade é montada

# 1) A mesma aula não poderá acontecer simultaneamente em salas diferentes;
# 2) Um professor não poderá dar 2 ou mais aulas ao mesmo tempo;
# A premissa 2) já engloba a premissa 1) pois cada disciplina
# tem sempre o mesmo professor
    total_dias = 5
    total_horarios = 2
    total_salas = 5
    for dia in range(total_dias):
        for horario in range(total_horarios):
            for sala_atual in range(total_salas):
                evento_atual = dia*total_dias*total_horarios+horario*total_salas+sala_atual 
                professor_atual = solucao[evento_atual][1]
                if (professor_atual != 'VAGO'):
                    for proxima_sala in range(sala_atual+1,total_salas):
                        proximo_evento = dia*total_dias*total_horarios+horario*total_salas+proxima_sala
                        proximo_professor = solucao[proximo_evento][1]
                        if (professor_atual == proximo_professor):
                            violacoes+=1
                            # evita a recontagem quando o mesmo professor 
                            # aparece mais de 2 vezes no mesmo dia e horario
                            break


# Caso a carga horária de uma aula seja maior que um 1 horário por semana,
# é desejável que as aulas não sejam na sequência imediata (mesmo dia);
# Como é uma premissa desejável e não obrigatória o peso da violacao é 0.1
    
    for dia in range(total_dias):
        for sala_h1 in range(total_salas):
            evento_h1 = dia*total_dias*total_horarios+sala_h1
            disciplina_h1 = solucao[evento_h1][0]
            if (disciplina_h1 != 'VAGO'):
                for sala_h2 in range(total_salas):
                    evento_h2 = dia*total_dias*total_horarios+sala_h2+total_salas
                    disciplina_h2 = solucao[evento_h2][0]
                    if (disciplina_h1 == disciplina_h2): # a mesma disciplina acontece no mesmo dia
                        if (sala_h1 == sala_h2): # se for na mesma sala a penalizacao reduz pela metade
                            violacoes+=0.05
                        else:
                            violacoes+=0.1
                        # a regra anterior já penaliza a mesma disciplina no mesmo horário
                        # assim para não penalizar novamente o laço é interrompido
                    break 
    

# É desejável que não existam buracos (horários/salas sem aula)
# na grade de horário
# Considera-se o número total de posicoes da grade (salas*dias*horarios) = 50 
# Como é uma premissa desejável e não obrigatória o peso da violacao é 0.1
    
    solucao_reversa = copy.deepcopy(solucao)
    solucao_reversa.reverse()
    buracos = 0;
    posicao_inicial = 0;
    while (posicao_inicial < 50 and solucao_reversa[posicao_inicial][1] == 'VAGO'):
        posicao_inicial+=1
    for i in range(posicao_inicial+1, len(solucao_reversa)):
        if (solucao_reversa[i][0] == 'VAGO'):
            buracos+=1
    violacoes = violacoes + 0.1*buracos;

# Solucao alternativa para as salas vagas (buracos na grade)
# Como não foi identificado problema de performance
# foi mantida a outra alternativa

    
#    ultimo_horario_ocupado = -1
#    salas_ocupadas = 0;
#    for i in range(0, len(solucao)):
#        if (solucao[i][0] != 'VAGO'):
#            ultimo_horario_ocupado = i
#            salas_ocupadas +=1
     # total de salas até o ultimo horario ocupado
#    total_de_salas = ultimo_horario_ocupado + 1
#    salas_vagas = total_de_salas - salas_ocupadas
#    violacoes = violacoes + 0.1*salas_vagas
 

# OBS: Uma questao importante é saber se o peso da violacao 
# de deixar um horario vago deve ser o mesmo que 
# colocar a mesma disciplina em sequencia

# O fitness (funcao objetivo) será :
# Melhor - quanto mais se aproximar de 0 (menos violacoes)
# Pior - quanto mais se aproximar de 1 (mais violacoes)
    custo = 1 - 1 / (1 * violacoes + 1);
    return custo
