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
