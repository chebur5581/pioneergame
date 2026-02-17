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
