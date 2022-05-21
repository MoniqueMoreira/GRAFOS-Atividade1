from grafo import Grafo
import numpy as np
import matriz

robot_pos_c = [9,0] # Robot current position linha 9 coluna 0
robot_pos_d = [0,2] # Robot desired position linha 0 coluna 2


def criar_vertices(occupancy):
  g = Grafo()
  for l in range(0,10):
    for c in range(0,10):
      lista = []
      if occupancy[l][c] != np.inf:
        lista.append(l)
        lista.append(c)
        g.set_vertice(lista)
  return g

def criar_arestas(g,occupancy):
  vs = g.get_vertices()
  for i in vs:
    l = i[0]
    c = i[1]
    if g.existe_vertice([i[0],i[1]+1]):
      g.set_aresta(i,[i[0],i[1]+1],occupancy[l][c+1])
    if g.existe_vertice([i[0]+1,i[1]]):
      g.set_aresta(i,[i[0]+1,i[1]],occupancy[l+1][c])
  return g

def robot_path(robot_pos_c, robot_pos_d, occupancy):
  path = []
  g = criar_vertices(occupancy)
  g = criar_arestas(g,occupancy)
  g.Dijkstra(robot_pos_c)
  path= g.caminho_minimo(robot_pos_c,robot_pos_d)
  return path

def inicio():
  #  Matriz com uniforme(1's)
  occupancy = matriz.matriz1()
  matriz.imprimir_matriz(occupancy)
  path= robot_path(robot_pos_c, robot_pos_d,occupancy)
  print("Caminho Minimo: ")
  print(path)
  # Matriz com terreno não uniforme(Float)
  occupancy = matriz.matriz2()
  matriz.imprimir_matriz(occupancy)
  path= robot_path(robot_pos_c, robot_pos_d,occupancy)
  print("Caminho Minimo: ")
  print(path)
inicio()