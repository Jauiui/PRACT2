# CARACTERÍSTICAS PARA GANAR UN OSCAR A LA MEJOR PELÍCULA INTERNACIONAL - Practica 2 del curso Tipología y ciclo de vida de los datos

Este repositorio contiene varios scripts en Python en la carpeta /resource que extrae información mediante web_scraping sobre películas ganadoras del Óscar a la mejor película Internacional (1956 - 2023) desde Wikipedia, limpia este dataset y realiza diferentes modelos y pruebas estadísticas para su análisis (modelos supervisados, no supervisados y las pruebas de contraste de hpótesis) en el intento de entender que hace que una película nominada a los Oscars sea la premiada. Los resultados se comentan en el PDF también entregado en la práctica y los archivos .CSV se encuentran ubicados en la carpeta /dataset. 

## Integrantes

- **Javier Martínes Rodríguez**
- **Joshua David Triana**

## Archivos del repositorio

- **README.md**: Donde se definen los nombres de los integrantes del grupo, se listan los archivos que componen el repositorio y se describe el uso del los script.py.
- **requirements.txt**: Lista las dependencias necesarias para ejecutar el código.
- **/resource**: Carpeta que contiene el código Python para el web_scraping de Wikipedia y creación del dataset, su limpieza y su analisis de posterior con la ejecución de los modelos supervisados, no supervisados y de contraste de hipótesis. El script principal se encuentra en este directorio.
  - **web_scrapper.py**: El código Python que realiza el web_scraping mediante solicitudes HTTP a las páginas de Wikipedia para extraer la información necesaria que dará forma al CSV resultante.
  - **limpieza_de_datos.py**: El código Python que realiza la limpieza de datos necesarios para la ejecución de los modelos.
  - **Mann-Whitney_U.py**: El código Python que realiza las pruebas de contraste de hipótesis (en este caso Mann-Whitney U).
  - **modelo_supervisado.py**: El código Python que realiza las ejecuciones de los modelos supervisados seleccionados.
  - **modelo_no_supervisado.py**: El código Python que realiza las ejecuciones de los modelos no supervisados seleccionados.
- **/dataset**: Carpeta que contiene los datasets generado en formato CSV.
  - **peliculas.csv**: Dataset con la información de las películas nominadas y ganadoras del Óscar a la mejor película Internacional, como el director, país, año, género, duración, presupuesto, recaudación, etc. En este dataset ya se han aplicad ciertas formas de limpieza. 
  - **peliculas_clean.csv**: Dataset con la información de las películas ganadoras y nominadas al Óscar a la mejor película Internacional, luego de la aplicación del proceso de limpieza.

## Uso del código

### Requisitos

Para ejecutar el script, es necesario primero tener instaladas varias librerías de Python. Ejecutando el siguiente código puedes instalarlas:

```bash
pip install -r requirements.txt
```

### Correr el código

mediante el siguiente script puedes correr el código del repositorio para cada una de las actividades que se quieran realizar:

```bash
python source/web_scrapper.py
python source/limpieza_de_datos.py
python source/Mann-Whitney_U.py
python source/modelo_supervisado.py
python source/modelo_no_supervisado.py
```

### Parámetros del script

Los scripts admites los siguientes parámetros:

Para web_scrapper.py: Por una parte, una url_base, en este caso, la URL base de Wikipedia. Este parámetro define la dirección principal de Wikipedia que el código usa para acceder a las páginas específicas, en un primer momento determinada https://es.wikipedia.org/wiki/Anexo:Ganadores_y_nominados_del_Óscar_a_la_mejor_película_internacional, pero más adelante, para el webscraping, definidas por otros hipervinculos. Por defecto, el valor es https://es.wikipedia.org/. Por otra parte, el archivo de salida: el archivo de salida que por defecto tiene el nombre de "peliculas.csv" y se guarda en la carpeta /dataset. Los encabezados de la solicitud HTTP para la estracción.
Para limpieza_de_datos.py: Por una parte, la ruta de entrada y por otra la ruta de salida, así como las opciones de limpieza determinadas. 
Para Mann-Whitney_U.py: Solo es la ruta de entrada, mediante la cual obtenemos tanto la columna utilizada para la comparación como la variable objetivo que secciona la muestra. 
Para modelo_supervisado.py: La ruta de entrada y los modelos utilizados, así como los propios parámetros que se utilizan en los modelos seleccionados.  
Para modelo_no_supervisado.py: La ruta de entrada y los modelos utilizados, así como los propios parámetros que se utilizan en los modelos seleccionados.  

### Correcciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

### Licencia

Este proyecto está bajo la Licencia unlicense. Consulta el archivo [LICENSE] para más detalles.
