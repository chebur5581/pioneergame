Ïðîñòàÿ îá¸ðòêà pygame äëÿ äåòåé

### Blank. Empty window ###

```python
from pioneergame import Window

my_window = Window(1200, 700, 'my black window')  # ñîçäà¸ì ãëàâíîå îêíî

while True:  # áåñêîíå÷íûé öèêë èãðû
    my_window.fill('black')  # çàïîëíåíèå ýêðàíà ÷¸ðíûì

    my_window.update(60)  # îáíîâëåíèå ýêðàíà ñ ÷àñòîòîé 60 êàäðîâ â ñåêóíäó
```

# Readme

### Drawing simple objects ###
![figures](https://github.com/chebur5581/pioneergame/blob/main/image/figures.png?raw=true)
```python
from pioneergame import Window, Rect, Circle

my_window = Window(1200, 700, 'my black window')  # ñîçäà¸ì ãëàâíîå îêíî

# ñîçäàíèå ñèíåãî ïðÿìîóãîëüíèêà ñ øèðèíîé 100 è âûñîòîé 50
block = Rect(my_window, x=10, y=40, width=100, height=50, color='blue')

# ñîçäàíèå îðàíæåâîãî êâàäðàòà ðàçìåðîì 60 íà 60, êîòîðûé ïîòîì áóäåì äâèãàòü
moving_square = Rect(my_window, x=100, y=200, width=60, height=60, color='orange')

# ñîçäàíèå êðàñíîãî êðóãà ñ ðàäèóñîì 20, êîòîðûé òîæå áóäåì äâèãàòü
moving_circle = Circle(my_window, x=1000, y=50, radius=20, color='red')

# ñîçäàíèå ñåðîãî êîëüöà ñ ðàäèóñîì 80 è òîëùèíîé ñòåíêè 5
bublik = Circle(my_window, x=500, y=350, radius=80, color='grey', thickness=5)

while True:  # áåñêîíå÷íûé öèêë èãðû
    my_window.fill('black')  # çàïîëíåíèå ýêðàíà ÷¸ðíûì

    block.draw()  # îòðèñîâêà ïðÿìîóãîëüíèêà
    moving_square.draw()  # îòðèñîâêà êâàäðàòà
    moving_circle.draw()  # îòðèñîâêà êðóãà
    bublik.draw()

    # åñëè ïðàâàÿ ñòîðîíà êâàäðàòà íàõîäèòñÿ ëåâåå ÷åì ïðàâàÿ ãðàíèöà ýêðàíà, òî ìû äâèãàåì êâàäðàò âïðàâî
    if moving_square.right < my_window.right:
        moving_square.x += 5  # äâèæåíèå êâàäðàòà âïðàâî íà 1 ïèêñåëü

    moving_circle.x -= 1  # äâèæåíèå êðóãà â ëåâî
    moving_circle.y += 1  # äâèæåíèå êðóãà âíèç

    my_window.update(60)  # îáíîâëåíèå ýêðàíà ñ ÷àñòîòîé 60 êàäðîâ â ñåêóíäó

```

#

### Keyboard and text ###
![keyboard](https://github.com/chebur5581/pioneergame/blob/main/image/keyboard_and_text.png?raw=true)
```python
from pioneergame import Window, Label

my_window = Window(1200, 700, 'my black window')  # ñîçäà¸ì ãëàâíîå îêíî

# ñîçäàíèå òåêñòà áåëîãî öâåòà
my_text = Label(my_window, x=300, y=350, text='Íàæìè ñòðåëî÷êó âïðàâî, âëåâî, ââåðõ èëè âíèç', color='white')

while True:  # áåñêîíå÷íûé öèêë èãðû
    my_window.fill('black')  # çàïîëíåíèå ýêðàíà ÷¸ðíûì

    my_text.draw()  # îòðèñîâêà òåêñòà

    if my_window.get_key('left'):  # åñëè íàæàòà ñòðåëî÷êà âëåâî
        my_text.set_text('áûëà íàæàòà ñòðåëî÷êà âëåâî')  # óñòàíîâêà íîâîãî òåêñòà
    if my_window.get_key('right'):  # åñëè íàæàòà ñòðåëî÷êà âïðàâî
        my_text.set_text('áûëà íàæàòà ñòðåëî÷êà âïðàâî')
    if my_window.get_key('up'):  # åñëè íàæàòà ñòðåëî÷êà ââåðõ
        my_text.set_text('áûëà íàæàòà ñòðåëî÷êà ââåðõ')
    if my_window.get_key('down'):  # åñëè íàæàòà ñòðåëî÷êà âíèç
        my_text.set_text('áûëà íàæàòà ñòðåëî÷êà âíèç')

    my_window.update(60)  # îáíîâëåíèå ýêðàíà ñ ÷àñòîòîé 60 êàäðîâ â ñåêóíäó
```

### Fireworks ###
![fireworks](https://github.com/chebur5581/pioneergame/blob/main/image/fireworks.png?raw=true)
```python
from pioneergame import Window, explode, explosion_update

my_window = Window(1200, 700, 'my black window')  # ñîçäà¸ì ãëàâíîå îêíî

while True:  # áåñêîíå÷íûé öèêë èãðû
    my_window.fill('black')  # çàïîëíåíèå ýêðàíà ÷¸ðíûì

    if my_window.get_mouse_button('left'):  # åñëè áûëà íàæàòà ëåâàÿ êíîïêà ìûøè
        explode(my_window, pos=my_window.mouse_position(), size=5, color='orange')

    explosion_update()  # îáðàáîòêà âñåõ âçðûâîâ

    my_window.update(60)  # îáíîâëåíèå ýêðàíà ñ ÷àñòîòîé 60 êàäðîâ â ñåêóíäó
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
