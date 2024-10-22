import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створюємо граф (той самий з прикладу)
G = nx.Graph()

# Додаємо вершини
users = ['JuliaShanel', 'Elkssenia', 'User1', 'User2', 'User3', 'User4', 'User5']
G.add_nodes_from(users)

# Додаємо ребра
subscriptions = [
    ('JuliaShanel', 'User1'), ('JuliaShanel', 'User2'),
    ('Elkssenia', 'User2'), ('Elkssenia', 'User3'),
    ('User1', 'User4'), ('User2', 'User5'), ('User3', 'User5'),
    ('User4', 'User5')
]
G.add_edges_from(subscriptions)

# Функція пошуку в глибину (DFS)
def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path + [neighbor])
            if new_path:
                return new_path
    return None

# Функція пошуку в ширину (BFS)
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    return None

# Візуалізуємо граф
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Генерація координат вузлів
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=3000, font_size=12, font_weight='bold', edge_color='black')
plt.title("Соціальна мережа: Взаємозв'язки користувачів")
plt.show()

# Використовуємо алгоритми DFS і BFS для пошуку шляху між двома користувачами
start_user = 'JuliaShanel'
goal_user = 'User5'

dfs_path = dfs(G, start_user, goal_user)
bfs_path = bfs(G, start_user, goal_user)

# Виводимо результати
print("Шлях за DFS:", dfs_path)
print("Шлях за BFS:", bfs_path)

# Порівняння шляхів
if dfs_path != bfs_path:
    print("\nШляхи різняться:")
    print(f"DFS обрав шлях: {dfs_path}")
    print(f"BFS обрав шлях: {bfs_path}")
else:
    print("\nDFS і BFS знайшли однаковий шлях.")

