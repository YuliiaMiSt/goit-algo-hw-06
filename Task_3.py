import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()

# Додаємо вершини (користувачі соціальної мережі)
users = ['JuliaShanel', 'Elkssenia', 'User1', 'User2', 'User3', 'User4', 'User5']
G.add_nodes_from(users)

# Додаємо ребра з вагами (підписки між користувачами та вага зв'язку)
# Вага тут може представляти силу зв'язку, кількість повідомлень тощо
subscriptions = [
    ('JuliaShanel', 'User1', 2), ('JuliaShanel', 'User2', 1),
    ('Elkssenia', 'User2', 3), ('Elkssenia', 'User3', 1),
    ('User1', 'User4', 2), ('User2', 'User5', 4), ('User3', 'User5', 2),
    ('User4', 'User5', 1)
]
G.add_weighted_edges_from(subscriptions)

# Візуалізуємо граф з вагами
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Генерація координат вузлів
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=3000, font_size=12, font_weight='bold', edge_color='black')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Соціальна мережа з вагами")
plt.show()

# Функція для знаходження найкоротших шляхів за допомогою алгоритму Дейкстри
def dijkstra_all_pairs(graph):
    shortest_paths = {}
    for node in graph.nodes():
        # Знаходимо найкоротші шляхи від поточного вузла до всіх інших
        shortest_paths[node] = nx.single_source_dijkstra_path_length(graph, node)
    return shortest_paths

# Отримуємо найкоротші шляхи між усіма вершинами
shortest_paths = dijkstra_all_pairs(G)

# Виведемо найкоротші шляхи для кожної пари вершин
print("Найкоротші шляхи між усіма вершинами:")
for start_node, paths in shortest_paths.items():
    print(f"Від {start_node}:")
    for end_node, distance in paths.items():
        print(f"  до {end_node}: {distance} одиниць")

# Знаходимо найкоротший шлях між двома конкретними користувачами
start_user = 'JuliaShanel'
goal_user = 'User5'
shortest_path = nx.dijkstra_path(G, start_user, goal_user)
shortest_distance = nx.dijkstra_path_length(G, start_user, goal_user)

print(f"\nНайкоротший шлях від {start_user} до {goal_user}: {shortest_path}")
print(f"Відстань за найкоротшим шляхом: {shortest_distance} одиниць")
