from pioneergame import Window

window = Window(1300, 700)
fps = 80

while True:
    window.fill('black')

    window.update(fps)
