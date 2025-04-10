
class Skill:
    def calculate_damage(self, caster, skill_key: str) -> float:
        """
        caster: 스킬 시전자
        skill_key: q,w,e,r
        """
        skill = caster.skills[skill_key]
        level = skill["level"]
        base = skill["base_damage"][level - 1] if level > 0 else 0

        bonus = 0
        if "ap_ratio" in skill:
            bonus += skill["ap_ratio"] * caster.attack.ability_power
        if "armor_ratio" in skill:
            bonus += skill["armor_ratio"] * caster.defense.armor

        return base + bonus
    
