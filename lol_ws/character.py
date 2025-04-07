# 나무위키 : https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EC%B1%94%ED%94%BC%EC%96%B8/%EC%97%AD%ED%95%A0%EA%B5%B0
from stats import *

class Character(CharacterStats):
    def __init__(self):
        super().__init__()

    def healing_hp(self, hp_regeneration:float = None):
        hp_regeneration = hp_regeneration if hp_regeneration is None else self.health.regeneration
        self.health.current_health += hp_regeneration

    def healing_mp(self, mp_regeneration:float = None):
        mp_regeneration = mp_regeneration if mp_regeneration is None else self.mana.regeneration
        self.mana.regeneration += mp_regeneration

class Fighter(Character):
    def __init__(self):
        super().__init__()

class Mage(Character):
    def __init__(self):
        super().__init__()
