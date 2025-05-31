from graph import generate_connected_graph  # Bağlantılı grafik oluşturmak için fonksiyon
from dijkstra import dijkstra               # Dijkstra algoritması
from visualize import layout_positions, draw_step  # Görselleştirme fonksiyonları
import os

if __name__ == "__main__":
    # 1000 düğümden oluşan bağlantılı bir grafik oluşturuluyor
    # Ekstra 1000 kenar ile daha karmaşık hale getiriliyor
    g = generate_connected_graph(1000, extra_edges=1000)

    # Dijkstra algoritması çalıştırılıyor, başlangıç düğümü: 0
    dist, prev, steps = dijkstra(g, 0)

    # "steps" adında bir klasör oluşturuluyor (zaten varsa hata vermez)
    os.makedirs("steps", exist_ok=True)

    # Düğümlere rastgele koordinatlar atanıyor (görsel yerleşim için)
    pos = layout_positions(range(g.num_nodes))

    # Her 5 adımda bir görsel oluşturuluyor (çok fazla dosya olmaması için)
    for i in range(0, len(steps), 5):
        draw_step(g, steps[i], pos, i, "steps")
