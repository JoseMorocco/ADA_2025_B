from Grafo import Grafo
from Algoritmos import bellman_ford_con_pasos
import matplotlib.pyplot as plt
import math 

def imprimir_tasas_y_pesos(tasas):
    """Función auxiliar para mostrar las tasas y sus pesos logarítmicos."""
    print("Tasas de Cambio (Aristas) y sus Pesos (-log(tasa)):")
    for (u, v), tasa in tasas.items():
        peso = -math.log(tasa)
        print(f"  {u} -> {v}: Tasa = {tasa:<6.3f} | Peso = {peso:<7.4f}")

def Ejercicio6():
    # 1. Crear el grafo y los vértices (monedas)
    g_arbitraje = Grafo()
    vertices = ['PEN', 'USD', 'EUR', 'CLP']
    for v in vertices:
        g_arbitraje.agregar_vertice(v)

    # 2. Definir las tasas de cambio
    # Tasas(A, B) = Cuántas unidades de B obtienes por 1 unidad de A
    # ¡Hemos creado un ciclo de ganancia (negativo) intencional!
    # PEN -> USD -> EUR -> PEN
    
    tasas = {
        # Tasa "normal"
        ('PEN', 'USD'): 0.27,    # 1 PEN -> 0.27 USD
        ('USD', 'PEN'): 3.65,    # 1 USD -> 3.65 PEN
        
        ('PEN', 'EUR'): 0.25,    # 1 PEN -> 0.25 EUR
        ('EUR', 'PEN'): 3.90,    # 1 EUR -> 3.90 PEN
        
        ('PEN', 'CLP'): 230.0,   # 1 PEN -> 230 CLP
        ('CLP', 'PEN'): 0.0043,  # 1 CLP -> 0.0043 PEN
        
        ('USD', 'EUR'): 0.92,    # 1 USD -> 0.92 EUR
        ('EUR', 'USD'): 1.08,    # 1 EUR -> 1.08 USD
        
        # --- ¡CICLO DE ARBITRAJE OCULTO! ---
        # Una casa de cambio "X" ofrece tasas raras:
        ('USD', 'CLP'): 850.0,   # 1 USD -> 850 CLP
        ('CLP', 'EUR'): 0.0011,  # 1 CLP -> 0.0011 EUR
        ('EUR', 'USD'): 1.09,    # 1 EUR -> 1.09 USD (¡Tasa alta!)
        
        # Ciclo: USD -> CLP -> EUR -> USD
        # 1 * 850 * 0.0011 * 1.09 = 1.0213 (¡Una ganancia del 2.13%!)
        # -log(850) + -log(0.0011) + -log(1.09) = -6.74 + 6.81 - 0.086 = -0.016 (¡Negativo!)
    }
    
    # 3. Agregar aristas con sus pesos (-log(tasa))
    for (u, v), tasa in tasas.items():
        peso = -math.log(tasa)
        g_arbitraje.agregar_arista(u, v, peso, dirigido=True)

    imprimir_tasas_y_pesos(tasas)
    
    # 4. Calcular posiciones y definir inicio
    pos = g_arbitraje.get_nx_pos(dirigido=True, seed=2) 
    vertice_inicio = 'USD' # Empezamos desde USD para encontrar el ciclo
    print(f"\nEjecutando Bellman-Ford desde '{vertice_inicio}' para detectar ciclos...")
    print("="*50)

    # 5. Ejecutar Bellman-Ford y obtener pasos
    distancias, ciclo_detectado, pasos = bellman_ford_con_pasos(g_arbitraje, vertice_inicio)
    
    # 6. Mostrar los pasos (texto y gráfico)
    print("Visualizando los pasos del algoritmo (buscando inestabilidad)...")
    
    for i, paso in enumerate(pasos):
        print(f"\n{paso['titulo']}")
        print("-" * len(paso['titulo']))
        
        # Imprimir "costos" 
        dist_str = ", ".join(
            f"{v}: {d:<7.4f}" if d != float('inf') else f"{v}: ∞"
            for v, d in sorted(paso['distancias'].items())
        )
        print(f"Costos (neg-log): {dist_str}")
        if paso['relaxed_edges']:
             print(f"Tasas 'útiles' encontradas en este paso: {len(paso['relaxed_edges'])}")
        
        g_arbitraje.dibujar_grafo_paso(pos, 
                             paso['titulo'], 
                             dirigido=True,
                             relaxed_edges=paso['relaxed_edges'],
                             cycle_highlight=paso.get('cycle_highlight')
                            )
        
        if i < len(pasos) - 1:
            print("\n>>> Cierra la ventana del gráfico para continuar al siguiente paso...")
            plt.show()
        else:
            print("\nAlgoritmo finalizado. Mostrando el resultado final.")
            plt.show() 

    # 7. Mostrar resultados finales
    print("\n" + "="*50)
    print(f"--- Resultados Finales de Bellman-Ford ---")
    if ciclo_detectado:
        camino_ciclo_str = " -> ".join(ciclo_detectado)
        print(f"  ¡ÉXITO! Se detectó una oportunidad de arbitraje (Ciclo Negativo).")
        print(f"  Ruta de ganancia encontrada: {camino_ciclo_str}")
    else:
        print("  Algoritmo finalizado. No se encontraron oportunidades de arbitraje.")
        
    print("\n  Costos finales (un costo -inf indica que es parte de un ciclo negativo):")
    for vertice, distancia in distancias.items():
        print(f"    Costo para llegar a {vertice}: {distancia}")

if __name__ == "__main__":
    Ejercicio6()