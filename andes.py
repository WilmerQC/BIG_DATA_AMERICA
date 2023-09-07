import requests
from bs4 import BeautifulSoup
from collections import deque

#en esta lista crearemos un registro de los enlaces para evitar duplicidad en la exploración
enlaces_explorados = set()

def buscar_palabra(palabra,url):
    response = requests.get(url)

    if response.status_code == 200:
        #parseamos el contenido del enlace
        soup=BeautifulSoup(response.text,'html.parser')

        #ubicamos el div deseado
        div_contenido = soup.find('div',class_='content-inner')
        
        #if el div existe y la palabra se encuentra en dicho div
        if div_contenido and palabra in div_contenido.text:
            print(palabra, " encontrada en la url: ", url)
        else:
            print("Div no encontrado o palabra no encontrada en la url: ",url)
    else:
              print("Error al acceder a la url ", url)

#función para explorar la url por niveles en sus enlaces
def explorar_enlaces(url_inicial,nivel_maximo):
    cola = deque([(url_inicial,0)])#inicializamos una cola con la url de inicio y con nivel 0
    
    while cola:
        url_actual, nivel_actual = cola.popleft()
        enlaces_explorados.add(url_actual)

        if nivel_actual<=nivel_maximo:
            response = requests.get(url_actual)

            if response.status_code == 200:
              soup=BeautifulSoup(response.text,'html.parser')

              #obtenemos todos los enlaces
              enlaces =soup.find_all('a',href=True)

              for cada_enlace in enlaces:
                  enlace_url = cada_enlace['href']

                  if enlace_url.startswith('http') and enlace_url not in enlaces_explorados:
                      cola.append((enlace_url,nivel_actual+1))
                      enlaces_explorados.add(enlace_url)
                      
                      buscar_palabra("UPeU",enlace_url)

#invocamos a la función
explorar_enlaces("https://www.losandes.com.pe/",4)