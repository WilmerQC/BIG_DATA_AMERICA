import requests
from bs4 import BeautifulSoup
from collections import deque
import mysql.connector

# En esta lista crearemos un registro de los enlaces para evitar duplicidad
enlaces_explorados = set()

# Conéctate a la base de datos
def conectar_base_de_datos():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            # Crear base de datos en PHPMyAdmin
            database='news'
        )
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

# Inserta un resultado en la base de datos
def insertar_resultado(url, titulo, descripcion, fecha, conn):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tabla_de_resultados (url, titulo, descripcion, fecha) VALUES (%s, %s, %s, %s)",
                       (url, titulo, descripcion, fecha))
        conn.commit()
        cursor.close()
    except Exception as e:
        print("Error al insertar en la base de datos:", e)

def buscar_noticias(url, conn):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        noticias = soup.find_all('div', class_='cada-noticia')  # Cambiar la clase según la estructura de la página

        for noticia in noticias:
            titulo = noticia.find('h2').text.strip()
            descripcion = noticia.find('p').text.strip()
            fecha = noticia.find('span', class_='fecha').text.strip()
            url_noticia = noticia.find('a')['href']

            # Insertar el resultado en la base de datos
            insertar_resultado(url_noticia, titulo, descripcion, fecha, conn)

def explorar_enlaces(url_inicial, nivel_maximo, conn):
    cola = deque([(url_inicial, 0)])

    while cola:
        url_actual, nivel_actual = cola.popleft()
        enlaces_explorados.add(url_actual)

        if nivel_actual <= nivel_maximo:
            response = requests.get(url_actual)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                enlaces = soup.find_all('a', href=True)

                for cada_enlace in enlaces:
                    enlace_url = cada_enlace['href']

                    if enlace_url.startswith('http') and enlace_url not in enlaces_explorados:
                        cola.append((enlace_url, nivel_actual + 1))
                        enlaces_explorados.add(enlace_url)
                        buscar_noticias(enlace_url, conn)

# Cambia los valores con tu configuración
conn = conectar_base_de_datos()
if conn is not None:
    explorar_enlaces("https://www.losandes.com.pe", 10, conn)
    conn.close()
else:
    print("No se pudo conectar a la base de datos.")
