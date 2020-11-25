# transferLearning
Código para usar redes neuronales con transfer learning con el objetivo de clasificar imágenes tomadas desde satélite.


Grupo en la competición de kaggle: MangasVerdes
Compuesto por:
	Christian Martínez Abad
	Andrés Montoro Montarroso
	María Elena Pedrajas Perabá

En este fichero se incluyen las indicaciones para usar el modelo creado.

Para ejecutar el código se ha usado la plataforma de Kaggle: https://www.kaggle.com/elenapedrajas/kernel3d4afa0a21
En dicha explicación de kaggle se encuentran la carpeta con los datos y el modelo.
Los archivos incluidos se pueden cargar añadiendo en esta plataforma a input la carpeta usos-del-suelo-desde-el-espacio que contiene las imágenes.

En primer lugar, ModeloFinalKaggle.ipynb contiene la lectura del modelo generado, que se puede probar directamente pasándole el conjunto de test.
Como el modeloXception-96-v2.h5 preconfigurado, con el que se puede cargar dicho modelo, pesa más de 25 MB, no se ha incluido.

El fichero GenerarModelo.ipynb contiene el código necesario para generar el modelo, el fichero modeloXception-96-v2.h5 y el csv entregable en kaggle.

El fichero comprobarAccuracy.py permite comprobar el Accuracy obtenido sobre validación, ya que al realizarse con una competición Kaggle los archivos de test no son supervisados. Se comprueba que el output.csv de las imágenes de validación acierta un 95,91% las imágenes de validacion.csv.
En cuanto a la competición, se obtuvo un accuracy de 0,96482 en el conjunto público y 0,95698 en el privado.

