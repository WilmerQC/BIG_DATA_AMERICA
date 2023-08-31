import pandas as pd
import matplotlib.pyplot as plt
archivo_1 = pd.read_csv('archivo_1.csv')

# Mostrar un resumen de estadísticas descriptivas
#resumen = archivo_1.describe()
#print(resumen)
# Cargar el archivo CSV en un DataFrame
archivo_1 = pd.read_csv('archivo_1.csv')

# Calcular el promedio de los ingresos
#promedio_ingresos = archivo_1['ingresos'].mean()
#print("El promedio de ingresos es:", promedio_ingresos)

# Calcular el promedio de las edades
#promedio_edad = archivo_1['edad'].mean()
#print("El promedio de edad es:", promedio_edad)

# Filtrar los datos para mostrar solo las personas que viven en Trujillo
#personas_en_trujillo = archivo_1[archivo_1['ciudad'] == 'Trujillo']
#print("Personas que viven en Trujillo:")
#print(personas_en_trujillo)


# Contar trabajadores por ciudad
#trabajadores_por_ciudad = archivo_1['ciudad'].value_counts()
#print("Cantidad de trabajadores por ciudad:")
#print(trabajadores_por_ciudad)

# Calcular el promedio de ingresos para cada ciudad
#promedios_por_ciudad = archivo_1.groupby('ciudad')['ingresos'].mean()
#print("Promedio de ingresos por ciudad:")
#print(promedios_por_ciudad)

# Encontrar la persona más joven
#indice_persona_mas_joven = archivo_1['edad'].idxmin()
#persona_mas_joven = archivo_1.loc[indice_persona_mas_joven]

# Encontrar la persona más mayor
#indice_persona_mas_mayor = archivo_1['edad'].idxmax()
#persona_mas_mayor = archivo_1.loc[indice_persona_mas_mayor]

#print("Persona más joven:")
#print(persona_mas_joven)

#print("\nPersona más mayor:")
#print(persona_mas_mayor)

# Encontrar la persona más joven
#indice_persona_mas_joven = archivo_1['edad'].idxmin()
#persona_mas_joven = archivo_1.loc[indice_persona_mas_joven]

# Encontrar la persona más mayor
#indice_persona_mas_mayor = archivo_1['edad'].idxmax()
#persona_mas_mayor = archivo_1.loc[indice_persona_mas_mayor]

# Encontrar la persona que gana menos
#indice_persona_gana_menos = archivo_1['ingresos'].idxmin()
#persona_gana_menos = archivo_1.loc[indice_persona_gana_menos]

# Encontrar la persona que gana más
#indice_persona_gana_mas = archivo_1['ingresos'].idxmax()
#persona_gana_mas = archivo_1.loc[indice_persona_gana_mas]
#print("Persona más joven:")
#print(persona_mas_joven)
#print("\nPersona más mayor:")
#print(persona_mas_mayor)
#print("\nPersona que gana menos:")
#print(persona_gana_menos)
#print("\nPersona que gana más:")
#print(persona_gana_mas)

# Contar personas por ciudad
#personas_por_ciudad = archivo_1['ciudad'].value_counts()
#print("Cantidad de personas por ciudad:")
#print(personas_por_ciudad)


# Ordenar la lista de personas por edad de la más joven a la más mayor
#personas_ordenadas_por_edad = archivo_1.sort_values(by='edad')
#print("Lista de personas ordenadas por edad:")
#print(personas_ordenadas_por_edad)

# Filtrar personas mayores de 30 años
#personas_mayores_de_30 = archivo_1[archivo_1['edad'] > 30]

# Calcular el promedio de sus edades
#promedio_edades_mayores_de_30 = personas_mayores_de_30['edad'].mean()
#print("Promedio de edades de personas mayores de 30 años:", promedio_edades_mayores_de_30)

# Calcular el total de ingresos para cada ciudad
#total_ingresos_por_ciudad = archivo_1.groupby('ciudad')['ingresos'].sum()
#print("Total de ingresos por ciudad:")
#print(total_ingresos_por_ciudad)

# Filtrar personas menores de 30 años
#personas_menores_de_30 = archivo_1[archivo_1['edad'] < 30]

# Calcular el promedio de ingresos para personas menores de 30 años
#promedio_ingresos_menores_de_30 = personas_menores_de_30['ingresos'].mean()
#print("Promedio de ingresos para personas menores de 30 años:", promedio_ingresos_menores_de_30)

# 1. Promedio de edades por ciudad
promedio_edades_por_ciudad = archivo_1.groupby('ciudad')['edad'].mean()
print("1. Promedio de edades por ciudad:")
print(promedio_edades_por_ciudad)
print("="*40)

# 2. Ciudades con ingresos promedios superiores a 3000
ciudades_con_ingresos_superiores_4000 = archivo_1.groupby('ciudad')['ingresos'].mean()
ciudades_con_ingresos_superiores_4000 = ciudades_con_ingresos_superiores_4000[ciudades_con_ingresos_superiores_4000 > 4000]
print("2. Ciudades con ingresos promedios superiores a 4000:")
print(ciudades_con_ingresos_superiores_4000)
print("="*40)

# 3. Ordenar por ingresos de forma ascendente
archivo_1_ordenado_por_ingresos = archivo_1.sort_values(by='ingresos', ascending=True)
print("3. Lista ordenada por ingresos de forma ascendente:")
print(archivo_1_ordenado_por_ingresos)
print("="*40)

# 4. Crear un histograma por edades
plt.hist(archivo_1['edad'], bins=10, edgecolor='black')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades')
plt.show()
print("="*40)


# 5. Agregar una columna de impuesto (11% del ingreso)
archivo_1['impuesto'] = archivo_1['ingresos'] * 0.11
print("5. DataFrame con columna de impuesto:")
print(archivo_1)
print("="*40)

# 6. Crear un gráfico pastel con el número de trabajadores por ciudad
trabajadores_por_ciudad = archivo_1['ciudad'].value_counts()
trabajadores_por_ciudad.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Distribución de Trabajadores por Ciudad')
plt.show()
print("="*40)