from AntColonyOptimization.AntColonyOptimizer import AntColonyOptimizer
import numpy as np

exampleMatrix =  np.array([[ np.inf, 	   1, 	  12, 	  65, 	   7, 	   3, 	  23, 	   2],
							[	  12, np.inf, 	   1, 	   1, 	  45, 	   6, 	  12, 	  34],
							[	  23, 	  23, np.inf, 	   1, 	  13, 	   4, 	   4, 	   5],
							[	   4, 	   1, 	   2, np.inf, 	   1, 	  43, 	  56, 	  67],
							[	  12, 	   3, 	  23, 	   3, np.inf,	   1,	   1,	  89],
							[	   5, 	  56, 	   3, 	  23, 	   3, np.inf,	   1,	  12],
							[	  61, 	   5, 	  44, 	  64, 	   4,	  24, np.inf,	   1],
							[	   4, 	  43, 	   5, 	   5, 	  35,	  12,	  34, np.inf]])

#						 	 prf1hr1|prf1hr2|prf1hr3|prf2hr1|prf2hr2|prf2hr3|prf0hr1|prf0hr2|prf0hr3
distanceMatrix =  np.array([[ np.inf, np.inf, np.inf, np.inf,      1, 	   1, 	   1, 	   1, 	   1],
							[ np.inf, np.inf, np.inf, 	   1, np.inf, np.inf, np.inf, np.inf, np.inf],
							[ np.inf, np.inf, np.inf,     10,      1, 	   1, 	   1, 	   1, 	   1],
							[ np.inf, 	   1,     10, np.inf, np.inf, 	  10, 	  10, 	  10, 	  10],
							[ 	   1, np.inf, 	   1, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
							[	  10,      1, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
							[ np.inf, 	   1, 	   1, np.inf,      1, np.inf, np.inf, np.inf, np.inf],
							[	   1, np.inf, 	   1, 	   1, np.inf, np.inf, np.inf, np.inf, np.inf],
							[	   1, 	   1, np.inf, 	   1,      1, np.inf, np.inf, np.inf, np.inf]])

acoOptmizer1 = AntColonyOptimizer(ants=100, evaporation_rate=0.1, intensification=0.1)

acoOptmizer1.fit(distanceMatrix, iterations=300, early_stopping_count=300)

acoOptmizer1.plot()

# --------------------------------------------------------------------------------------------

diasDeTrabalho = 2
horariosPorDia = 1
qtdProfessores = 2

horariosTotal = diasDeTrabalho * horariosPorDia

horariosPorProfessor = horariosTotal * qtdProfessores

