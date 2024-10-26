import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def simulate_dice_rolls(num_rolls):
    # Ініціалізація масиву для підрахунку сум
    sums_count = np.zeros(13)  # Індекси 0-12, 0 та 1 не використовуються
    
    # Симуляція кидків кубиків
    for _ in range(num_rolls):
        die1 = np.random.randint(1, 7)  # Кубик 1
        die2 = np.random.randint(1, 7)  # Кубик 2
        total = die1 + die2
        sums_count[total] += 1  # Збільшити лічильник для відповідної суми
    
    return sums_count

def calculate_probabilities(sums_count, num_rolls):
    # Обчислення ймовірностей
    probabilities = (sums_count / num_rolls) * 100  # У відсотках
    return probabilities[2:]  # Повертаємо від 2 до 12

def plot_probabilities(probabilities):
    sums = range(2, 13)
    plt.bar(sums, probabilities, color='skyblue')
    plt.xticks(sums)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.ylim(0, 20)
    plt.grid(axis='y')
    plt.show()

def create_probability_table(probabilities):
    # Створення таблиці ймовірностей
    sum_values = range(2, 13)
    probability_table = pd.DataFrame({
        'Сума': sum_values,
        'Ймовірність (%)': probabilities
    })
    return probability_table

def main():
    num_rolls = 100000  # Кількість кидків кубиків
    sums_count = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(sums_count, num_rolls)
    
    # Створення таблиці ймовірностей
    probability_table = create_probability_table(probabilities)
    print(probability_table)
    
    # Візуалізація ймовірностей
    plot_probabilities(probabilities)

    # Аналітичні ймовірності для порівняння
    analytical_probabilities = [
        2.78, 5.56, 8.33, 11.11, 13.89,
        16.67, 13.89, 11.11, 8.33, 5.56, 2.78
    ]

    print("\nПорівняння ймовірностей (Метод Монте-Карло vs Аналітичні):")
    for sum_value, monte_prob, analytical_prob in zip(range(2, 13), probabilities, analytical_probabilities):
        print(f"Сума {sum_value}: {monte_prob:.2f}% vs {analytical_prob:.2f}%")

if __name__ == "__main__":
    main()
