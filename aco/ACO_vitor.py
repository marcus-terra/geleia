from pyeasyga import pyeasyga
import numpy as np
from random import randrange
from enum import Enum

horarios_dia = 2
dias_semana = 5

horarios_semana = lambda:[None for i in range(horarios_dia * dias_semana)]

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

ga = pyeasyga.GeneticAlgorithm(data)

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
	individual[randrange(0, len(individual))] = data[randrange(0, len(individual))]
	return individual

ga.mutate_function = mutate

ga.run()