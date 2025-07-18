from pioneergame import Window

window = Window(width=1500, height=700)
fps = 80

while True:
    window.fill('orange')

    window.update(fps)
