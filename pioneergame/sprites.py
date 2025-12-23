# presets

from .sprite import Sprite
from pkg_resources import resource_filename

green_tank = Sprite(None, resource_filename('pioneergame', 'res/green_tank.png'))

yellow_tank = Sprite(None, resource_filename('pioneergame', 'res/yellow_tank.png'))

brick_sprte = Sprite(None, resource_filename('pioneergame', 'res/brick.png'))
