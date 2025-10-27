import pandas as pd
import matplotlib.pyplot as plt

def generar_grafica_comparativa():

    nombre_archivo = "tiempos.csv"
    
    # 1. Leer los datos del CSV usando pandas
    try:
        df = pd.read_csv(nombre_archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        print("Por favor, ejecuta 'problema4.py' primero para generar el archivo.")
        return
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return

    print(f"Datos leídos de '{nombre_archivo}':")
    print(df)

    # 2. Preparar los ejes para la gráfica
    # Usaremos 'V' (Número de Vértices) como el eje X
    x_axis = 'V'
    
    # 3. Generar la gráfica
    plt.figure(figsize=(12, 7))
    
    plt.plot(df[x_axis], df['Dijkstra'], label='Dijkstra (V+E log V)', marker='o')
    plt.plot(df[x_axis], df['BellmanFord'], label='Bellman-Ford (V * E)', marker='s')
    plt.plot(df[x_axis], df['FloydWarshall'], label='Floyd-Warshall (V^3)', marker='^')
    
    # 4. Configurar la apariencia de la gráfica
    plt.title('Comparación de Tiempos de Ejecución de Algoritmos de Grafos')
    plt.xlabel('Número de Vértices (V)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.legend()  
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # 5. Usar escala logarítmica en el eje Y para ver mejor
    # las diferencias, ya que Floyd-Warshall será mucho más lento.
    plt.yscale('log')
    plt.ylabel('Tiempo de Ejecución (segundos, escala logarítmica)')
    
    # 6. Guardar y mostrar la gráfica
    nombre_grafica = "comparacion_tiempos.png"
    try:
        plt.savefig(nombre_grafica)
        print(f"\nGráfica guardada como '{nombre_grafica}'")
        plt.show() 
    except Exception as e:
        print(f"Error al guardar o mostrar la gráfica: {e}")

if __name__ == "__main__":
    generar_grafica_comparativa()