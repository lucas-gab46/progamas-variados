import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios (substitua por dados reais do grSim)
robot_path = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)] 
obstacles = [(0.5, 0.5)] 

def plot_visibility_graph(path, obstacles):
    x, y = zip(*path)
    ox, oy = zip(*obstacles)
    
    plt.plot(x, y, "-b", label="Trajetória")
    plt.plot(x[0], y[0], "og", label="Início")
    plt.plot(x[-1], y[-1], "or", label="Fim")
    plt.scatter(ox, oy, c="k", label="Obstáculos")
    
    # Grafo de visibilidade simples (linhas entre pontos visíveis)
    for i in range(len(path)-1):
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]], "g--")
    
    plt.legend()
    plt.grid(True)
    plt.title("Grafo de Visibilidade")
    plt.show()

# Plota
plot_visibility_graph(robot_path, obstacles)

 