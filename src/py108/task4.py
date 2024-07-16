# TODO("Delete this 'TODO' and create your class here")
class Hero:

    def __init__(self):
        self._health  = 10
        self._level = 0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    def sick(self):
        self._health -= 1

    def heal(self):
        self._health += 1

    def attack(self):
        self._level += 1
