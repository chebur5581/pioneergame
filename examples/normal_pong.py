from pioneergame.pioneergame import Window, Circle, Rect, Label

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
