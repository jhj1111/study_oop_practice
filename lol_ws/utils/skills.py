
class Skill:
    def calculate_damage(self, caster, target, skill_key: str) -> tuple:
        """
        간단화된 데미지 계산 공식
        - 계수: ad, ap, armor, hp
        - damage_type: "ad" or "ap"
        - 반환: (최종 피해량, (기본, ad, ap, armor, hp))
        """
        skill = caster.skills[skill_key]
        level = skill["level"]

        if level <= 0:
            return 0, (0, 0, 0, 0, 0)

        base = skill["base_damage"][level - 1]
        ad_dmg = skill.get("ad_ratio", 0) * caster.attack.attack_damage
        ap_dmg = skill.get("ap_ratio", 0) * caster.attack.ability_power
        armor_dmg = skill.get("armor_ratio", 0) * caster.defense.armor
        hp_dmg = skill.get("hp_ratio", 0) * caster.health.max_health

        total_raw_damage = base + ad_dmg + ap_dmg + armor_dmg + hp_dmg

        # 간단한 타입 기반 방어 적용
        damage_type = skill.get("damage_type", "ap")

        if damage_type == "ad":
            resist = target.defense.armor
            pen = caster.penetration.armor_penetration
        elif damage_type == "ap":
            resist = target.defense.magic_resistance
            pen = caster.penetration.magic_penetration
        else:  # 잘못된 입력이 들어오면 기본으로
            resist = 0
            pen = 0

        # 피해량 감소 계산
        effective_resist = max(resist - pen, 0) # 양수만 고려
        if effective_resist >= 0:
            multiplier = 100 / (100 + effective_resist)
        else:
            multiplier = 2 - (100 / (100 - effective_resist))  

        final_damage = total_raw_damage * multiplier

        return final_damage, (base, ad_dmg, ap_dmg, armor_dmg, hp_dmg)
    
    def use_skill_to_targets(self, caster, targets: list, skill_key: str):
        '''
        caster: 스킬 시전자
        targets: 목표 챔피언 클래스
        skill_key: q,w,e,r
        '''
        if not len(targets):
            return print(f"{caster.name}의 {caster.skills[skill_key]['name']} 스킬 빗나감")
            
        for target in targets:
            damage, _ = self.calculate_damage(caster, target, skill_key)
            target.health.current_health -= damage
            print(f"{caster.name}가 {target.name}에게 {caster.skills[skill_key]['name']} 사용 → {damage:.2f} 피해!")
