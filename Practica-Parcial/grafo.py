class Grafo:
    def __init__(self, es_dirigido=False):
        self.adj_list = {}
        self.dirigido = es_dirigido

    def agregar_vertice(self, v):
        if v not in self.obtener_vertices():
            self.adj_list[v] = {}

    def agregar_arista(self, v, w, peso=1):
        self.adj_list[v][w] = peso
        if not self.dirigido:
            self.adj_list[w][v] = peso

    def sacar_vertice(self, v):
        self.adj_list.pop(v)

    def sacar_arista(self, v, w):
        self.adj_list[v].pop(w)
        if not self.dirigido:
            self.adj_list[w].pop(v)

    def obtener_vertices(self):
        vertices = []
        for vertice in self.adj_list:
            vertices.append(vertice)
        return vertices

    def adyacentes(self, v):
        adyacentes = []
        for adyacente in self.adj_list[v]:
            adyacentes.append(adyacente)
        return adyacentes

    def peso(self, v, w):
        return self.adj_list[v][w]
    
    def hay_arista(self, v, w):
        if v in self.adj_list and w in self.adj_list[v]:
            return True
        return False
    
    def obtener_aristas(self):
        aristas = []
        for v, adyacentes in self.adj_list.items():
            for adyacente, peso in adyacentes.items():
                aristas.append((v, adyacente, peso))
        return aristas
    
    def copiar(self):
        nuevo_grafo = Grafo(es_dirigido=self.dirigido)
        
        for vertice in self.adj_list:
            nuevo_grafo.agregar_vertice(vertice)
        
        for v, adyacentes in self.adj_list.items():
            for adyacente, peso in adyacentes.items():
                nuevo_grafo.agregar_arista(v, adyacente, peso)
                print(f"Copiando arista: ({v}, {adyacente}), Peso: {peso}")

        return nuevo_grafo



