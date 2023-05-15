import sys
import pandas as pd
import matplotlib.pyplot as plt

# Obtener la ubicación del archivo .csv desde la línea de comandos
csv_file = sys.argv[1]

# Cargar el archivo .csv en un DataFrame de pandas
data = pd.read_csv(csv_file)

# Mostrar un menú de opciones de gráficos disponibles
print("Seleccione el tipo de gráfico que desea generar:")
print("1. Histograma")
print("2. Gráfico de barras")
print("3. Gráfico de dispersión")
opcion = int(input("Opción seleccionada: "))

# Generar el gráfico seleccionado
if opcion == 1:
    # Pedir al usuario el número de bins para el histograma
    bins = int(input("Ingrese el número de bins para el histograma: "))
    # Pedir al usuario las columnas del DataFrame que se utilizarán para el histograma
    print("Columnas disponibles:")
    print(data.columns)
    columnas = input("Ingrese las columnas que desea utilizar separadas por comas: ").split(",")
    # Generar el histograma
    data.hist(column=columnas, bins=bins)
    #Crear el nombre para el gráfico generado
    nombre_img = input("Escriba el nombre con el que quira que se guarde la gráfica: ")
    extension_img = input("Escriba la extension con la que quiera que se guarde la imagen (.png o .jpg): ")
    img = nombre_img + extension_img
    plt.savefig(img)
    plt.show()
elif opcion == 2:
    # Pedir al usuario las columnas del DataFrame que se utilizarán para el gráfico de barras
    print("Columnas disponibles:")
    print(data.columns)
    columnas = input("Ingrese las columnas que desea utilizar separadas por comas: ").split(",")
    # Generar el gráfico de barras
    data.plot.bar(x=columnas[0], y=columnas[1])
    #Crear el nombre para el gráfico generado
    nombre_img = input("Escriba el nombre con el que quira que se guarde la gráfica: ")
    extension_img = input("Escriba la extension con la que quiera que se guarde la imagen (.png o .jpg): ")
    img = nombre_img + extension_img
    plt.savefig(img)
    plt.show()
elif opcion == 3:
    # Pedir al usuario las columnas del DataFrame que se utilizarán para el gráfico de dispersión
    print("Columnas disponibles:")
    print(data.columns)
    columnas = input("Ingrese las columnas que desea utilizar separadas por comas: ").split(",")
    # Generar el gráfico de dispersión
    data.plot.scatter(x=columnas[0], y=columnas[1])
    #Crear el nombre para el gráfico generado
    nombre_img = input("Escriba el nombre con el que quira que se guarde la gráfica: ")
    extension_img = input("Escriba la extension con la que quiera que se guarde la imagen (.png o .jpg): ")
    img = nombre_img + extension_img
    plt.savefig(img)
    plt.show()
else:
    print("Opción no válida. Saliendo del programa.")
