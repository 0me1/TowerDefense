

map_dict = {16: ['o', 'o', 'o', 'o', '(', '5', ')', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 15: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 14: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '{', '*', '}', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 13: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 
'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 12: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 11: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 10: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 9: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 8: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 7: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 6: ['o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 5: ['o', 'o', 'o', 'o', '[', ' ', ']', '[', ' ', ']', '[', ' ', ']', '[', ' ', ']', '[', ' ', ']', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 4: ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 3: ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 2: ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 1: ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']}
road_pattern = [ # (x, y) road center
            (5, 15), (5, 14), (5, 13), (5, 12), (5, 11),
            (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), 
            (5, 5), (8, 5), (11, 5), (14, 5), (17, 5), (17, 6), (17, 7),
            (17, 8), (17, 9), (17, 10), (17, 11), (17, 12),
            (17, 13)
        ]
class Enemy:
    def __init__(self, hp, cord=None):
        self.cord = cord
        self.hp = hp

enemy_ingame = [Enemy(5,(5,16))]
# enemy_ingame.append(Enemy(5, (5,3)))
enemy_base_cord = (5,16)

def map_del(map, x, y, symbol):
    line = map[y]
    line[x] = symbol
    return map

def next_turn(map:dict, enemy_ingame:list, road_pattern:list):
    for enemy in enemy_ingame:
        old_cord = enemy.cord
        if old_cord == enemy_base_cord: #Если враг только реснулся то он на кордах базы ее нету в списке дороги
            map_del(map, old_cord[0], old_cord[1], '*')
            new_cord = road_pattern[0]
        else:
            map_del(map, old_cord[0], old_cord[1], ' ')
            index = road_pattern.index(old_cord)
            new_cord = road_pattern[index+1]
        
        line = map[new_cord[1]]
        line[new_cord[0]] = str(enemy.hp)
         
        
    return map_dict

# a = next_turn(map_dict, enemy_ingame, road_pattern)
# b = map_del(map_dict, 5, 16, '*')

lines = []
for k,v in map_dict.items():
    line = "".join(v)
    lines.append(line)
print("\n".join(lines))
lines = []
while True:
    next_turn(map_dict, enemy_ingame, road_pattern)
    for k,v in map_dict.items():
        line = "".join(v)
        lines.append(line)
    print("\n".join(lines))
    if input() == '0':
        break

# for k,v in b.items():
#     line = "".join(v)
#     lines.append(line)
# print("\n".join(lines))