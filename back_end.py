import random

def player_stats():
    hp_defence = []
    player_attacks=[]
    my_level=int(input("which level of difficulty do you want?\nfor easy type 1\nfor medium type 2\nfor hard type 3"))
    #while my_level != type(int):
        #player_stats()
    if my_level == 1:
        hp = 50
        defence = 35
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_1= 10
        attack_2 = 5
        player_attacks.append(attack_1)
        player_attacks.append(attack_2)
        ability_player = 5
        player_attacks.append(ability_player)

    if my_level == 2:
        hp = 30
        defence = 20
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_1 = 7
        attack_2 = 3
        player_attacks.append(attack_1)
        player_attacks.append(attack_2)
        ability_player = 5
        player_attacks.append(ability_player)
    
    if my_level == 3:
        hp = 20
        defence = 10
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_1 = 4
        attack_2 = 1
        player_attacks.append(attack_1)
        player_attacks.append(attack_2)
        ability_player = 5
        player_attacks.append(ability_player)
    return player_attacks, hp_defence

def enemy_stats():
    hp_defence = []
    enemy_attacks=[]
    his_level=int(input("which level of difficulty do you want your enemy to be?\nfor easy type 1\nfor medium type 2\nfor hard type 3"))
    #while his_level != type(int):
        #player_stats()
    if his_level == 1:
        hp = 15
        defence = 8
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 3
        attack_two = 1
        enemy_attacks.append(attack_one)
        enemy_attacks.append(attack_two)
        ability_enemy = 4
        enemy_attacks.append(ability_enemy)

    if his_level == 2:
        hp = 25
        defence = 18
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 7
        attack_two = 3
        enemy_attacks.append(attack_one)
        enemy_attacks.append(attack_two)
        ability_enemy = 4
        enemy_attacks.append(ability_enemy)
    
    if his_level == 3:
        hp = 45
        defence = 30
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 12
        attack_two = 8
        enemy_attacks.append(attack_one)
        enemy_attacks.append(attack_two)
        ability_enemy = 4
        enemy_attacks.append(ability_enemy)
    return enemy_attacks, hp_defence

def player_game(player_hp_defence, player_attacks):
##    turn=( , )
    
    choice = input("What Would you like to do?\nTo choose attack type'attack'\nTo use ability type'ability'\nTo run type'run'")
    choice.lower()
    if(choice == 'attack'):
        attack_choice = input("To choose a powerfull attack that is affected by defence type'power'\nTo choose a less is not affected by defence type'less power'")
        attack_choice.lower()
        if attack_choice == 'power':
            player_turn = "attack power",player_attacks[0]
        if(attack_choice =='less power'):
            player_turn = "attack less power" , player_attacks[1]
        else:
            print("Try agian")
            player_game(player_hp_defence, player_attacks)
    if choice == 'ability':
        player_turn = "ability" , player_attacks[2]
    else:
        print("Try agian")
        player_game(player_hp_defence, player_attacks)
    if(choice == 'run'):
        exit()


def enemy_game(player_hp_defence,enemy_attacks):
    if (changing_def >=  player_hp_defence[1]/2):
        rand_abi_latt = random.randint(1,2)
        if rand_abi_latt == 1:
            enemy_turn_be = 'ability', enemy_attacks[2]
        if rand_abi_latt == 2:
            enemy_turn_be = 'attack less power', enemy_attacks[1]
    else:
        enemy_turn_af = 'power attack' , enemy_attacks[0]
            
        
        
        


    
#1/3 chance that the same move will not work for player
    
def main():
    
    enemy_hp_defence ,enemy_attacks =  enemy_stats()
    player_hp_defence, player_attacks = player_stats()
    player_game(player_hp_defence, player_attacks)
    global changing_def
    changing_def = player_hp_defence[1]

            
            

main()
        
        
