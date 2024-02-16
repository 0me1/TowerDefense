import os
import time

turn = 0
enemy_base_cord = (5,16)
player_base_cord = (17, 14)
enemy_ingame = [1]

class Enemy:
    def __init__(self, hp, cord=None):
        self.cord = cord
        self.hp = hp


class Tower:
    def __init__(self, damage, range, speed, cord) -> None:
        self.damage = damage
        self.range = range
        self.speed = speed
        self.cord = cord

def generate_map(x_size=32, y_size=16, pattern=None, road='[ ]', enemy_base='(*)', player_base='{*}'):
    map_dict = {}
    road_pattern = []
    road_left = road[0]
    road_right = road[2]
    road_center = road[1]
    enemy_base_left = enemy_base[0]
    enemy_base_center = enemy_base[1]
    enemy_base_right = enemy_base[2]
    player_base_left = player_base[0]
    player_base_center = player_base[1]
    player_base_right = player_base[2]

    for y in reversed(range(y_size)):
        map_dict[y+1] = ['o']*x_size
    if pattern == None:
        pass
    elif pattern == 1:
        road_pattern = [ # (x, y) road center
            (5, 15), (5, 14), (5, 13), (5, 12), (5, 11),
            (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), 
            (5, 5), (8, 5), (11, 5), (14, 5), (17, 5), (17, 6), (17, 7),
            (17, 8), (17, 9), (17, 10), (17, 11), (17, 12),
            (17, 13)
        ]
        # Рисует дорогу
        for i in road_pattern:
            cord = i
            x = cord[0]
            y = cord[1]
            line = map_dict[y]
            line[x] = road_center
            line[x-1] = road_left
            line[x+1] = road_right
        
        enemy_base_cord = (5,16)
        player_base_cord = (17, 14)
        # Прорисовка базы врагов
        line = map_dict[enemy_base_cord[1]]
        line[enemy_base_cord[0]] = enemy_base_center
        line[enemy_base_cord[0]-1] = enemy_base_left
        line[enemy_base_cord[0]+1] = enemy_base_right
        # Прорисовка базы игрока
        line = map_dict[player_base_cord[1]]
        line[player_base_cord[0]] = player_base_center
        line[player_base_cord[0]-1] = player_base_left
        line[player_base_cord[0]+1] = player_base_right


    return map_dict

def create_enemy(count_enemy):
    """Создает словарь врагов"""
    enemy_count = count_enemy
    enemy_dict = {}
    for i in range(enemy_count):
        enem = Enemy(hp=5)
        enemy_dict[i] = enem
    return enemy_dict

def normalize(dict):
    """Смешает все значения влево"""
    for i in range(len(dict)):
        if i+2 == len(dict):
                del dict[i+1]
        else:
            dict[i] = dict[i+1]
    return dict

def spawn_enemy(enemy_base_cord, map_dict, enemy_dict):
    """Рисует врагов на карте"""
    line = map_dict[enemy_base_cord[1]]
    cord = line[enemy_base_cord[0]]
    if cord in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']: # Проверка не стоит ли на базе уже враг
        print("ENEMY ALREADY HERE")
        pass
    elif cord not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        enemy = enemy_dict.pop(0)
        enemy_ingame.append(enemy)
        enemy = enemy.hp
        enemy_dict = normalize(enemy_dict)
        line[enemy_base_cord[0]] = str(enemy)
    return map_dict


def map_del(map:dict, x, y, symbol:str):
    line = map[y]
    line[x] = symbol
    return map


def next_turn(map:dict, enemy_ingame:list, road_pattern:list):
    for enemy in enemy_ingame:
        old_cord = enemy.cord
        if old_cord == enemy_base_cord: #Если враг только реснулся то он на кордах базы и ее нету в списке дороги
            map_del(map, old_cord[0], old_cord[1], '*')
            new_cord = road_pattern[0]
        else:
            map_del(map, old_cord[0], old_cord[1], ' ')
            index = road_pattern.index(old_cord)
            new_cord = road_pattern[index+1]
        
        line = map[new_cord[1]]
        line[new_cord[0]] = str(enemy.hp)
         
        
    return map_dict

map_dict = generate_map(pattern=1)
map_dict = spawn_enemy(enemy_base_cord, map_dict, create_enemy(7))
map_dict = spawn_enemy(enemy_base_cord, map_dict, create_enemy(7))

lines = []
for k,v in map_dict.items():
    line = "".join(v)
    lines.append(line)

# print("\n".join(lines))
list.reverse()
while True:
    print("\n".join(lines))
    print(f"Ход:", turn, end='')
    print(f'\t\tВолна 1')
    print(enemy_ingame[0])
    print(map_dict)
    if input() == '0':
        break
    os.system('cls||clear')
    turn += 1
    



