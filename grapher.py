import sys
import pandas as pd
import numpy as np
#import altair as alt
#import nbinteract as nbi
#import ipywidgets as widgets
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
    color_variable = input("Ingrese un color en inglés: ").split(",")
    # Generar el histograma
    data.hist(column=columnas, bins=bins,color=color_variable,edgecolor='black')
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
    color_variable = input("Ingrese un color en inglés: ").split(",")
    # Generar el gráfico de barras
    data.plot.bar(x=columnas[0], y=columnas[1],color=color_variable,edgecolor='black')
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
    color_variable = input("Ingrese un color en inglés: ").split(",")
    # Generar el gráfico de dispersión
    data.plot.scatter(x=columnas[0], y=columnas[1],color=color_variable,edgecolor='black')
    #Crear el nombre para el gráfico generado
    nombre_img = input("Escriba el nombre con el que quira que se guarde la gráfica: ")
    extension_img = input("Escriba la extension con la que quiera que se guarde la imagen (.png o .jpg): ")
    img = nombre_img + extension_img
    plt.savefig(img)
    plt.show()
    """     Altair
elif opcion == 4:
    # Pedir al usuario las columnas del DataFrame que se utilizarán para el gráfico de barras apiladas
    print("Columnas disponibles:")
    print(data.columns)
    columnas = input("Ingrese las columnas que desea utilizar separadas por comas: ").split(",")

    # Crear un DataFrame con las columnas seleccionadas
    df = pd.DataFrame({
        "x": data[columnas[0]],
        "y": data[columnas[1]],
    })

    # Generar el gráfico de barras apiladas utilizando Altair
    bar_chart = alt.Chart(df).mark_bar().encode(
        x='x',
        y='y',
        color='x'
    ).properties(
        width=600,
        height=400
    )
    # Guardar el gráfico generado
    nombre_img = input("Escriba el nombre con el que quiera que se guarde la gráfica: ")
    extension_img = input("Escriba la extensión con la que quiera que se guarde la imagen (.png o .jpg): ")
    img = nombre_img + extension_img
    bar_chart.save(img)
    # Mostrar el gráfico
    bar_chart.show()
    """
    """     Nbinteract 
elif opcion == 5:
    # Pedir al usuario las columnas del DataFrame que se utilizarán para el gráfico de dispersión
    print("Columnas disponibles:")
    print(data.columns)
    columnas = input("Ingrese las columnas que desea utilizar separadas por comas: ").split(",")

    # Crear un DataFrame con las columnas seleccionadas
    df = pd.DataFrame({
        "x": data[columnas[0]],
        "y": data[columnas[1]]
    })

    # Generar el gráfico de dispersión utilizando Matplotlib
    plt.scatter(df["x"], df["y"])
    plt.xlabel(columnas[0])
    plt.ylabel(columnas[1])
    plt.title("Gráfico de dispersión")
    plt.show()

    # Generar la visualización interactiva con Nbinteract
    @widgets.interact(x=df[columnas[0]], y=df[columnas[1]])
    def scatter_plot(x, y):
        plt.scatter(x, y)
        plt.xlabel(columnas[0])
        plt.ylabel(columnas[1])
        plt.title("Gráfico de dispersión interactivo")
        plt.show()
    """
else:
    print("Opción no válida. Saliendo del programa.")
