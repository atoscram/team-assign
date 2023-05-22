from enum import Enum

class Positions(Enum):
    SETTER = 1
    OUTSIDE = 2
    MIDDLE = 3
    OPPOSITE = 4
    LIBERO = 5


class Player:
    def __init__(self, name, position, level):
        self._name = name
        self._position = position
        self._level = level

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def player_profile(self):
        return {self.name: [self.position, self.level]}