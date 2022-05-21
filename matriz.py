import numpy as np

def imprimir_matriz(occupancy):
  for l in range(0,10):
    for c in range(0,10):
      print("{:.2f}".format(occupancy[l][c]),end="\t")
    print("\n")

def matriz1():
    occupancy = np.ones((10, 10))
    occupancy[0:5, 0] = np.inf
    occupancy[5, 0:5] = np.inf
    occupancy[5:8, 5] = np.inf
    occupancy[0:3, 5:8] = np.inf
    occupancy[7:9, 3] = np.inf
    occupancy[5:10, 8] = np.inf
    #print(occupancy)
    return occupancy

def matriz2():
  occupancy = 10 * np.random.rand(10, 10)
  occupancy[0:5, 0] = np.inf
  occupancy[5, 0:5] = np.inf
  occupancy[5:8, 5] = np.inf
  occupancy[0:3, 5:8] = np.inf
  occupancy[7:9, 3] = np.inf
  occupancy[5:10, 8] = np.inf
  #print(occupancy)
  return occupancy