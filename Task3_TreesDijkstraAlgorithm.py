import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # для ненапрямленого графа

    def dijkstra(self, start):
        # Відстань до всіх вершин
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        
        # Використовуємо купу для зберігання вершин
        priority_queue = [(0, start)]  # (відстань, вершина)
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Якщо відстань більше, ніж вже знайдена, пропускаємо
            if current_distance > distances[current_vertex]:
                continue
            
            # Перебираємо сусідів
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                # Якщо новий шлях коротший, оновлюємо відстань
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances


# Приклад використання
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'E', 3)

    start_vertex = 'A'
    distances = g.dijkstra(start_vertex)
    
    print(f"Найкоротші шляхи від вершини '{start_vertex}':")
    for vertex, distance in distances.items():
        print(f"Вершина {vertex}: {distance}")
