from champions import *
from items import *

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
    # print(malpha.use_skill_to_targets([], 'q'))
    print(malpha.use_skill_to_targets([ahri, garen], 'q'))
    print(malpha.get_experience(300))
    print(malpha.skill_level_up('q'))
    print(malpha.use_skill_to_targets([ahri, garen], 'q'))
    # print(malpha)