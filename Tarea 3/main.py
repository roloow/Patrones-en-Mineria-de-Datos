# -*- coding: utf-8 -*-

#--------------------------------------------
#            Libraries
#--------------------------------------------
from pyspark import SparkContext, SparkConf
from pyspark.mllib.recommendation import ALS, Rating
from math import sqrt


#--------------------------------------------
#            spark_init
#--------------------------------------------
#   FUNCTION_IN_PARAMETERS_DEFINITION
#	None
#
#   FUNCTION_OUT_PARAMETERS_DEFINITION
#   out:    SparkContext object
#   FUNCTION_CODING
def spark_init():
	sc = SparkContext()
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
#	sc:		spark context object
#
#   FUNCTION_OUT_PARAMETERS_DEFINITION
#   out:    Tuple of lists of tuples
#   FUNCTION_CODING
def read_datasets(sc, mode=None):
	try:
		file_movies = sc.textFile("DataSets/movies.dat")
		file_tags = sc.textFile("DataSets/tags.dat")
	except:
		print "ERROR: Not all Files were found."
		return -1
	movies = file_movies.map(lambda line: line.split("::"))
	tags = file_movies.map(lambda line: line.split("::"))
	return (movies, tags)
#   FUNCTION_EXPLANATION
#   Open Datasets and returns them into python variables
#--------------------------------------------

def read_file(filename):
	file_ = open(filename)
	data = list()
	for line in file_:
		line = line.strip().split("::")
		data.append((int(line[0]), int(line[1]), float(line[2])))
	return data

def read_ratings(sc):
	train1 = sc.parallelize(read_file("DataSets/SplitData/r1.train"))
	train2 = sc.parallelize(read_file("DataSets/SplitData/r2.train"))
	train3 = sc.parallelize(read_file("DataSets/SplitData/r3.train"))
	train4 = sc.parallelize(read_file("DataSets/SplitData/r4.train"))
	train5 = sc.parallelize(read_file("DataSets/SplitData/r5.train"))
	test1 = sc.parallelize(read_file("DataSets/SplitData/r1.test"))
	test2 = sc.parallelize(read_file("DataSets/SplitData/r2.test"))
	test3 = sc.parallelize(read_file("DataSets/SplitData/r3.test"))
	test4 = sc.parallelize(read_file("DataSets/SplitData/r4.test"))
	test5 = sc.parallelize(read_file("DataSets/SplitData/r5.test"))
	train = (train1, train2, train3, train4, train5)
	test = (test1, test2, test3, test4, test5)
	ratings = (train, test)
	return ratings


def system_train(ratings, rank, lambda_=0.01):
#	ratings:	RDD of Rating or (userID, productID, rating) tuple.
#	rank:		Rank of the feature matrices computed (number of features).
#	lambda:		Regularization parameter. (default: 0.01)
	model = ALS.train(ratings, rank=rank, lambda_=lambda_, seed=0)
	return model

def re_train(model, data, rank, lambda_=0.01):
	model.train(data, rank=rank, lambda_=lambda_, seed=0)
	return model

if __name__ ==  "__main__":
	sc = spark_init()
	movies, tags = read_datasets(sc)
	ratings = read_ratings(sc)
	train, test = ratings
	tr1, tr2, tr3, tr4, tr5 = train
	ts1, ts2, ts3, ts4, ts5 = test

	ranks = [1, 5, 10, 50, 100]
	lambdas = [0.01, 0.02]

	for rank in ranks:
		for lambda_ in lambdas:
			model = system_train(tr1, rank, lambda_)
			model = re_train(model, tr2, rank, lambda_)
			model = re_train(model, tr3, rank, lambda_)
			model = re_train(model, tr4, rank, lambda_)
			model = re_train(model, tr5, rank, lambda_)
			predict = model.predictAll(ts1.map(lambda gp: (gp[0], gp[1]))).map(lambda res: (res[2]))
			validation = ts1.map(lambda real: (real[2]))
			union = validation.join(predict)
			RMSE = sqrt(union.map(lambda row: (row[0] - row[1])**2).mean())

			results = open("Results/results.dat", "a")
			results.write('rank:'+str(rank)+' lambda:'+str(lambda_)+' RMSE:'+str(RMSE))
