import networkx as nx
from database.dao import DAO
from model.rifiugio import Rifugio
from model.connessione import Connessione

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.rifugi = DAO.read_rifugi()
        self.sentieri = DAO.read_connessioni()

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        for sentiero in self.sentieri:
            if sentiero.anno <= year:
                r1 = self.rifugi[sentiero.id_rifugio1]
                r2 = self.rifugi[sentiero.id_rifugio2]

                self.G.add_node(r1)
                self.G.add_node(r2)
                self.G.add_edge(r1, r2)


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        return self.G.nodes()

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        return self.G.degree[node]

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        return nx.number_connected_components(self.G)

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """
        visited = set()
        stack = [start.id]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                neighbors = list(self.G.neighbors(node))
                stack.extend(n for n in neighbors if n not in visited)
        visited.remove(start.id)
        return [self.id_to_rifugio[n] for n in visited]