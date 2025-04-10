from champions import *
from items import *

if __name__ =='__main__':
    malpha = Malphite()
    dod = DanceOfDeath()

    malpha.apply_item_stats(dod)

    print(malpha)