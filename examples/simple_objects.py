from pioneergame import Window, Rect, Circle

window = Window(1300, 700)
fps = 80

square = Rect(window, 10, 10, 200, 200, 'red')
rectangle = Rect(window, 700, 200, 150, 300, 'orange')

circle = Circle(window, 800, 100, 50, 'white')
bublik = Circle(window, 500, 500, 75, 'pink', 30)

while True:
    window.fill('black')

    square.draw()
    rectangle.draw()

    circle.draw()
    bublik.draw()

    square.x = square.x + 1

    window.update(fps)
