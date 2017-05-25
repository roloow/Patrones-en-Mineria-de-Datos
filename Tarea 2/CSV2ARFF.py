# -*- coding: utf-8 -*-
"""
This program has the responsability to create or transform some DataSet as CSV
into a ARFF archive, which can be read by WEKA
"""
#--------------------------------------------
#            products
#--------------------------------------------
#   FUNCTION_IN_PARAMETERS_DEFINITION
#   FILE:  Opened Data Type File
#
#   FUNCTION_OUT_PARAMETERS_DEFINITION
#   out:    list of strings refering to the no
#           repeated names in the DataSet
#   FUNCTION_CODING
def products(FILE):
	my_set = set([])
	for line in FILE:
		line = line.strip().split(',')
		line_set = set(line)
		my_set |= line_set
	return list(my_set)
#   FUNCTION_EXPLANATION
#   As a brute force algorithm, it only reads
#	line by line adding the parameters to a set
#	with a union operation
#--------------------------------------------


#--------------------------------------------
#            matrix
#--------------------------------------------
#   FUNCTION_IN_PARAMETERS_DEFINITION
#   FILE:  Opened Data Type File
#
#   FUNCTION_OUT_PARAMETERS_DEFINITION
#   out:    tuple with a list of list and a list
#           of strings
#   FUNCTION_CODING
def matrix(FILE):
	matrix = []
	MSET = products(FILE)
	FILE.seek(0)
	for line in FILE:
		line = line.strip().split(',')
		vector = []
		for product in MSET:
			if product in line:
				vector.append('1')
			else:
				vector.append('0')
		matrix.append(vector)
	return (matrix, MSET)
#   FUNCTION_EXPLANATION
#	Firstly it takes the file and gets the
#	list of diferent products, then it creates
#	a matrix where 1 represents the product is
#	on current order, and 0 doesnt.
#--------------------------------------------

#--------------------------------------------
#            create_arff
#--------------------------------------------
#   FUNCTION_IN_PARAMETERS_DEFINITION
#   FILE:  Opened Data Type File
#   OUTNAME:  String value
#
#   FUNCTION_OUT_PARAMETERS_DEFINITION
#   out:    No return value
#   FUNCTION_CODING
def create_arff(FILE, OUTNAME):
	FILENAME = OUTNAME.lower() + '.arff'
	MATRIX, MSET = matrix(FILE)
	f = open(FILENAME, 'w')
	f.write('@RELATION ' + OUTNAME.lower() + '\n\n')
	for product in MSET:
		f.write("@ATTRIBUTE '" + product + "' NUMERIC\n")
	f.write('\n@DATA\n')
	for vector in MATRIX:
		f.write( ','.join(vector) + '\n')
	f.close()
#   FUNCTION_EXPLANATION
#	Creates an ARFF file with the attributes
#	that were obtained in previews functionalities
#--------------------------------------------



if __name__ ==  "__main__":
	# FILE = str(raw_input('Ingrese nombre del archivo: '))
	# if '.csv' not in FILE:
	# 	FILE += '.csv'

	f = open("groceries.csv")
	create_arff(f, 'groceries')
	f.close()
