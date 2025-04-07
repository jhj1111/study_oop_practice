from dataclasses import dataclass, field

@dataclass
class LevelStats:
    level: int = 1
    experience: float = 0.0

@dataclass
class HealthStats:
    max_health: float = 100.0
    current_health: float = 100.0
    regeneration: float = 5.0

@dataclass
class ManaStats:
    max_mana: float = 100.0
    current_mana: float = 100.0
    regeneration: float = 3.0

@dataclass
class ResourceStats:
    health: HealthStats = field(default_factory=HealthStats)
    mana: ManaStats = field(default_factory=ManaStats)
    other_resource: float = 0.0
    resource_type: str = "mana"  # 혹은 "none", "energy", "fury" 등
    has_resource: bool = True

@dataclass
class AttackStats:
    attack_damage: float = 50.0
    ability_power: float = 0.0
    adaptive_force: float = 0.0

@dataclass
class DefenseStats:
    armor: float = 30.0
    magic_resistance: float = 30.0

@dataclass
class SpeedStats:
    attack_speed: float = 0.7
    ability_haste: float = 0.0
    movement_speed: float = 325.0

@dataclass
class CriticalStats:
    crit_chance: float = 0.0
    crit_damage: float = 175.0  # 기본 치명타 피해량

@dataclass
class PenetrationStats:
    armor_penetration: float = 0.0
    magic_penetration: float = 0.0

@dataclass
class VampStats:
    life_steal: float = 0.0
    physical_vamp: float = 0.0
    omnivamp: float = 0.0
    spell_vamp: float = 0.0

@dataclass
class OtherStats:
    range: float = 550.0
    tenacity: float = 0.0
    heal_and_shield_power: float = 0.0

@dataclass
class CharacterStats:
    level_stats: LevelStats = field(default_factory=LevelStats)
    resource_stats: ResourceStats = field(default_factory=ResourceStats)
    attack_stats: AttackStats = field(default_factory=AttackStats)
    defense_stats: DefenseStats = field(default_factory=DefenseStats)
    speed_stats: SpeedStats = field(default_factory=SpeedStats)
    critical_stats: CriticalStats = field(default_factory=CriticalStats)
    penetration_stats: PenetrationStats = field(default_factory=PenetrationStats)
    vamp_stats: VampStats = field(default_factory=VampStats)
    other_stats: OtherStats = field(default_factory=OtherStats)

if __name__ == '__main__':
    levelstats = LevelStats(8, 99)
    level = LevelStats(experience=100)
    leesin = CharacterStats(level_stats=levelstats)

    print(leesin)