from pyeasyga import pyeasyga
import numpy as np
from random import randrange
from enum import Enum

horarios_dia = 2
dias_semana = 5

horarios_semana = lambda:[None for i in range(horarios_dia * dias_semana)]

class Penalizacoes(Enum):
	disponibilidade = 30

# 1 == indisponível
# 0 == disponível
disponibilidade_professores = {
	'professor1': [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
	'professor2': [0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
	'professor3': [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	'professor4': [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
	'professor5': [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
	'topaTudoPorDinheiro': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	'preguicoso': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
}

class Disciplina(Enum):
    portugues = 'portugues'
    matematica = 'matematica'
    historia = 'historia'
    geografia = 'geografia'

data = [{'nome_professor': 'professor1', 'disciplina_nome': Disciplina.portugues},
		{'nome_professor': 'professor2', 'disciplina_nome': Disciplina.matematica},
		{'nome_professor': 'professor3', 'disciplina_nome': Disciplina.historia},
		{'nome_professor': 'professor4', 'disciplina_nome': Disciplina.geografia},
		{'nome_professor': 'professor5', 'disciplina_nome': Disciplina.portugues},
		{'nome_professor': 'topaTudoPorDinheiro', 'disciplina_nome': Disciplina.matematica},
		{'nome_professor': 'preguicoso', 'disciplina_nome': Disciplina.matematica}]

# Adicionando mais um valor com None pra representar ausência de professor
data = data + [None]

ga = pyeasyga.GeneticAlgorithm(data, maximise_fitness=False)

def create_individual(data):
	# Retorna um vetor do tamanho de horários disponíveis preenchido com os professores 
	return [data[randrange(0, len(data))] for i in range(horarios_dia * dias_semana)]

ga.create_individual = create_individual

def fitness(individual, data):
	return 10

ga.fitness_function = fitness

def crossover(parent_1, parent_2):
	crossover_index = randrange(1, len(parent_1))
	child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
	child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
	return child_1, child_2

ga.crossover_function = crossover

def mutate(individual):
	individual[randrange(0, len(individual))] = data[randrange(0, len(data))]
	return individual

ga.mutate_function = mutate

ga.run()

for professor in ga.best_individual()[1]:
	print(professor, '\n')
print('\n')
print(ga.best_individual(), '\n')
print(ga.last_generation(), '\n')