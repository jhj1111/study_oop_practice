# 나무위키 : https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EC%B1%94%ED%94%BC%EC%96%B8/%EC%97%AD%ED%95%A0%EA%B5%B0
from stats import *
import json, yaml, os

# 현재 파이썬 파일 위치 기준으로 상대 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config")

class Character(CharacterStats):
    def __init__(self, name: str=None):
        super().__init__()
        self.name = name    # 챔피언 이름

        data = self.load_champion_stats()
        for champ_data in data.get('champions', []):
            name_data = champ_data.get('name')
            if name_data != self.name:
                continue
            # 데이터 일시 시
            self.health = HealthStats(**champ_data["health_stats"])
            self.mana = ManaStats(**champ_data.get("mana_stats", {}))
            self.attack = AttackStats(**champ_data["attack_stats"])
            self.defense = DefenseStats(**champ_data.get("defense_stats", {}))
            self.speed = SpeedStats(**champ_data["speed_stats"])
            break
        else: 
            print('정보 없음. 혹은 오타 확인')

    def load_champion_stats(self, filepath: str=os.path.join(CONFIG_PATH, 'character.yaml')) -> list:
        if filepath.endswith('.json'):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        else:
            raise ValueError("지원하지 않는 파일 형식입니다.")
        
        return data

    def healing_hp(self, hp_regeneration:float = None):
        current_health = self.health.current_health
        max_hp = self.health.max_health

        # set hp_regeneration
        hp_regeneration = hp_regeneration if hp_regeneration is not None else self.health.regeneration
        current_health += hp_regeneration
        # 최대체력 초과시 최대체력으로 조정
        current_health = current_health if current_health <= max_hp else max_hp
        # 대입
        self.health.current_health = current_health

    def healing_mp(self, mp_regeneration:float = None):
        current_mp = self.mana.current_mana
        max_mp = self.mana.max_mana

        # set hp_regeneration
        mp_regeneration = mp_regeneration if mp_regeneration is not None else self.mana.regeneration
        current_mp += mp_regeneration
        # 최대체력 초과시 최대체력으로 조정
        current_mp = current_mp if current_mp <= max_mp else max_mp
        # 대입
        self.mana.current_mana = current_mp

class Fighter(Character):
    def __init__(self, name: str=None, class_group: str='fighter'):
        super().__init__(name=name)
        self.name = name
        self.class_group = class_group
    
    def __repr__(self):
        return f"{self.class_group} class"

class Mage(Character):
    def __init__(self, name: str=None, class_group: str='mage'):
        super().__init__(name=name)
        self.name = name
        self.class_group = class_group

    def __repr__(self):
        return f"{self.class_group} class"
    
class Tanker(Character):
    def __init__(self, name: str=None, class_group: str='tanker'):
        super().__init__(name=name)
        self.name = name
        self.class_group = class_group

    def __repr__(self):
        return f"{self.class_group} class"

if __name__ == '__main__':
    leesin = Fighter('leesin')
    print(f"name = {leesin.name}")
    print(f"leesin's class is {leesin.class_group}")
    print(f"leesin's current hp is {leesin.health.current_health}")
    leesin.healing_hp()
    print(f"leesin's hp after healing = {leesin.health.current_health}")
    print(repr(leesin))
    print(leesin.crit_chance)