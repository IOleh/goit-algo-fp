import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)  # Додаємо вузол до графа з міткою
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додаємо ребро до лівого нащадка
            l = x - 1 / 2 ** layer  # Обчислюємо позицію для лівого нащадка
            pos[node.left.id] = (l, y - 1)  # Зберігаємо позицію
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # Рекурсивно обробляємо лівого нащадка
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додаємо ребро до правого нащадка
            r = x + 1 / 2 ** layer  # Обчислюємо позицію для правого нащадка
            pos[node.right.id] = (r, y - 1)  # Зберігаємо позицію
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)  # Рекурсивно обробляємо правого нащадка
    return graph

def draw_tree(tree_root, node_colors):
    # Функція для візуалізації дерева з кольорами вузлів
    tree = nx.DiGraph()  # Створюємо направлений граф
    pos = {tree_root.id: (0, 0)}  # Визначаємо позицію кореня
    tree = add_edges(tree, tree_root, pos)  # Додаємо вузли і ребра до графа

    # Збираємо кольори та мітки для візуалізації
    colors = [node_colors[node[0]] for node in tree.nodes(data=True)]  # Отримуємо кольори вузлів
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуємо значення вузла для міток

    # Створюємо візуалізацію
    plt.figure(figsize=(8, 5))  # Встановлюємо розмір фігури
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)  # Малюємо граф
    plt.show()  # Відображаємо графік

def generate_color(step, total_steps):
    """Генерація кольору в 16-ковій системі RGB на основі порядку обходу"""
    # Визначаємо темні та світлі відтінки
    intensity = int(255 * (step / total_steps))  # Пропорційна інтенсивність кольору
    return f'#{intensity:02X}96F0'  # Використовуємо синій відтінок

def depth_first_search(root):
    """Обхід у глибину (DFS)"""
    stack = [root]  # Стек для обходу
    visited = set()  # Відвідані вузли
    node_colors = {}  # Словник для кольорів вузлів
    steps = []  # Список кроків обходу

    while stack:
        node = stack.pop()  # Витягуємо вузол з верху стеку
        if node not in visited:
            visited.add(node)  # Позначаємо вузол як відвіданий
            steps.append(node)  # Додаємо вузол до списку кроків
            # Додаємо нащадків до стеку (правий, потім лівий)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # Генеруємо кольори для відвіданих вузлів
    for step, node in enumerate(steps):
        node_colors[node.id] = generate_color(step, len(steps))  # Генеруємо колір для вузла

    return node_colors

def breadth_first_search(root):
    """Обхід в ширину (BFS)"""
    queue = [root]  # Черга для обходу
    visited = set()  # Відвідані вузли
    node_colors = {}  # Словник для кольорів вузлів
    steps = []  # Список кроків обходу

    while queue:
        node = queue.pop(0)  # Витягуємо перший вузол з черги
        if node not in visited:
            visited.add(node)  # Позначаємо вузол як відвіданий
            steps.append(node)  # Додаємо вузол до списку кроків

            # Додаємо нащадків до черги (лівий, потім правий)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Генеруємо кольори для відвіданих вузлів
    for step, node in enumerate(steps):
        node_colors[node.id] = generate_color(step, len(steps))  # Генеруємо колір для вузла

    return node_colors

# Створення бінарного дерева
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

# Візуалізація обходу в глибину (DFS)
dfs_colors = depth_first_search(root)  # Отримуємо кольори для DFS
draw_tree(root, dfs_colors)  # Візуалізуємо дерево з кольорами DFS

# Візуалізація обходу в ширину (BFS)
bfs_colors = breadth_first_search(root)  # Отримуємо кольори для BFS
draw_tree(root, bfs_colors)  # Візуалізуємо дерево з кольорами BFS
