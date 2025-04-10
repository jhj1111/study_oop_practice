# 롤 인벤: https://lol.inven.co.kr/dataninfo/champion/
from character import Fighter, Mage, Tanker, Character

class Malphite(Tanker):
    def __init__(self, name='malphite'):
        super().__init__(name=name)
        self.name = name

    def passive(self):
        name = '화강암 방패 (Granite Shield)'
        pass

    def q_skill(self):
        name = '지진의 파편 (Seismic Shard)'
        pass

    def w_skill(self):
        name = '천둥소리 (Thunderclap)'
        pass

    def e_skill(self):
        name = '지면 강타 (Ground Slam)'
        pass

    def r_skill(self):
        name = '멈출 수 없는 힘 (Unstoppable Force)'
        pass

if __name__ == '__main__':
    champ = Malphite()
    print(f"name = {champ.name}")
    print(f"{champ.name}'s attack damage = {champ.attack.attack_damage}")
    print(f"{champ.name}'s class = {champ.class_group}")