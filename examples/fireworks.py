from pioneergame import Window, explode, explosion_update

my_window = Window(1200, 700, 'my black window')  # создаём главное окно

while True:  # бесконечный цикл игры
    my_window.fill('black')  # заполнение экрана чёрным

    if my_window.get_mouse_button('left'):  # если была нажата левая кнопка мыши
        explode(my_window, pos=my_window.mouse_position(), size=5, color='orange')

    explosion_update()  # обработка всех взрывов

    my_window.update(60)  # обновление экрана с частотой 60 кадров в секунду
