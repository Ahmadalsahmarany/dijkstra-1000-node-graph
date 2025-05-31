import random
from collections import defaultdict

# Grafik sınıfı: düğümleri ve kenarları temsil eder
class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes  # Düğüm sayısı
        self.adj = defaultdict(list)  # Komşuluk listesi: her düğüm için komşular ve ağırlıklar

    # İki düğüm arasında çift yönlü kenar (edge) ekler
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # Rastgele kenarlar oluşturur (tekrar eden kenarlar eklenmez)
    def generate_random_edges(self, num_edges, max_weight=10):
        added = set()  # Eklenen kenarları takip etmek için
        while len(added) < num_edges:
            u = random.randint(0, self.num_nodes - 1)
            v = random.randint(0, self.num_nodes - 1)
            if u != v and (u, v) not in added and (v, u) not in added:
                w = random.randint(1, max_weight)
                self.add_edge(u, v, w)
                added.add((u, v))

# 🔗 Tüm düğümleri birbirine bağlayan (connected) grafik oluşturur
def generate_connected_graph(num_nodes, extra_edges=1000):
    g = Graph(num_nodes)

    # Adım 1: Düğümleri sırayla birbirine bağla (bağlantılı hale getirmek için)
    for i in range(num_nodes - 1):
        g.add_edge(i, i + 1, random.randint(1, 10))

    # Adım 2: Rastgele ekstra kenarlar ekle (grafiği daha karmaşık hale getirir)
    g.generate_random_edges(extra_edges)

    return g
