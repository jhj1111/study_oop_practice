# 나무위키 : https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EC%B1%94%ED%94%BC%EC%96%B8/%EC%97%AD%ED%95%A0%EA%B5%B0
from stats import *
from utils import information, skills
from items import Item

class Character(CharacterStats):
    def __init__(self, name: str=None):
        super().__init__()
        self.name = name    # 챔피언 이름
        self.init_stats_from_config('character.yaml', 'champions')
        self.init_skills_from_config()

    def init_skills_from_config(self, file_path: str='character.yaml'):
        self.skills = {}  # 스킬 저장소

        data = information.ConfigLoader().load_file_info(file_path)['champions']

        for champ_data in data:
            if champ_data['name'].lower() == self.name.lower():
                try:
                    skill_data = champ_data['skills']
                except KeyError:
                    print(f'{self.name}의 스킬 정보 없음')

                for key, values in skill_data.items():
                    self.skills[key] = {
                        "name": values.get("name", ""),
                        "level": 0,
                        "base_damage": values.get("base_damage", []),
                        "ad_ratio": values.get("ad_ratio", 0.0),
                        "ap_ratio": values.get("ap_ratio", 0.0),
                        "hp_ratio": values.get("hp_ratio", 0.0),
                        "armor_ratio": values.get("armor_ratio", 0.0),
                    }

    def apply_item_stats(self, item: 'Item'):
        """Item 객체의 모든 스탯을 현재 캐릭터에 더한다"""
        stat_categories = [
            "health", "mana", "attack", "defense", "speed",
            "critical", "penetration", "vamp", "other"
        ]

        for category in stat_categories:
            if not hasattr(self, category) or not hasattr(item, category):
                continue
            
            target_stat = getattr(self, category)
            item_stat = getattr(item, category)

            for field_name in vars(target_stat):
                item_value = getattr(item_stat, field_name, 0)
                if not isinstance(item_value, (int, float)):
                    continue
                current_value = getattr(target_stat, field_name, 0)
                setattr(target_stat, field_name, current_value + item_value)

    def get_experience(self, get_experience: float, max_level: int=18):
        '''경험치 획득'''
        if self.level.level == max_level:
            return
        new_exp = self.level.experience + get_experience
        max_exp = self.level.experience_required_for_each_level()
        if new_exp < max_exp:
            self.level.experience = new_exp
            return f"현재 레벨 {self.level.level}, 획득 경험치 {get_experience}, 현재 경험치 {self.level.experience}"
        # 레벨 업
        self.level.level += 1
        self.level.experience -= new_exp - max_exp
        # 성장 스탯
        self.health.max_health += self.health.growth_rate
        self.mana.max_mana += self.mana.growth_rate
        self.attack.attack_damage += self.attack.growth_rate
        self.defense.armor += self.defense.armor_growth_rate
        self.defense.magic_resistance += self.defense.magic_resistance_growth_rate
        self.speed.attack_speed += self.speed.attack_speed_growth_rate
        
        return f"{self.name} 레벨업 -> {self.level.level}, 경험치 {self.level.experience}"
    
    def skill_level_up(self, skill_key: str):
        '''레벨 업 skill_key: q,w,e,r'''
        self.skills[skill_key]['level'] += 1
        return f"{self.name}의 {skill_key} 레벨 -> {self.skills[skill_key]['level']}"
    
    # def use_skill_to_targets(self, targets: list, skill_key: str):
    #     '''
    #     targets: 목표 챔피언 클래스
    #     skill_key: q,w,e,r
    #     '''
    #     list_of_target_names = []
    #     damage = skills.Skill().calculate_damage(self, skill_key)

    #     for target in targets:
    #         target.health.current_health -= damage
    #         list_of_target_names.append(target.name)
    #     else:
    #         return f"{self.name}가 {list_of_target_names}에게 {self.skills[skill_key]['name']} 사용 → {damage:.2f} 피해!"

    #     return f"{self.name}의 {self.skills[skill_key]['name']} 스킬 빗나감"

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

    # def __repr__(self):
    #     return f"{self.class_group} class"

if __name__ == '__main__':
    leesin = Fighter('leesin')
    print(f"name = {leesin.name}")
    print(f"leesin's class is {leesin.class_group}")
    print(f"leesin's current hp is {leesin.health.current_health}")
    leesin.healing_hp()
    print(f"leesin's hp after healing = {leesin.health.current_health}")
    print(repr(leesin))
    print(leesin.critical.crit_chance)