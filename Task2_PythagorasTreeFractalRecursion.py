import turtle

def draw_branch(branch_length, level):
    if level > 0:
        # Малюємо основну гілку
        turtle.forward(branch_length)
        # Поворот вліво та малювання лівої гілки
        turtle.left(30)
        draw_branch(branch_length * 0.7, level - 1)
        # Поворот вправо для малювання правої гілки
        turtle.right(60)
        draw_branch(branch_length * 0.7, level - 1)
        # Повертаємося назад
        turtle.left(30)
        turtle.backward(branch_length)

def main():
    # Запитуємо у користувача рівень рекурсії
    level = int(input("Введіть рівень рекурсії (1-7): "))
    
    # Налаштування вікна
    turtle.bgcolor("white")
    turtle.speed(0)  # Найшвидший режим малювання
    turtle.left(90)  # Починаємо з вертикального положення
    turtle.penup()
    turtle.backward(100)  # Зміщуємо на початку вниз
    turtle.pendown()
    turtle.pensize(2)

    # Малюємо дерево з початковою довжиною гілки 100
    draw_branch(100, level)

    # Завершення малювання
    turtle.done()

if __name__ == "__main__":
    main()
