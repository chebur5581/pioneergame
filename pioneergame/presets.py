# prestes

from .window import Window
from .rect import Rect
from .sprite import Sprite


class Map:
    """map of blocks by char map, # - meaning block"""

    def __init__(self, window: Window, char_map: list[str], sprite: Sprite, block_size=50):
        self.window = window
        self.charm_map = char_map
        self.sprite = sprite
        self.sprite.window = self.window

        self.block_size = block_size

        self.blocks = []
        for y, row in enumerate(self.charm_map):
            for x, char in enumerate(row):
                if char == "#":
                    self.blocks.append(
                        Rect(self.window, x * self.block_size, y * block_size, self.block_size, self.block_size))

    def draw(self):
        for block in self.blocks:
            self.sprite.attach_to(block)
            self.sprite.draw()


class Player(Rect):
    def __init__(self, window: Window, x: float, y: float, width: int, height: int, sprite: Sprite,
                 speed: int = 5):
        super().__init__(window, x, y, width, height)
        self.speed = speed

        self.old_sprite = sprite
        self.old_sprite.window = window
        self.old_sprite.attach_to(self)

        self.sprite = self.old_sprite  # спрайт для отрисовки, что б можно было вращать
        self.sprite.window = window

    def go(self, direction: str) -> None:
        """go("up"), go("down"), go("left") or go("right")"""

        match direction:
            case "up":
                self.sprite = self.old_sprite
                self.y -= self.speed
            case "down":
                self.sprite = self.old_sprite.get_rotated(180)
                self.y += self.speed
            case "right":
                self.sprite = self.old_sprite.get_rotated(-90)
                self.x += self.speed
            case "left":
                self.sprite = self.old_sprite.get_rotated(90)
                self.x -= self.speed

        self.sprite.attach_to(self)

    def draw(self) -> None:
        self.sprite.draw()

    def collide_map(self, block_map: Map, collision_tolerance: int = 8):
        for block in block_map.blocks:

            if not self.colliderect(block):
                continue

            collision = self.collision(block, collision_tolerance)

            match collision:
                case "top":
                    self.top = block.bottom
                case "bottom":
                    self.bottom = block.top
                case "left":
                    self.left = block.right
                case "right":
                    self.right = block.left
