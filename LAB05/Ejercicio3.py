from Grafo import Grafo
from Algoritmos import bellman_ford_con_pasos
import matplotlib.pyplot as plt

def Ejercicio3():
    
    # 1. Crear manualmente un grafo dirigido con un ciclo negativo
    g_ciclo_neg = Grafo()
    g_ciclo_neg.agregar_arista('A', 'B', 3, dirigido=True)
    g_ciclo_neg.agregar_arista('B', 'C', 2, dirigido=True)
    g_ciclo_neg.agregar_arista('C', 'D', 4, dirigido=True)
    g_ciclo_neg.agregar_arista('D', 'B', -10, dirigido=True) # Ciclo B->C->D->B
    g_ciclo_neg.agregar_arista('A', 'D', 1, dirigido=True)
    g_ciclo_neg.agregar_arista('E', 'A', 5, dirigido=True) # Nodo extra

    print(g_ciclo_neg)
    
    # 2. Definir inicio y calcular posiciones
    vertice_inicio = 'A'
    pos = g_ciclo_neg.get_nx_pos(dirigido=True) 
    print(f"Ejecutando Bellman-Ford desde '{vertice_inicio}'...")
    print("="*50)

    # 3. Ejecutar Bellman-Ford y obtener pasos
    distancias, ciclo_detectado, pasos = bellman_ford_con_pasos(g_ciclo_neg, vertice_inicio)
    
    # 4. Mostrar los pasos 
    print("Visualizando los pasos del algoritmo (un gráfico por cada iteración)...")
    
    for i, paso in enumerate(pasos):
        print(f"\n{paso['titulo']}")
        print("-" * len(paso['titulo']))
        
        # Imprimir distancias actuales en texto
        dist_str = ", ".join(
            f"{v}: {d if d != float('inf') else '∞'}" 
            for v, d in sorted(paso['distancias'].items())
        )
        print(f"Distancias: {dist_str}")
        if paso['relaxed_edges']:
             print(f"Aristas relajadas en este paso: {len(paso['relaxed_edges'])}")
        
        # Generar el gráfico para este paso
        g_ciclo_neg.dibujar_grafo_paso(pos, 
                             paso['titulo'], 
                             dirigido=True,
                             # No pasar distancias
                             relaxed_edges=paso['relaxed_edges'],
                             cycle_highlight=paso.get('cycle_highlight')
                            )
        
        if i < len(pasos) - 1:
            print("\n>>> Cierra la ventana del gráfico para continuar al siguiente paso...")
            plt.show()
        else:
            print("\nAlgoritmo finalizado. Mostrando el último paso.")
            plt.show() 

    # 5. Mostrar resultados finales
    print("\n" + "="*50)
    print(f"--- Resultados Finales de Bellman-Ford ---")
    if ciclo_detectado:
        camino_ciclo_str = " -> ".join(ciclo_detectado)
        print(f"  ¡ÉXITO! Se detectó un ciclo de peso negativo.")
        print(f"  Nodos en el ciclo: {camino_ciclo_str}")
    else:
        print("  Algoritmo finalizado. No se encontraron ciclos negativos.")
        
    print("\n  Distancias finales (pueden ser -inf si hay ciclo):")
    for vertice, distancia in distancias.items():
        print(f"    Distancia de {vertice_inicio} a {vertice}: {distancia}")

if __name__ == "__main__":
    Ejercicio3()