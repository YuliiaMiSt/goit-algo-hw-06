import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()

# Додаємо вершини (користувачі соціальної мережі)
users = ['JuliaShanel', 'Elkssenia', 'User1', 'User2', 'User3', 'User4', 'User5']
G.add_nodes_from(users)

# Додаємо ребра (підписки між користувачами)
subscriptions = [
    ('JuliaShanel', 'User1'), ('JuliaShanel', 'User2'),
    ('Elkssenia', 'User2'), ('Elkssenia', 'User3'),
    ('User1', 'User4'), ('User2', 'User5'), ('User3', 'User5'),
    ('User4', 'User5')
]
G.add_edges_from(subscriptions)

# Візуалізуємо граф
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Генерація координат вузлів
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=3000, font_size=12, font_weight='bold', edge_color='black')
plt.title("Соціальна мережа: Взаємозв'язки користувачів")
plt.show()

# Аналіз графа
print("Кількість вершин (користувачів):", G.number_of_nodes())
print("Кількість ребер (зв'язків):", G.number_of_edges())

# Ступінь кожної вершини
print("\nСтупінь кожної вершини:")
degree = dict(G.degree())
for node, deg in degree.items():
    print(f"{node}: {deg}")

# Середній ступінь вершини
average_degree = sum(degree.values()) / len(degree)
print("\nСередній ступінь вершини:", average_degree)

# Коефіцієнт кластеризації
clustering_coefficient = nx.average_clustering(G)
print("\nСередній коефіцієнт кластеризації:", clustering_coefficient)

# Перевірка, чи є граф зв'язним (чи всі користувачі між собою пов'язані)
is_connected = nx.is_connected(G)
print("\nГраф зв'язний?" , is_connected)

# Діаметр графа (максимальна відстань між вузлами, якщо граф зв'язний)
if is_connected:
    diameter = nx.diameter(G)
    print("Діаметр графа:", diameter)
else:
    print("Граф не є зв'язним, діаметр не визначено.")
