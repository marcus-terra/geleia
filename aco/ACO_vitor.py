from pyeasyga import pyeasyga
import numpy as np
from random import randrange
from enum import Enum

# Enum de penalizações
class Penalizacoes(Enum):
	indisponibilidade = 499
	horario_incompleto = 1000
	aula_extra = 10

# Enum de disciplinas
class Disciplina(Enum):
    historia = 'historia'
    portugues = 'portugues'
    geografia = 'geografia'
    matematica = 'matematica'

# Quantidade de horários por dia e dias de aula por semana, usado pra calcular os horários por semana
horarios_dia = 2
dias_semana = 5

horarios_semana = lambda:[None for i in range(horarios_dia * dias_semana)]

# Exemplo de matérias por semana necessárias para a grade de uma classe
materias_classe1 = {
	Disciplina.historia.value: 2,
	Disciplina.geografia.value: 2,
	Disciplina.portugues.value: 2,
	Disciplina.matematica.value: 3,
}

# Lista de professores disponíveis e suas matérias
data = [{'nome_professor': 'professor1', 'disciplina_nome': Disciplina.portugues},
		{'nome_professor': 'professor2', 'disciplina_nome': Disciplina.matematica},
		{'nome_professor': 'professor3', 'disciplina_nome': Disciplina.historia},
		{'nome_professor': 'professor4', 'disciplina_nome': Disciplina.geografia},
		{'nome_professor': 'professor5', 'disciplina_nome': Disciplina.portugues},
		{'nome_professor': 'topaTudoPorDinheiro', 'disciplina_nome': Disciplina.matematica},
		{'nome_professor': 'preguicoso', 'disciplina_nome': Disciplina.matematica}]

# Dicionário de disponibilidade de cada professor
# 1 == indisponível
# 0 == disponível
disponibilidade_professores = {
	'professor1': [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
	'professor2': [0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
	'professor3': [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
	'professor4': [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
	'professor5': [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
	'topaTudoPorDinheiro': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	'preguicoso': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
}

# Adicionando mais um valor com None pra representar a escolha de não colocar um professor
data = data + [None]

# Inicializando o GA
ga = pyeasyga.GeneticAlgorithm(
	data,
	maximise_fitness=False,
	population_size=300,
	generations=1000,
	crossover_probability=0.8,
	mutation_probability=0.2,
	elitism=True,
)

# Função que cria uma solução aleatória
# data é a lista de professores possíveis
# Talvez seja interessante limitar essa criação pra pegar só os professores disponíveis pra cada horário
def create_individual(data):
	# Retorna um vetor do tamanho de horários disponíveis preenchido com os professores 
	return [data[randrange(0, len(data))] for i in range(horarios_dia * dias_semana)]

ga.create_individual = create_individual

# Função de fitness
# solução é a solução cujo fitness será calculado, é um vetor com tamanho igual ao número de horários
# data é a lista de professores possíveis
def fitness(solucao, data):
	fitness_total = 0
	aulas_total = {}
	for horario in range(len(solucao)):

		professor = solucao[horario]
		if professor is not None:

			# Se professor está indisponível no horário, soma penalização de indisponibilidade
			fitness_total += disponibilidade_professores[professor['nome_professor']][horario] * Penalizacoes.indisponibilidade.value
			# Calculando total de aulas de cada matéria que teve até agora
			if professor['disciplina_nome'].value in aulas_total:
				aulas_total[professor['disciplina_nome'].value] += 1
			else:
				aulas_total[professor['disciplina_nome'].value] = 1

	# Pra cada matéria que a classe tem, vê se foram dadas as aulas necessárias
	for nome_materia, qtd_aulas in materias_classe1.items():
		aulas_excedentes = (aulas_total[nome_materia] if nome_materia in aulas_total else 0) - qtd_aulas
		# Soma a penalização de horário incompleto se faltaram aulas, se não soma a penalização de aulas a mais
		# Se não tiveram aulas a mais, soma 0
		fitness_total += aulas_excedentes * Penalizacoes.aula_extra.value if aulas_excedentes >= 0 else Penalizacoes.horario_incompleto.value
	return fitness_total

ga.fitness_function = fitness

# Função de crossover, só troca duas seções dos pais pra criar os filhos
def crossover(parent_1, parent_2):
	crossover_index = randrange(1, len(parent_1))
	child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
	child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
	return child_1, child_2

ga.crossover_function = crossover

# Função de mutação, troca o professor de algum horário por outro professor possível
# Talvez seja interessante limitar essa troca pra pegar só os professores disponíveis pro horário
def mutate(individual):
	individual[randrange(0, len(individual))] = data[randrange(0, len(data))]
	return individual

ga.mutate_function = mutate

ga.run()

# Printando os melhores indivíduos
for professor in ga.best_individual()[1]:
	print(professor, '\n')
print('\n')
print(ga.best_individual(), '\n')