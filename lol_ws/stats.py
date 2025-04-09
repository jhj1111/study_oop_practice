# 나무위키 : https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EC%B1%94%ED%94%BC%EC%96%B8/%EB%8A%A5%EB%A0%A5%EC%B9%98
from dataclasses import dataclass, field
from utils import information

@dataclass
class LevelStats:
    level: int = 1
    experience: float = 0.0

    def experience_required_for_each_level(self):
        return 180 + 100*self.level

@dataclass
class HealthStats:
    max_health: float = 100.0
    current_health: float = 100.0
    growth_rate: float = 1.0    # 성장수치
    regeneration: float = 5.0

@dataclass
class ManaStats:
    max_mana: float = 100.0
    current_mana: float = 100.0
    growth_rate: float = 1.0    # 성장수치
    regeneration: float = 3.0

@dataclass
class AttackStats:
    attack_damage: float = 50.0
    ability_power: float = 0.0
    adaptive_force: float = 0.0
    growth_rate: float = 1.0    # 성장수치

@dataclass
class DefenseStats:
    armor: float = 30.0
    magic_resistance: float = 30.0
    armor_growth_rate: float = 1.0    # 방어력 성장수치
    magic_resistance_growth_rate: float = 1.0    # 마방 성장수치

@dataclass
class SpeedStats:
    attack_speed: float = 0.7
    ability_haste: float = 0.0
    movement_speed: float = 325.0
    attack_speed_growth_rate: float = 0.0

@dataclass
class CriticalStats:
    crit_chance: float = 0.0
    crit_damage: float = 175.0  # 기본 치명타 피해량

@dataclass
class PenetrationStats:
    armor_penetration: float = 0.0
    magic_penetration: float = 0.0

@dataclass
class VampStats:    # 흡혈
    life_steal: float = 0.0 # 생명력 흡수
    physical_vamp: float = 0.0  # 물리 피해 흡혈
    omnivamp: float = 0.0   # 모든 피해 흡혈
    spell_vamp: float = 0.0# 주문 흡혈

@dataclass
class ResourceStats:
    health: HealthStats = field(default_factory=HealthStats)
    mana: ManaStats = field(default_factory=ManaStats)
    attack: AttackStats = field(default=AttackStats)
    defense: DefenseStats = field(default_factory=DefenseStats)
    other_resource: float = 0.0
    resource_type: str = "mana"  # 혹은 "none", "energy", "fury" 등
    has_resource: bool = True

@dataclass
class OtherStats:
    range: float = 550.0    # 사거리
    tenacity: float = 0.0   # 강인함
    heal_and_shield_power: float = 0.0  # 회복 및 보호막 효과

@dataclass
class CharacterStats:
    level: LevelStats = field(default_factory=LevelStats)
    health: HealthStats = field(default_factory=HealthStats)
    mana: ManaStats = field(default_factory=ManaStats)
    attack: AttackStats = field(default=AttackStats)
    defense: DefenseStats = field(default_factory=DefenseStats)
    speed: SpeedStats = field(default_factory=SpeedStats)
    critical: CriticalStats = field(default_factory=CriticalStats)
    penetration: PenetrationStats = field(default_factory=PenetrationStats)
    vamp: VampStats = field(default_factory=VampStats)
    other: OtherStats = field(default_factory=OtherStats)

    def init_stats_from_config(self, file_name: str, class_name: str=None):
        self.data = information.ConfigLoader().load_file_info(file_name)
        class_name = file_name.split('.')[0] if class_name is None else class_name
        for target_data in self.data.get(class_name):
            try :
                name_data = target_data['name']
            except KeyError:
                print("정보 없음")

            if name_data != self.name:
                continue
            # 데이터 일치 시
            self.health = HealthStats(**target_data["health_stats"])
            self.mana = ManaStats(**target_data.get("mana_stats", {}))
            self.attack = AttackStats(**target_data["attack_stats"])
            self.defense = DefenseStats(**target_data.get("defense_stats", {}))
            self.speed = SpeedStats(**target_data["speed_stats"])
            self.critical = SpeedStats(**target_data["speed_stats"])
            self.penetration = PenetrationStats(**target_data["penetration_stats"])
            self.vamp = VampStats(**target_data["vamp_stats"])
            self.other = OtherStats(**target_data["other_stats"])
            break
        else: 
            print('정보 없음. 혹은 오타 확인')

    def experience_required_for_each_level(self, level:int =None):
        level = level if None else self.level_stats.level
        return 180 + 100*level

if __name__ == '__main__':
    levelstats = LevelStats(8, 99)
    level = LevelStats(experience=100)
    leesin = CharacterStats(level=8, experience=100)

    print(leesin)
    print(leesin.experience_required_for_each_level())