from pioneergame import Window, Rect, Circle

my_window = Window(1200, 700, 'my black window')  # создаём главное окно

# создание синего прямоугольника с шириной 100 и высотой 50
block = Rect(my_window, x=10, y=40, width=100, height=50, color='blue')

# создание оранжевого квадрата размером 60 на 60, который потом будем двигать
moving_square = Rect(my_window, x=100, y=200, width=60, height=60, color='orange')

# создание красного круга с радиусом 20, который тоже будем двигать
moving_circle = Circle(my_window, x=1000, y=50, radius=20, color='red')

# создание серого кольца с радиусом 80 и толщиной стенки 5
bublik = Circle(my_window, x=500, y=350, radius=80, color='grey', thickness=5)

while True:  # бесконечный цикл игры
    my_window.fill('black')  # заполнение экрана чёрным

    block.draw()  # отрисовка прямоугольника
    moving_square.draw()  # отрисовка квадрата
    moving_circle.draw()  # отрисовка круга
    bublik.draw()

    # если правая сторона квадрата находится левее чем правая граница экрана, то мы двигаем квадрат вправо
    if moving_square.right < my_window.right:
        moving_square.x += 5  # движение квадрата вправо на 1 пиксель

    moving_circle.x -= 1  # движение круга в лево
    moving_circle.y += 1  # движение круга вниз

    my_window.update(60)  # обновление экрана с частотой 60 кадров в секунду
