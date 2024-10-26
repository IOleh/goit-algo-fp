# Вхідні дані: словник з інформацією про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості
    ratio_items = [(item, value['calories'] / value['cost']) for item, value in items.items()]
    
    # Сортуємо за співвідношенням (зменшенням)
    ratio_items.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    selected_items = []
    
    for item, ratio in ratio_items:
        cost = items[item]['cost']
        calories = items[item]['calories']
        
        if cost <= budget:
            budget -= cost
            total_calories += calories
            selected_items.append(item)
    
    return total_calories, selected_items

def dynamic_programming(items, budget):
    n = len(items)
    dp = [0] * (budget + 1)  # Массив для зберігання максимальних калорій для кожного бюджету
    selected_items = [[] for _ in range(budget + 1)]  # Список для зберігання вибраних страв
    
    # Список предметів з їх вартістю та калорійністю
    item_list = list(items.items())
    
    for i in range(n):
        item, value = item_list[i]
        cost = value['cost']
        calories = value['calories']
        
        # Проходимо від бюджету до вартості елемента
        for w in range(budget, cost - 1, -1):
            if dp[w] < dp[w - cost] + calories:
                dp[w] = dp[w - cost] + calories
                selected_items[w] = selected_items[w - cost] + [item]

    return dp[budget], selected_items[budget]

# Приклад використання
budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Максимальні калорії:", greedy_result[0])
print("Вибрані страви:", greedy_result[1])

dynamic_result = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Максимальні калорії:", dynamic_result[0])
print("Вибрані страви:", dynamic_result[1])
