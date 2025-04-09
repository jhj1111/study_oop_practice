# 롤 인벤: https://lol.inven.co.kr/dataninfo/item/list.php
from stats import *
from utils import information

class Item(CharacterStats):
    def __init__(self, name: str=None, total_cost: int=0):
        super().__init__()
        self.name = name
        self.total_cost = total_cost    # 일시불 가격
        self.cost = total_cost  # 하위템 고려한 가격
        self.child_item: list[str] = []  # 하위 조합식
        self.parent_item: list[str] = [] # 상위 조합식

        self.init_stats_from_config()

    def init_stats_from_config(self, file_name: str='items.yaml', class_name: str=None):
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
            self.total_cost = target_data["total_cost"]
            self.cost = self.total_cost
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

    def get_current_cost(self):
        '''인벤토리 내 하위 조합식에 따른 아이템 가격'''
        for item in self.child_item:
            for item_data in self.data.get('items'):
                if item != item_data.get('name'):
                    continue
                # 하위 아이템 가격 차감
                self.cost -= item_data.get('total_cost')
                break
            else:
                return f"하위 아이템 {item_data.get('name')} 오타 혹은 가격 정보가 존재하지 않음"
        
        return self.cost

class DanceOfDeath(Item):   # 죽무
    def __init__(self, name: str='dance_of_death', total_cost: int=0):
        super().__init__(name=name)
        self.child_item: list[str] = ['pickaxe', 'steel_sigil', 'caulfield_warhammer']  # 하위 조합식
        self.parent_item: list[str] = [] # 상위 조합식

    def effect1(self):
        pass

    def effect2(self):
        pass

if __name__ == '__main__':
    dod = DanceOfDeath()
    dod1 = DanceOfDeath()
    print(dod.total_cost)
    print(dod.get_current_cost())
    print(dod1.cost)
    print(dod1.speed)