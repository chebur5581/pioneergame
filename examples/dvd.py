from pioneergame import Window, Label

window = Window(1024, 768, 'DVD test')

dvd = Label(window, 10, 10, 'grey', 'DVD', font='Impact', size=70, italic=True)
state = Label(window, 10, 10, 'grey', 'state: IDLE', italic=True)

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
