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
