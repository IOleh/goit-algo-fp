import uuid  # Імпорт бібліотеки для генерації унікальних ідентифікаторів
import networkx as nx  # Імпорт бібліотеки для роботи з графами
import matplotlib.pyplot as plt  # Імпорт бібліотеки для візуалізації графіків

class Node:
    def __init__(self, key, color="skyblue"):
        # Ініціалізація вузла з ключем, кольором та унікальним ідентифікатором
        self.left = None  # Лівий нащадок
        self.right = None  # Правий нащадок
        self.val = key  # Значення вузла
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Генерація унікального ідентифікатора для вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    # Функція для додавання вузлів і ребер до графа
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додаємо вузол до графа з кольором і міткою
        if node.left:  # Якщо є лівий нащадок
            graph.add_edge(node.id, node.left.id)  # Додаємо ребро до лівого нащадка
            l = x - 1 / 2 ** layer  # Обчислюємо позицію для лівого нащадка
            pos[node.left.id] = (l, y - 1)  # Зберігаємо позицію
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # Рекурсивно обробляємо лівого нащадка
        if node.right:  # Якщо є правий нащадок
            graph.add_edge(node.id, node.right.id)  # Додаємо ребро до правого нащадка
            r = x + 1 / 2 ** layer  # Обчислюємо позицію для правого нащадка
            pos[node.right.id] = (r, y - 1)  # Зберігаємо позицію
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)  # Рекурсивно обробляємо правого нащадка
    return graph  # Повертаємо граф з усіма вузлами і ребрами

def draw_tree(tree_root):
    # Функція для візуалізації дерева
    tree = nx.DiGraph()  # Створюємо направлений граф
    pos = {tree_root.id: (0, 0)}  # Визначаємо позицію кореня
    tree = add_edges(tree, tree_root, pos)  # Додаємо вузли і ребра до графа

    # Збираємо кольори та мітки для візуалізації
    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Отримуємо кольори вузлів
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуємо значення вузла для міток

    # Створюємо візуалізацію
    plt.figure(figsize=(8, 5))  # Встановлюємо розмір фігури
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)  # Малюємо граф
    plt.show()  # Відображаємо графік

def insert_into_heap(root, key):
    """Вставка нового ключа у бінарну купу"""
    new_node = Node(key)  # Створюємо новий вузол
    if root is None:
        return new_node  # Якщо купа порожня, повертаємо новий вузол
    else:
        # Використовуємо список для представлення рівнів купи
        queue = [root]  # Створюємо чергу для обходу дерева
        while queue:
            current = queue.pop(0)  # Витягуємо перший елемент з черги
            if not current.left:  # Якщо немає лівого нащадка
                current.left = new_node  # Додаємо нового вузла лівим нащадком
                break
            else:
                queue.append(current.left)  # Інакше додаємо лівого нащадка до черги

            if not current.right:  # Якщо немає правого нащадка
                current.right = new_node  # Додаємо нового вузла правим нащадком
                break
            else:
                queue.append(current.right)  # Інакше додаємо правого нащадка до черги

    # Після вставки виконуємо "просування" нової вершини до правильного місця для підтримання властивостей купи
    return heapify_up(root, new_node)

def heapify_up(root, node):
    """Просування вузла вгору для підтримання властивостей купи"""
    if node is root:  # Якщо вузол - корінь, немає чого просувати
        return root
    parent = find_parent(root, node)  # Знайти батьківський вузол
    if parent and node.val > parent.val:  # Якщо значення вузла більше за значення батьківського
        # Міняємо значення між батьківським та новим вузлом
        parent.val, node.val = node.val, parent.val  
        return heapify_up(root, parent)  # Рекурсивно просуваємо вгору
    return root

def find_parent(root, node):
    """Знайти батьківський вузол для заданого вузла"""
    if root is None:
        return None
    if root.left == node or root.right == node:
        return root
    left_search = find_parent(root.left, node)  # Шукаємо в лівому піддереві
    if left_search:
        return left_search
    return find_parent(root.right, node)  # Шукаємо в правому піддереві

# Створення бінарної купи
root = Node(10)  # Створюємо корінь купи з значенням 10
root = insert_into_heap(root, 5)  # Додаємо нові значення
root = insert_into_heap(root, 30)
root = insert_into_heap(root, 20)
root = insert_into_heap(root, 15)

# Візуалізація бінарної купи
draw_tree(root)  # Візуалізуємо купу за допомогою функції draw_tree
