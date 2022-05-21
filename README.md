# GRAFOS: Atividade 1

# Aplicação básica
## Um robô precisa planejar a menor rota em uma grade de ocupação. Suponha que a grade de ocupação é fornecida como uma matriz com células indicando espaço livre (1) e obstáculo (∞). No caso, para a grade de ocupação a seguir:

```
  occupancy = np.ones((10, 10))
  
  occupancy[0:5, 0] = np.inf
  
  occupancy[5, 0:5] = np.inf
  
  occupancy[5:8, 5] = np.inf
  
  occupancy[0:3, 5:8] = np.inf
  
  occupancy[7:9, 3] = np.inf
  
  occupancy[5:10, 8] = np.inf
  
  print(occupancy)
  
 ```
  
 ## Sabendo que o robô inicia em uma célula específica, e.g. pos = [9, 0], e deseja-se chegar em uma posição destino, e.g. pos_d = [0, 2]. O robô se move apenas na horizontal e vertical (não se move na diagonal). Espera-se de retorno uma lista com o caminho.
 
 ```
 robot_pos_c = [9, 0] # Robot current position
 
 robot_pos_d = [0, 2] # Robot desired position

  def robot_path(robot_pos, robot_pos_d, occupancy):

    path = []
  
    ***Insert code here***
  
    return path

path = robot_path(robot_pos_c, robot_pos_d) 
```
 

# Considerando terreno
  ## Agora vamos considerar que algumas células representam regiões com terreno de mais difícil acesso que outras (terreno íngreme, com maior atrito). Dessa vez as células da grade de ocupação terão um peso atribuído de maneira não uniforme.
  ```
  occupancy = 10 * np.random.rand(10, 10)
  occupancy[0:5, 0] = np.inf
  
  occupancy[5, 0:5] = np.inf
  
  occupancy[5:8, 5] = np.inf
  
  occupancy[0:3, 5:8] = np.inf
  
  occupancy[7:9, 3] = np.inf
  
  occupancy[5:10, 8] = np.inf
  
  print(occupancy)
  
  ```
  

## Espera-se que o mesmo código de cima funcione com esse cenário.

  path = robot_path(robot_pos_c, robot_pos_d, occupancy)

## A resolução e feita em 3 arquivos, o ***Robot.py*** que responsável pela parte da resolução do problema, o ***Grafo.PY*** que serve para criar No e Aresta(funções para gerenciamento um grafo) e o ***matriz.py*** que responsável por cria matriz(funções para gerenciamento uma matriz).

## O algoritmo busca resolver o problema dos caminho minímo, por meio da implementação do algoritmo de  ***Dijkstra***.

## Entrada: 
  Matriz[10][10], posição inicial [9,0], posicão final [0,2]
## Saída:
  Caminho minímo[]
## Exemplo de execução:
### Caso 1: Terreno uniforme (1's)
![Screenshot](caso1.png)
### Caso 1: Terreno não uniforme (Float)
![Screenshot](caso2.png)
### Caso 1: Terreno não uniforme (Float)
![Screenshot](caso3.png)
