# Patrones en Mineria de Datos

Para realizar las tareas utilizaremos el lenguaje Python dadas las librerias correspondientes que existen para el manejor de patrones. Como prerrequisito para el correcto funcionamiento de estas tareas es la instalación de la version **2.7** de Python. [Página oficial](https://www.python.org/downloads/)

Se recomienda instalar el gestor de paquetes de python conocido como **`pip`**

Integrantes
-----------

| Nombre   | Rol   |
| :------- | :---- |
| Felipe Avaria | 2923547-3 |
| Rolando Casanueva  | 201204505-3 |


## Tarea 1

Para la primera tarea se requiere realizar los siguientes pasos previos a la ejecución, se recomienda el uso de virtualenv para evitar la instalación basura.

    pip install virtualenv

Una vez instalado se deberá ingresar correr el ambiente de desarrollo, *la siguiente ejecución debe realizarse donde se quiera generar el ambiente de entorno*
```
  > ../virtualenv .
  > ../.\Scripts\activate
  (AMBIENTE) >
```

* **Instalacion de paquetes**

```
    pip install numpy
    pip install scipy
    pip install matplotlib
    pip install sklearn
    pip install pandas
```

* **Documentación de Clusters**

Podemos encontrar todos los clusters que utilizaremos en [esta](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.cluster) página o bien, puede ir directamente a las documentaciones individuales.

|Cluster | Documentación |
|:---|:---|
|K-Means| [Ir a la documentación](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans)|
|Mini Batch K-Means| [Ir a la documentación](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html)|
|DBScan |[Ir a la documentación](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN)|
|HAC Completo (*AgglomerativeClustering - linkage: Complete*) |[Ir a la documentación](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering)|
|Ward (*AgglomerativeClustering - linkage: Ward*) |[Ir a la documentación](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering)|

## Tarea 2

Basado en los mismos principios de la tarea 1, utilizaremos un DataSet "groceries" el cual se encuentra en la carpeta como una extensión (.csv) para poder realizar su análisis se utiliza un [Weka](http://www.cs.waikato.ac.nz/ml/weka/), sin embargo esta aplicación lee archivos (.arff) para ello creamos un conversor de csv a arff.

## Tarea 3

Para esta tarea debemos utilizar la herramienta [Spark](https://spark.apache.org/), que nos permitirá utilizar una librería de *Machine Learning*. Para su instalación adecuada y notando que utilizaremos la versión compatible con **Python** sigase los siguientes pasos:

### Instalación Spark

#### Windows

- Primero descargaremos una versión de Apache Spark pre-construida, que en nuestro caso fue [Spark 2.1.1](https://spark.apache.org/) con tipo `pre-build for Apache Hadoop 2.7 and later`.
- Una vez descargado, proceder a descomprimirlo en la carpeta que desea mantener para *Spark*.
- Si bien, el archivo descargado viene con leves acercamientos de lo que es Hadoop, seguirá faltando un archivo `winutils.exe`, el cual puede encontrarse en su [GitHub](https://github.com/steveloughran/winutils) para la versión correspondiente, basta copiar el archivo `winutils.exe` en la carpeta `PATH\Spark\bin`
- Ahora a través de linea de comandos, ir hasta la carpeta *python* y correr el *setup* hacia la carpeta *sdist*, lo que generará un archivo *.tgz* para ser instalado mediante `pip`
        c:\PATH\Spark> cd Python
        c:\PATH\Spark\Python> python setup.py sdist
        c:\PATH\Spark\Python> cd dist
        c:\PATH\Spark\Python\dist> pip install package_name.tgz
- Ahora es momento de finalizar la instalación agregando la `SPARK_HOME` a las variables de entorno del sistema y agregar el `PATH` también. Para evitar problemas esto puede hacerse manualmete desde `propiedades del sistema> configuración avanzada> variables de entorno`
        SPARK_HOME = c:\PATH\Spark
        PATH = c:\PATH\Spark\bien
**NOTAR:** *Si la ruta (nombres de las carpetas) poseen espacios, utilizar la abreviación de las mismas para evitar que se produzca un error. Para saber cual es la abreviación de una carpeta basta colocarse en una carpeta superior y correr `DIR /X`*

### DataSet

#### Descarga

El dataset puede ser descargado en [este link](https://grouplens.org/datasets/movielens/10m/) y dado que utilizaremos un método de *Machine Learning*, es conveniente dividir el archivo `rating`, para esto deberemos correr
```
c:\PATH\TO\DATASET\ bash split_ratings.sh
```

#### Estructura

- RATINGS

`UserID::MovieID::Rating::Timestamp`

- TAGS

`UserID::MovieID::Tag::Timestamp`

- MOVIES

`MovieID::Title::Genres`
