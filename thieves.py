# thieves module

import random

from attributes import Agile, Sneaky
from characters import Character

# Method Resolution Order (MRO)
class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))