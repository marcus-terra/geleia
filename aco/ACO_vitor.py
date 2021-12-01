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
		{'nome_professor': 'professor5', 'disciplina_nome': Disciplina.portugues}]

ga = pyeasyga.GeneticAlgorithm(data)

def create_individual(data):
	# Adiciona um horário vago temporariamente na lista de professores
	data = data + [None]
	# Retorna um vetor do tamanho de horários disponíveis preenchido com os professores 
	return [data[randrange(0, len(data))] for i in range(horarios_dia * dias_semana)]

ga.create_individual = create_individual

def fitness(individual, data):
	pass

ga.fitness_function = fitness

def crossover(parent_1, parent_2):
	pass

ga.crossover_function = crossover

def mutate(individual):
	pass

ga.mutate_function = mutate

ga.run()