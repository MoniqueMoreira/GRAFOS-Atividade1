class Vertice():
    def __init__(self, id):
        self.id = id
        self.estimativa = 999999
        self.anterior = "-"
        self.vizinhos = []

    def set_vizinho(self,u):
        self.vizinhos.append(u)

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa

class Aresta():
	def __init__(self,origem,destino,peso = 0):
		self.origem = origem
		self.destino = destino
		self.peso = peso
				
	def get_origem(self):
		return self.origem
		
	def get_Destino(self):
		return self.destino
	
	def set_peso(self,peso):
		self.peso = peso
		
	def	get_Peso(self):
		return self.peso
		
	def set_Origem(self,vertice):
		self.origem = vertice
		
	def set_Destino(self,vertice):
		self.destino = vertice
	
class Grafo():
    def __init__(self, orientado = False, lenV = 0, lenA = 0 ) -> None:
        self.v = []
        self.a = []
        self.orientado = orientado
        self.ord = lenV
        self.size = lenA

    def set_orientado(self):
        # Definir de grafo é orintado
        self.orientado = True

    def get_direcionado(self):
        # Grafo orientado
        return self.orientado

    def get_ord(self):
        #Quantidade de vertices
        return len(self.v)
    
    def get_size(self):
        #Quantidade de aresta
        return len(self.a)

    def set_vertice(self,u):
        #Adicionar um vertice no grafo
        k = self.existe_vertice(u)
        if k == False:
            u = Vertice(u)
            self.v.append(u)
            self.ord = self.ord + 1
        else:
            print("Vertice já pertece ao Grafo")

    def existe_vertice(self, u):
        #Verificar se vertice está no grafo
        for i in self.v:
            if i.id == u:
                return True
        return False

    def get_vertices(self):
        #Retorna um lista de vertice presente no grafo
        vertices = []
        for i in self.v:
            vertices.append(i.id)
        return vertices

    def obj_vertice(self,v):
        for i in self.v:
            if i.id == v:
                return i

    def set_aresta(self,u,v,peso):
        uobj = self.obj_vertice(u)
        vobj = self.obj_vertice(v)
        
        # Adiciona uma aresta com orinetação
        aresta = Aresta(u,v,peso)
        self.a.append(aresta)
        uobj.set_vizinho(vobj)
        self.size = self.size + 1
        if self.orientado == False:
            # Adiciona uma aresta
            aresta = Aresta(v,u,peso)
            self.a.append(aresta)
            vobj.set_vizinho(uobj)
            self.size = self.size + 1
   
    def get_arestas(self):
        # Retorna uma lista com as aresta
        p = []
        for i in self.a:
            k  = []
            k.append(i.origem)
            k.append(i.destino)
            k.append(i.peso)
            p.append(k)
        return p

    def existe_aresta(self,u,v):
        #Veriificar se existe a aresta
        for i in self.a:
            if i.origem == u and i.destino == v:
                return True 
        return False

    def __str__(self) -> str:
        #imprimir grafo
        print("Vertices: ")
        print(self.get_vertices())
        print("Arestas: ")
        print(self.get_arestas())
    
# Dijkstra --------------------------------------------------------------------
    def get_peso(self,u,v):
        for i in self.a:
            if i.origem == u and i.destino == v:
                return i.peso

    def inicia_vertices(self,u):
        for i in self.v:
            i.estimativa = 99999
            if u == i.id:
                i.estimativa = 0

    def menor_estimativa(self,lista_vertices):
        dmenor = 99999
        for i in lista_vertices:
            if i.estimativa <= dmenor:
                dmenor = i.estimativa
                v = i
        return v
    
    def print_Dijkstra(self):
        print("Vertices:\t",end="\t")
        for i in self.v:
            print(i.id,end="\t")
        print("\nDistancia:\t",end="\t")
        for i in self.v:
            print(i.estimativa,end="\t")
        print("\nAnteriores:\t", end="\t")
        for i in self.v:
            print(i.anterior,end="\t")
    
    def caminho_minimo(self,u,v):
        cam = []
        iv = self.obj_vertice(v)
        while v != u:
            cam.append(v)
            v = iv.anterior
            iv = self.obj_vertice(v)
        cam.append(v)
        cam1 = list(reversed(cam))
        return cam1

    def Dijkstra(self,u):
        lista_vertices = self.v.copy()
        self.inicia_vertices(u)
        while len(lista_vertices)!= 0:
            v = self.menor_estimativa(lista_vertices)
            lista_vertices.remove(v)
            for i in v.vizinhos:
                peso = self.get_peso((v.id),(i.id))
                nova_estimativa = v.estimativa + peso
                if nova_estimativa < i.estimativa:
                    i.estimativa = nova_estimativa
                    i.anterior = v.id
        #self.print_Dijkstra()

        