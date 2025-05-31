# Dijkstra algoritmasını elle (hazır yapılar kullanmadan) uygular
def dijkstra(graph, start):
    n = graph.num_nodes  # Toplam düğüm sayısı
    dist = [float('inf')] * n  # Başlangıçta tüm uzaklıklar sonsuz
    prev = [None] * n  # Her düğümün önceki (parent) düğümünü tutar
    visited = [False] * n  # Ziyaret edilen düğümleri takip eder
    steps = []  # Görselleştirme için her adımda ne olduğunu kaydeder

    dist[start] = 0  # Başlangıç düğümünün kendisine olan uzaklığı sıfırdır

    for _ in range(n):
        u = -1
        min_dist = float('inf')

        # Henüz ziyaret edilmemiş düğümler arasından en kısa mesafeye sahip olanı seç
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break  # Ulaşılmayan düğüm kalmadıysa döngüden çık

        visited[u] = True  # Düğüm artık ziyaret edildi

        # Görselleştirme için mevcut durumu kaydet
        steps.append({
            'current': u,
            'distances': dist.copy(),
            'visited': visited.copy()
        })

        # Komşularla olan kenarları gevşet (relax)
        for v, w in graph.adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    return dist, prev, steps  # En kısa mesafeler, önceki düğümler ve tüm adımlar
