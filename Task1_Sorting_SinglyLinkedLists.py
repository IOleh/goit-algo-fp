class Node:
    """Клас, що представляє вузол однозв'язного списку."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Клас, що представляє однозв'язний список."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додає новий вузол до кінця списку."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """Виводить всі елементи списку."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсує однозв'язний список, змінюючи посилання між вузлами."""
        prev, current = None, self.head
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev

    def insertion_sort(self):
        """Сортує однозв'язний список методом вставок."""
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, sorted_list, new_node):
        """Вставляє вузол у відсортований список."""
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node
        current = sorted_list
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return sorted_list

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Об'єднує два відсортовані однозв'язні списки в один."""
        dummy = Node(0)
        tail = dummy
        while list1 and list2:
            if list1.data < list2.data:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next


# Створюємо перший однозв'язний список
list1 = LinkedList()
for value in [3, 1, 4, 2]:
    list1.append(value)

# Створюємо другий однозв'язний список
list2 = LinkedList()
for value in [5, 0, 6]:
    list2.append(value)

# Виводимо обидва списки
print("Перший список:")
list1.print_list()
print("Другий список:")
list2.print_list()

# Реверсуємо та сортуємо перший список
list1.reverse()
print("Реверсований перший список:")
list1.print_list()
list1.insertion_sort()
print("Відсортований перший список:")
list1.print_list()

# Сортуємо другий список
list2.insertion_sort()
print("Відсортований другий список:")
list2.print_list()

# Об'єднуємо два відсортовані списки
merged_list = LinkedList.merge_sorted_lists(list1.head, list2.head)
print("Об'єднаний список:")
merged = LinkedList()
merged.head = merged_list
merged.print_list()
