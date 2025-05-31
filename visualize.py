import matplotlib.pyplot as plt
import random

# Düğümlere rastgele (x, y) konumları atar (grafiği görsel olarak yerleştirmek için)
def layout_positions(nodes, w=1, h=1):
    return {n: (random.random() * w, random.random() * h) for n in nodes}

# Her adımı görselleştirmek için bir fonksiyon
def draw_step(graph, step, pos, index, folder):
    plt.figure(figsize=(16, 16))  # Grafiği büyük çiz (daha net görünüm)
    ax = plt.gca()
    ax.set_xticks([]); ax.set_yticks([])  # Eksen çizgileri kapatılıyor

    u = step['current']        # Şu an işlenen düğüm
    dist = step['distances']   # Düğümlere olan uzaklıklar
    visited = step['visited']  # Hangi düğümler ziyaret edildi

    # 🔗 Sadece her iki ucu da ziyaret edilmiş kenarları çiz
    for a in graph.adj:
        if not visited[a]:
            continue
        for b, _ in graph.adj[a]:
            if visited[b]:
                x1, y1 = pos[a]
                x2, y2 = pos[b]
                plt.plot([x1, x2], [y1, y2], color='gray', linewidth=0.5)

    # 🔴 veya ⚫ düğümleri çiz
    for node in range(graph.num_nodes):
        x, y = pos[node]
        renk = 'black' if visited[node] else 'red'
        plt.plot(x, y, 'o', color=renk, ms=3)
        if dist[node] < float('inf'):
            ax.text(x, y, str(dist[node]), fontsize=4)  # Uzaklığı yaz

    # 🔵 Şu an işlenen düğümü mavi olarak çiz
    x, y = pos[u]
    plt.plot(x, y, 'o', color='blue', ms=6)

    # Görseli kaydet
    plt.title(f"Adım {index}")
    plt.savefig(f"{folder}/step_{index:04d}.png", dpi=300)
    plt.close()
