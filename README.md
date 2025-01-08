# OSCARS A LA MEJOR PELÍCULA - Practica 2 del curso Tipología y ciclo de vida de los datos

Este repositorio contiene un script en Python almacenado en la carpeta /resource que extrae información mediante web_scraping sobre películas ganadoras del Óscar (1927/28 - 2023) desde Wikipedia, unido con otras películas nominadas, pero no ganadoras del Oscar, y la guarda en un archivo CSV ubicado en la carpeta /dataset. La información extraída refiere variables como el título, director, país, año, género, duración (minutos), entre otros. La carpeta /resource también
cuenta con un archivo de python con la aplicación de la limpieza de datos y las diferentes
transformaciones necesarias para que el dataset tuviera un formato adecuado para los otros
archivos de python donde se ejecutaron los modelos supervisados, no supervisados y las pruebas de hipótesis

## Integrantes

- **Javier Martínes Rodríguez**
- **Joshua David Triana**

## Archivos del repositorio

- **README.md**: Donde se definen los nombres de los integrantes del grupo, se listan los archivos que componen el repositorio, se describe el uso del script.py y el DOI de Zenodo para el dataset generado.
- **requirements.txt**: Lista las dependencias necesarias para ejecutar el código.
- **/resource**: Carpeta que contiene el código Python para el web_scraping de Wikipedia, otro para limpieza y analisis de hipotesis y finalmente con las ejecuciones de los modelos supervisados y no supervisados. El script principal se encuentra en este directorio.
  - **web_scrapper.py**: El código Python que realiza el web_scraping mediante solicitudes HTTP a las páginas de Wikipedia para extraer la información necesaria que dará forma al CSV resultante.
  - **limpieza_de_datos.py**: El código Python que realiza la limpieza de datos necesarios para la ejecución de los modelos
  - **Mann-Whitney_U.py**: El código Python que realiza las pruebas de contraste de hipótesis
  - **modelo_supervisado.py**: El código Python que realiza las ejecuciones de los modelos supervisados seleccionados
  - **modelo_no_supervisado.py**: El código Python que realiza las ejecuciones de los modelos no supervisados seleccionados
- **/dataset**: Carpeta que contiene el dataset generado en formato CSV.
  - **peliculas.csv**: Dataset con la información de las películas ganadoras del Óscar, como el director, país, año, género, duración, presupuesto, recaudación, etc.
  - **peliculas_clean.csv**: Dataset con la información de las películas ganadoras y nominadas al Óscar, luego de la aplicación del proceso de limpieza

## Uso del código

### Requisitos

Para ejecutar el script, es necesario primero tener instaladas varias librerías de Python. Ejecutando el siguiente código puedes instalarlas:

```bash
pip install -r requirements.txt
```

### Correr el código

mediante este script puedes correr el código del repositorio:

```bash
python source/web_scrapper.py
```

### Parámetros del script

El script admite los siguientes parámetros:

Una url_base: en este caso, la URL base de Wikipedia. Este parámetro define la dirección principal de Wikipedia que el código usa para acceder a las páginas específicas, en un primer momento determinada https://es.wikipedia.org/wiki/Anexo:Óscar_a_la_mejor_película, pero más adelante, para el webscraping, definidas por otros hipervinculos. Por defecto, el valor es https://es.wikipedia.org/.
EL archivo de salida: el archivo de salida que por defecto tiene el nobre de "peliculas.csv" y se guarda en la carpeta /dataset.
Los encabezados de la solicitud HTTP para la estracción.

### Correcciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

### Licencia

Este proyecto está bajo la Licencia unlicense. Consulta el archivo [LICENSE]para más detalles.
