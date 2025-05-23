import pygame as pg


class Window:
    def __init__(self, width, height, caption=None):
        pg.init()

        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))

        self.clock = pg.time.Clock()

        self.caption = 'Pioneer Window' if caption is None else caption
        pg.display.set_caption(self.caption)

        self._mouse = ['left', 'middle', 'right']

        self.left = 0
        self.right = width
        self.top = 0
        self.bottom = height

    def get_fps(self) -> float:
        return self.clock.get_fps()

    def fill(self, color: pg.Color | tuple[int, int, int] | str | int) -> None:
        self.screen.fill(color)

    def update(self, FPS: int = 60) -> int:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()

        pg.display.flip()
        return self.clock.tick(FPS)

    def draw_rect(self, color: str | tuple[int, int, int] | tuple[int, int, int] | pg.Color,
                  rect: tuple[int, int, int, int] | pg.Rect | pg.rect.RectType, width: int = 0) -> None:
        pg.draw.rect(self.screen, color, rect, width)

    def draw_circle(self, color: str | tuple[int, int, int] | tuple[int, int, int] | pg.Color,
                    center: tuple[int, int], radius: int, width: int = 0) -> None:
        pg.draw.circle(self.screen, color, center, radius, width)

    def draw_line(self):
        ...

    def get_mouse_button(self, button: str = 'left') -> bool:
        return pg.mouse.get_pressed()[self._mouse.index(button)]

    @staticmethod
    def mouse_position() -> tuple[int, int]:
        return pg.mouse.get_pos()

    @staticmethod
    def get_key(key: str) -> bool:
        return pg.key.get_pressed()[pg.key.key_code(key)]  # Example: Check if space key is pressed

    @staticmethod
    def close() -> None:
        pg.quit()

    @staticmethod
    def set_caption(text: str) -> None:
        pg.display.set_caption(text)
