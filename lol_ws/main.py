from champions import *
from items import *
from utils import skills

if __name__ =='__main__':
    # malpha = Malphite()
    # malpha = Tanker('malphite')
    malpha = Character('malphite')
    ahri = Character('ahri')
    garen = Character('garen')
    dod = DanceOfDeath()

    malpha.apply_item_stats(dod)
    print(garen.skills['q'])
    # print(malpha.skills['q'])
    print(malpha.get_experience(300))
    print(garen.skill_level_up('q'))
    print(garen.skill_level_up('q'))
    print(garen.skill_level_up('q'))
    print(garen.skill_level_up('q'))
    skills.Skill().use_skill_to_targets(malpha, [], 'q')
    skills.Skill().use_skill_to_targets(garen, [ahri, garen, malpha], 'q')
    # print(malpha)