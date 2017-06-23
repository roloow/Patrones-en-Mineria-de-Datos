# -*- coding: utf-8 -*-

#--------------------------------------------
#            Libraries
#--------------------------------------------
from pyspark import SparkContext, SparkConf


#--------------------------------------------
#            spark_init
#--------------------------------------------
#   FUNCTION_IN_PARAMETERS_DEFINITION
#   name:  String name for environ [not required]
#
#   FUNCTION_OUT_PARAMETERS_DEFINITION
#   out:    SparkContext object
#   FUNCTION_CODING
def spark_init(name='Default Name'):
	conf = SparkConf().setAppName(name)
	sc = SparkContext(conf=conf)
    return sc
#   FUNCTION_EXPLANATION
#   Creates a new JVM, if non is already created,
#	and return the context object to work with
#	spark utilities
#--------------------------------------------

#--------------------------------------------
#            read_datasets
#--------------------------------------------
#   FUNCTION_IN_PARAMETERS_DEFINITION
#   mode:   one letter string which makes read
#			of the ratings.dat file or the training
#			and tests ones.[Not required]
#
#   FUNCTION_OUT_PARAMETERS_DEFINITION
#   out:    Tuple of lists of tuples
#   FUNCTION_CODING
def read_datasets(mode=None):
	try:
		file_movies = open("DataSets/movies.dat", "r")
		file_tags = open("DataSets/tags.dat", "r")
	except:
		print "ERROR: Not all Files were found."
		return -1

	movies = list()
    for line in file_movies:
		aux = list()
		line = line.strip().split('::')
		aux.append(line[0]).append(line[1]).append(line[2].split('|'))
		movies.append(tuple(aux))
	file_movies.close()

	tags = list()
    for line in file_tags:
		line = line.strip().split('::')
		tags.append(tuple(line))
	file_tags.close()

	if not mode:
		try:
			file_ratings = open("DataSets/ratings.dat", "r")
		except:
			print "ERROR: Not all Files were found."
			return -1
		ratings = list()
	    for line in file_ratings:
			line = line.strip().split('::')
			ratings.append(tuple(line))
		file_ratings.close()
	return (movies, tags, ratings)
#   FUNCTION_EXPLANATION
#   Creates a new JVM, if non is already created,
#	and return the context object to work with
#	spark utilities
#--------------------------------------------
