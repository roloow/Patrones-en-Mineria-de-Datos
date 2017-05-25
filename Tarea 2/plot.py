# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
######################################################
#                      Parte 1
######################################################
"""
Esta sección está realizada en el archivo CSV2ARFF.py
"""


######################################################
#                      Parte 2
######################################################

# Algoritmo Apriori
# numRules 500, lowerBoundMinSupport 0.001
minMetrics = [0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95]
numRulesA   = [199, 161, 150, 143, 131, 130, 77, 58, 34, 28, 28]

plt.plot(minMetrics, numRulesA, 'ro:')
plt.ylabel("numRules found")
plt.xlabel("minMetrics")
plt.title("2. Algoritmo Apriori con soporte min {0.001}")
plt.show()

######################################################
#                      Parte 3
######################################################

# Algoritmo Apriori
# numRules 500, lowerBoundMinSupport 0.0013
numRulesB = [56, 49, 38 , 31, 19, 18, 14, 14, 8, 2, 2]

plt.plot(minMetrics, numRulesB, 'ro:')
plt.ylabel("numRules found")
plt.xlabel("minMetrics")
plt.title("3. Algoritmo Apriori con soporte min {0.0013}")
plt.show()

######################################################
#                      Parte 4
######################################################

# Algoritmo FP-growth
# numRules 1000

#soporte 0.0018
numRules18 = [6, 5, 5, 5, 4, 2, 0, 0, 0, 0, 0]
plt.plot(minMetrics, numRules18, 'r*:', label="Soporte 0.0018")
#soporte 0.0017
numRules17 = [8, 7, 7, 7, 6, 3, 1, 1, 1, 1, 1]
plt.plot(minMetrics, numRules17, 'b*:', label="Soporte 0.0017")
#soporte 0.0016
numRules16 = [12, 11, 11, 11, 6, 3, 1, 1, 1, 1, 1]
plt.plot(minMetrics, numRules16, 'g*:', label="Soporte 0.0016")
#soporte 0.0015
numRules15 = [21, 20, 20, 13, 7, 3, 3, 3, 3, 1, 1]
plt.plot(minMetrics, numRules15, 'c*:', label="Soporte 0.0015")
#soporte 0.0014
numRules14 = [33, 32, 32, 25, 13, 10, 8, 8, 8, 2, 2]
plt.plot(minMetrics, numRules14, 'm*:', label="Soporte 0.0014")
#soporte 0.0013
numRules13 = [50, 49, 38, 31, 19, 16, 14, 14, 8, 2, 2]
plt.plot(minMetrics, numRules13, 'y*:', label="Soporte 0.0013")
#soporte 0.0012
numRules12 = [102, 70, 59, 52, 40, 37, 35, 35, 11, 5, 5]
plt.plot(minMetrics, numRules12, 'k*:', label="Soporte 0.0012")
#soporte 0.0011
numRules11 = [128, 96, 85, 78, 66, 63, 61, 42, 18, 12, 12]
plt.plot(minMetrics, numRules11, 'r*:', label="Soporte 0.0011")
#soporte 0.0010
numRules10 = [193, 161, 150, 143, 131, 128, 77, 58, 34, 28, 28]
plt.plot(minMetrics, numRules10, 'b*:', label="Soporte 0.0010")

# Gráfico genérico
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4. Datos FP-growth")
plt.legend()
plt.show()


# GRÁFICOS INDIVIDUALES
plt.plot(minMetrics, numRules18, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.1 Datos FP-growth Soporte 0.0018")
plt.show()

plt.plot(minMetrics, numRules17, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.2 Datos FP-growth Soporte 0.0017")
plt.show()

plt.plot(minMetrics, numRules16, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.3 Datos FP-growth Soporte 0.0016")
plt.show()

plt.plot(minMetrics, numRules15, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.4 Datos FP-growth Soporte 0.0015")
plt.show()

plt.plot(minMetrics, numRules14, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.5 Datos FP-growth Soporte 0.0014")
plt.show()

plt.plot(minMetrics, numRules13, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.6 Datos FP-growth Soporte 0.0013")
plt.show()

plt.plot(minMetrics, numRules12, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.7 Datos FP-growth Soporte 0.0012")
plt.show()

plt.plot(minMetrics, numRules11, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.8 Datos FP-growth Soporte 0.0011")
plt.show()

plt.plot(minMetrics, numRules10, 'b*:')
plt.ylabel("numRules")
plt.xlabel("minMetrics")
plt.title("4.9 Datos FP-growth Soporte 0.0010")
plt.show()
