simple pygame plugin for kids.



### Template. Empty window ###

```python
from pioneergame import Window

window = Window(1300, 700)  # 1300x700 window
fps = 80

while True:  # main loop
    window.fill('black')

    window.update(fps)  # update 80 times per second
```
#
### Drawing simple objects ###

```python
from pioneergame import Window, Rect, Circle

window = Window(1300, 700)
fps = 80

square = Rect(window, 10, 10, 200, 200, 'red')
rectangle = Rect(window, 700, 200, 150, 300, 'orange')
# Rect(Window, x, y, width, 'height', color)

circle = Circle(window, 800, 100, 50, 'white')
bublik = Circle(window, 500, 500, 75, 'pink', 30)
# Circle(Window, x, y, radius, color, thickness)

while True:
    window.fill('black')

    square.draw()
    rectangle.draw()

    circle.draw()
    bublik.draw()

    square.x = square.x + 1

    window.update(fps)
```
#

### Example. DVD screen ###

```python
from pioneergame import Window, Label

window = Window(1024, 768, 'DVD test')

dvd = Label(window, 10, 10, 'DVD' 'grey', font='Impact', size=70, italic=True)
state = Label(window, 10, 10, 'state: IDLE', 'grey', italic=True)
# Label(Window, x, y, text, color, size, font, italic)

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


### Ping Pong Game ###
![pong](https://media1.tenor.com/m/T3H92Qstl68AAAAC/p-ong.gif)

```python
from pioneergame import Window, Circle, Rect, Label

window = Window(1024, 768)
fps = 20

pad1 = Rect(window, 50, 20, 20, 200, color='grey')
text1 = Label(window, 10, 10, text='0', color='darkgray', size=50)
score1 = 0

pad2 = Rect(window, 954, 20, 20, 200, color='pink')
text2 = Label(window, 700, 10, color='darkgray', size=50)
score2 = 0

ball = Circle(window, 100, 100, radius=10, color='grey')
ball_speed = 3

dx = ball_speed
dy = ball_speed

while True:
    window.fill('green')

    pad1.draw()
    text1.draw()

    pad2.draw()
    text2.draw()

    ball.draw()

    ball.x += dx
    ball.y += dy

    if ball.bottom > window.bottom:
        dy = -dy
    if ball.top < window.top:
        dy = -dy

    if ball.right > window.right:
        score2 = score2 + 1
    if ball.left < window.left:
        score2 = score2 + 1

    if window.get_key('w') and pad1.top > window.top:
        pad1.y -= 5
    if window.get_key('s') and pad1.bottom < window.bottom:
        pad1.y += 5

    if window.get_key('up'):
        pad2.x -= 5
    if window.get_key('down') and pad2.bottom < window.bottom:
        pad2.x += 5

    if ball.colliderect(pad1):
        dx = ball_speed
    if ball.colliderect(pad2):
        dx = -ball_speed

    window.update(fps)
```