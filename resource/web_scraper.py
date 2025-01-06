import os
import re
import requests
import csv
from bs4 import BeautifulSoup

wiki_base_url = 'https://es.wikipedia.org/'

# Envía una solicitud a una URL de Wikipedia (wiki_base_url + queryURL) y extrae información de las tablas precedidas por los encabeados décadas.
def queryInfo(oscar, headersValues, elementList):
    response = requests.post(wiki_base_url + oscar, headers=headersValues)
    soup = BeautifulSoup(response.text, "html.parser")
    
    decadas = [
        '1956-1959', '1960-1969', '1970-1979',
        '1980-1989', '1990-1999', '2000-2009',
        '2010-2019', '2020-2029'
    ]
    
    for decada in decadas:
        encabezado = soup.find('h5', {'id': decada}) or soup.find('span', {'id': decada}) # h5 en vez de h3
        
        if encabezado:
            tabla = encabezado.find_next('table')
            if tabla:
                # Extraer el cuerpo de la tabla
                filas = tabla.find('tbody')
                listaPeliculas = filas.find_all('tr') if filas else []
                # Se establece un contador para poder definir cuales peiculas han ganado el Oscar
                contador_filas = 0
                año_actual = None

                for pelicula in listaPeliculas:
                    celdas = pelicula.find_all('td')
                    if celdas:
                        # Cada vez que se encuentre rowspan, se extraerá el año. 
                        if celdas[0].get('rowspan'):
                            año_actual = celdas[0].text.strip()
                        # Debido a la estructura HTML del sitio, debemos de buscar los td sin rowspan, ya que este hace referencia al año
                        if celdas[0].get('rowspan'):
                            enlace = celdas[1].find('a')
                        else:
                            enlace = celdas[0].find('a')
                        ganador = 1 if contador_filas % 5 == 0 else 0
                    
                        if enlace:
                            buscar_no_redactados = enlace.get('title')
                            contador_filas += 1
                            if '(aún no redactado)' not in buscar_no_redactados:
                                queryMovie(enlace.get('href'), enlace.get('title'), headersValues, elementList, año_actual, ganador) 
                                # Añadimos ganador como nueva variable
                    

# Extrae información de cada película desde su página en Wikipedia
def queryMovie(queryURL,titulo,headersValues,elementList, año_actual, ganador):
    response= requests.post(wiki_base_url+queryURL, headers=headersValues)
    soup = BeautifulSoup(response.text,"html.parser")
    # Encuentra la tabla Infobox, de donde sacaremos nuestra información
    tablaInfo = soup.find("table", {"class": "infobox plainlist plainlinks"})
    
    # Obseramos que hay enlaces a pleículas sin infobox
    if tablaInfo:
        # Información del director
        director = get_value_from_table(tablaInfo, "Director de cine")
        pais = get_value_from_table(tablaInfo, "País")
        genero = get_value_from_table(tablaInfo, "Género cinematográfico")
        duracion = get_value_from_table(tablaInfo, "Duración")
        
        # Más información
        protagonistas = get_value_from_table(tablaInfo, "Protagonistas")
        idioma = get_value_from_table(tablaInfo, "Idioma")
        produccion = get_value_from_table(tablaInfo, "Producción")
        guion = get_value_from_table(tablaInfo, "Guion")
        musica = get_value_from_table(tablaInfo, "Música")
        fotografia = get_value_from_table(tablaInfo, "Fotografía")
        vestuario = get_value_from_table(tablaInfo, "Vestuario")
        productora = get_value_from_table(tablaInfo, "Productora")
        presupuesto = get_value_from_table(tablaInfo, "Presupuesto")
        recaudacion = get_value_from_table(tablaInfo, "Recaudación")
        
        # Si el nombre del país no está directamente disponible, lo busca en el icono de bandera
        if not pais:
            pais_tag = tablaInfo.find('span', class_='flagicon')
            if pais_tag:
                pais_link = pais_tag.find_next('a', title=True)
                if pais_link and pais_link.get('title'):
                    pais = pais_link['title']
        
        if pais:
            pais = re.sub(r'Bandera de |Bandera del ', '', pais)

        # Lista con los valores asociados a cada película (se agrega a elementlist)
        pelicula = []
        pelicula.append(titulo)
        pelicula.append(director)
        pelicula.append(pais)
        pelicula.append(año_actual)
        pelicula.append(genero)
        pelicula.append(duracion)
        pelicula.append(protagonistas)
        pelicula.append(idioma)
        pelicula.append(produccion)
        pelicula.append(guion)
        pelicula.append(musica)
        pelicula.append(fotografia)
        pelicula.append(vestuario)
        pelicula.append(productora)
        pelicula.append(presupuesto)
        pelicula.append(recaudacion)
        pelicula.append(ganador)
        elementList.append(pelicula)  

    else:
        pais = ""

    
    

# Busca y extrae valores específicos del infobox de la película.
def get_value_from_table(tablaInfo, titulo):
    if tablaInfo:
        main_enlace = tablaInfo.find("a", {'title': titulo})
        valor = ""
        
        if main_enlace:
            content = main_enlace.parent.findNextSibling()
            enlace = content.find("a") if content else None
            if enlace:
                valor = enlace.text
            else:
                valor = content.text if content else ""
        else:
            row = tablaInfo.find("th", string=titulo)
            if row:
                # Debido a fallos en el código, debemos asegurarnos de que el siguiente hermano exista antes de acceder a él
                siguiente_hermano = row.findNextSibling()
                if siguiente_hermano:
                    valor = siguiente_hermano.text.strip()
        
        # Limpiar y devolver el valor
        return valor.strip().replace('\n', '')
    else:
        return ""

# Define la ubicación para guardar el archivo de salida .csv
currentDir = os.getcwd()
filename = "peliculas.csv"
filePath = os.path.join(currentDir, filename)
# Son los encabezados HTTP para las solicitudes
oscar="/wiki/Anexo:Ganadores_y_nominados_del_Óscar_a_la_mejor_película_internacional"
headerValues={}
#Set the header values of HTTP Request
headerValues['Origin']='https://es.wikipedia.org'
headerValues['Referer']='https://es.wikipedia.org/wiki/Anexo:Ganadores_y_nominados_del_Óscar_a_la_mejor_película_internacional'
headerValues['Content-Type']='text/html; charset=UTF-8'
#Set the POST values of HTTP Request

# Lista para la creación de la consiguiente tabla
moviesInfo=[]
moviesInfo.append(["Titulo", "Director", "Pais", "Año", "Genero", "Duración (Minutos)",
    "Protagonistas", "Idioma", "Producción", "Guion", "Música",
    "Fotografía", "Vestuario", "Productora", "Presupuesto (Dólares)", "Recaudación (Dólares)", "Ganador"])
queryInfo(oscar,headerValues,moviesInfo)

# Limpia de parántesis y corchetes y lo que hubiera dentro de ellos
def limpiar(texto):
    texto = re.sub(r'\s*\(.*?\)', '', texto)
    texto = re.sub(r'\[.*?\]', '', texto)
    return texto.strip()  

# Aisla los números del string y convierte la variable en int
def limpiar_duracion(duracion):
    match = re.search(r'(\d+)', str(duracion)) 
    if match:
        return int(match.group(1))
    return None

# Busca la congruencia entre una letra minuscula y otra mayuscula, añade entre los dos una coma y un espacio
def anadir_coma(añadircoma):
    añadircoma = re.sub(r'(?<=[a-z])(?=[A-Z])', ', ', añadircoma)
    return añadircoma

# Aisla el número mayor de los resultantes (prioridad si está en millones) y pasandolo de millones a dolares si fuera necesario. 
def limpiar_millones(monto):
    if pd.isnull(monto):
        return None  
    monto = str(monto).lower().replace('&#160;', '').replace('&nbsp;', '').replace('\xa0', '').replace(' ', '').replace(',', '').replace('.', '') 
    if 'millones' in monto or 'm' in monto:
        patron_millon = re.findall(r'(\d+)', monto) 
        valores_millones = [int(m) for m in patron_millon]
        if valores_millones:
            max_valor = max(valores_millones) * 1_000_000
            return f"{max_valor:,}".replace(',', '.') 
        return None
    else:
        patron_mil = re.findall(r'(\d+)', monto)
        if patron_mil:
            valores = [int(m) for m in patron_mil]
            max_valor = max(valores)
            return f"{max_valor:,}".replace(',', '.')
        return None

for pelicula in moviesInfo[1:]:
    for i in range(len(pelicula)):
        if i !=16:  
            pelicula[i] = limpiar(pelicula[i])

for pelicula in moviesInfo[1:]:
    pelicula[5] = limpiar_duracion(pelicula[5])
    pelicula[2] = anadir_coma(pelicula[2])
    pelicula[6] = anadir_coma(pelicula[6])
    pelicula[14] = limpiar_millones(pelicula[14])
    pelicula[15] = limpiar_millones(pelicula[15])
    for i in range(8, 14):  
        pelicula[i] = anadir_coma(pelicula[i])

# Escribe moviesInfo en un archivo .csv llamado peliculas.csv
with open("/content/drive/MyDrive/oscars.csv", 'w', newline='', encoding='utf-8') as csvFile:
  writer = csv.writer(csvFile)
  for info in moviesInfo:
    writer.writerow(info)
