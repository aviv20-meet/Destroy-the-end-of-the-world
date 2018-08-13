def player_stats():
    hp_defence = []
    attacks=[]
    my_level=int(input("which level of difficulty do you want?\nfor easy type 1\nfor medium type 2\nfor hard type 3"))
    while my_level != type(int):
        player_stats()
    if my_level == 1:
        hp = 50
        defence = 35
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 10
        attack_two = 5
        attacks.append(attack_1)
        attacks.append(attack_2)

    if my_level == 2:
        hp = 30
        defence = 20
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 7
        attack_two = 3
        attacks.append(attack_1)
        attacks.append(attack_2)
    
    if my_level == 3:
        hp = 20
        defence = 10
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 4
        attack_two = 1
        attacks.append(attack_1)
        attacks.append(attack_2)



def enemy_stats():
    hp_defence = []
    attacks=[]
    his_level=int(input("which level of difficulty do you want your enemy to be?\nfor easy type 1\nfor medium type 2\nfor hard type 3"))
    while his_level != type(int):
        player_stats()
    if his_level == 1:
        hp = 20
        defence = 8
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 3
        attack_two = 1
        attacks.append(attack_1)
        attacks.append(attack_2)

    if his_level == 2:
        hp = 27
        defence = 18
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 7
        attack_two = 3
        attacks.append(attack_1)
        attacks.append(attack_2)
    
    if his_level == 3:
        hp = 45
        defence = 30
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 12
        attack_two = 8
        attacks.append(attack_1)
        attacks.append(attack_2)

def player_game():
    
        
        
