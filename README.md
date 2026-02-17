Простая обёртка pygame для детей

### Blank. Empty window ###

```python
from pioneergame import Window

my_window = Window(1200, 700, 'my black window')  # создаём главное окно

while True:  # бесконечный цикл игры
    my_window.fill('black')  # заполнение экрана чёрным

    my_window.update(60)  # обновление экрана с частотой 60 кадров в секунду
```

#

### Drawing simple objects ###
![figures](https://github.com/chebur5581/pioneergame/blob/main/image/figures.png?raw=true)
```python
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

```

#

### Keyboard and text ###
![keyboard](https://github.com/chebur5581/pioneergame/blob/main/image/keyboard_and_text.png?raw=true)
```python
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
```

### Fireworks ###
![fireworks](https://github.com/chebur5581/pioneergame/blob/main/image/fireworks.png?raw=true)
```python
from pioneergame import Window, explode, explosion_update

my_window = Window(1200, 700, 'my black window')  # создаём главное окно

while True:  # бесконечный цикл игры
    my_window.fill('black')  # заполнение экрана чёрным

    if my_window.get_mouse_button('left'):  # если была нажата левая кнопка мыши
        explode(my_window, pos=my_window.mouse_position(), size=5, color='orange')

    explosion_update()  # обработка всех взрывов

    my_window.update(60)  # обновление экрана с частотой 60 кадров в секунду
```

### Example. DVD screen ###
![dvd](https://github.com/chebur5581/pioneergame/blob/main/image/DVD.png?raw=true)
```python
from pioneergame import Window, Label

window = Window(1024, 768, 'DVD test')

dvd = Label(window, 10, 10, 'DVD', 'grey', font='Impact', size=70, italic=True)
state = Label(window, 10, 10, 'state: IDLE', 'grey', italic=True)

dx, dy = 3, 3

while True:
    window.fill('black')
    dvd.draw()
    state.draw()

    dvd.x += dx
    dvd.y += dy

    if dvd.left < window.left or dvd.right > window.right:
        dx *= -1
    if dvd.top < window.top or dvd.bottom > window.bottom:
        dy *= -1

    window.update(80)
```

#

### Ping Pong ###

![pong](https://github.com/chebur5581/pioneergame/blob/main/image/pong.png?raw=true)
```python
from pioneergame import Window, Circle, Rect, Label

window = Window(1024, 768)
fps = 80

pad1 = Rect(window, 50, 20, 20, 200, color='grey')
text1 = Label(window, 100, 10, text='0', color='darkgray', size=50)
score1 = 0

pad2 = Rect(window, 954, 20, 20, 200, color='grey')
text2 = Label(window, 900, 10, color='darkgray', size=50)
score2 = 0

ball = Circle(window, 100, 100, radius=10, color='grey')
ball_speed = 3

dx = ball_speed
dy = ball_speed

while True:
    window.fill('black')

    pad1.draw()
    text1.draw()
    text1.set_text(score1)

    pad2.draw()
    text2.draw()
    text2.set_text(score2)

    ball.draw()

    ball.x += dx
    ball.y += dy

    if ball.bottom > window.bottom:
        dy = -dy
    if ball.top < window.top:
        dy = -dy

    if ball.right > window.right:
        score1 = score1 + 1
        ball.x = 512
        ball.y = 344
    if ball.left < window.left:
        score2 = score2 + 1
        ball.x = 512
        ball.y = 344

    if window.get_key('w') and pad1.top > window.top:
        pad1.y -= 5
    if window.get_key('s') and pad1.bottom < window.bottom:
        pad1.y += 5

    if window.get_key('up') and pad2.top > window.top:
        pad2.y -= 5
    if window.get_key('down') and pad2.bottom < window.bottom:
        pad2.y += 5

    if ball.colliderect(pad1):
        dx = ball_speed
    if ball.colliderect(pad2):
        dx = -ball_speed

    window.update(fps)
```

### BattleCity ###

![pong](https://github.com/chebur5581/pioneergame/blob/main/image/BattleCity.png?raw=true)
```python
from pioneergame import Window, Label
from pioneergame.presets import Player, Map
from pioneergame.sprites import green_tank, yellow_tank, brick_sprite, bush_sprite, metal_sprite

window = Window(1050, 900)
fps = 80

player1 = Player(window, 500, 800, 50, 50, green_tank)


player2 = Player(window, 500, 45, 50, 50, yellow_tank)

game_over_text = Label(window, 0, 0, 'Player0 WIN!', 'red', size=50)
game_over_text.center = window.center

# W - unbreakable wall
# $ - bush
# # - brick
# @ - metal block (unbreakable)
charmap = ['WWWWWWWWWWWWWWWWWWWWW',
           'W.......$@.@$.......W',
           'W.$$.....$.$.....$$.W',
           'W.##..$$.....$$..##.W',
           'W.##..##.#.#.##..##.W',
           'W.###.##.....##.###.W',
           'W.##..##.....##..##.W',
           'W$.......#.#.......$W',
           'W@$.$@$$.#@#.$$@$.$@W',
           'W$.......#.#.......$W',
           'W.##..##.....##..##.W',
           'W.##.###.....###.##.W',
           'W.##..##.#.#.##..##.W',
           'W.##..##.....##..##.W',
           'W.##..$$.....$$..##.W',
           'W.$$.....$.$.....$$.W',
           'W.......$@.@$.......W',
           'WWWWWWWWWWWWWWWWWWWWW']

map = Map(window, charmap, brick_sprite, metal_sprite, bush_sprite)

while True:
    window.fill('black')

    player1.draw()
    player1.collide_map(map)
    player1.collide_player(player2)

    player2.draw()
    player2.collide_map(map)
    player2.collide_player(player1)

    map.draw()

    if player1.hp <= 0:
        game_over_text.set_text('Player2 WIN!')
        game_over_text.draw_box()
        game_over_text.draw()
    if player2.hp <= 0:
        game_over_text.set_text('Player1 WIN!')
        game_over_text.draw_box()
        game_over_text.draw()

    if player1.hp > 0:
        if window.get_key('w'):
            player1.go('up')
        elif window.get_key('s'):
            player1.go('down')
        elif window.get_key('a'):
            player1.go('left')
        elif window.get_key('d'):
            player1.go('right')

        if window.get_key('space'):
            player1.shoot()

    if player2.hp > 0:
        if window.get_key('up'):
            player2.go('up')
        elif window.get_key('down'):
            player2.go('down')
        elif window.get_key('left'):
            player2.go('left')
        elif window.get_key('right'):
            player2.go('right')

        if window.get_key('right shift'):
            player2.shoot()

    window.update(fps)
```