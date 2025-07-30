from pioneergame import Window, Label

my_window = Window(1200, 700, 'my black window')  # создаём главное окно

# создание текста белого цвета
my_text = Label(my_window, x=300, y=350, text='Нажми стрелочку вправо, влево, вверх или вниз', color='white')

while True:  # бесконечный цикл игры
    my_window.fill('black')  # заполнение экрана чёрным

    my_text.draw()  # отрисовка текста

    if my_window.get_key('left'):  # если нажата стрелочка влево
        my_text.set_text('была нажата стрелочка влево')  # установка нового текста
    if my_window.get_key('right'):  # если нажата стрелочка вправо
        my_text.set_text('была нажата стрелочка вправо')
    if my_window.get_key('up'):  # если нажата стрелочка вверх
        my_text.set_text('была нажата стрелочка вверх')
    if my_window.get_key('down'):  # если нажата стрелочка вниз
        my_text.set_text('была нажата стрелочка вниз')

    my_window.update(60)  # обновление экрана с частотой 60 кадров в секунду
