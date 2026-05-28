#importing modules
import random
import time

#functions
def load():
    for i in range(0,21): #loop
        bar = "█" * i + '-' * (20-i) #bar + empty
        print(f"\r Loading: [{bar}] {i*5}%", end = "" ) #\r re write same time
        rand_loading_time = random.uniform(0.1,0.5) #uniform to find random delay
        time.sleep(rand_loading_time) #delay
    print() # next line
    print("═" * 40) # close loading bar
    print("You encountered an Enemy!")

def player_attack(enemy):
    dmg = random.randint(10, 25) #choose atk value
    print("\n⚔ You unsheathe your sword...")
    time.sleep(4)
    print("\n🩸 You tried to slash the enemy...")
    time.sleep(1) #wait

    chance = random.random()

    if chance <= 0.1: #checking for miss
        print("❌ Your attack missed the enemy.")
        print("Enemy took no damage.")
        dmg = 0
    elif chance <= 0.3: #checking for crit - 20% chance, 0.1 → 0.3 = 20% cri (used up 0.0-0.1 in if)
        dmg = 2*dmg #2xdmg for crit bonus
        print("It was a Critical Hit!")
        time.sleep(0.5)
        print(f"🔥 You dealt {dmg} (CRIT!) damage to the enemy !")

    else:
        print(f"⚔ You dealt {dmg} damage to the enemy!")

    enemy = enemy_take_dmg(enemy, dmg)
    return enemy

def enemy_take_dmg(enemy, dmg):
    enemy["HP"] = max(0, enemy["HP"] - dmg)
    return enemy

def player_poison_atk(enemy):
    time.sleep(1)
    print("\n🧪 You cast a Poison Spell..")
    time.sleep(2.5)
    if random.random() < 0.8:  # optional hit chance
        
        enemy["HP"]= max(0, enemy["HP"] - 5) #first dmg
        enemy["Status"] = "poison"
        enemy["Status_Turns"] = 3
        enemy["Poison_Dmg"] = random.randint(5, 10)

        print("☠️ Enemy is poisoned!")
    else:
        print("💨 Poison spell failed!")

    return enemy

def apply_status_effect(enemy):
    if enemy["Status"] == 'poison' and enemy["Status_Turns"] > 0:
        print("\n☣ The poison is dealing damage!")

        enemy["HP"] = max(0, enemy["HP"] - enemy["Poison_Dmg"])
        enemy["Status_Turns"] -= 1

        time.sleep(2)
        print(f"💀 Enemy takes {enemy['Poison_Dmg']} poison damage!")

        if enemy["Status_Turns"] == 0:
            enemy["Poison_Dmg"] = 0
            enemy["Status"] = None
            print("✨ Poison wore off!")

    return enemy

def game_end(player_hp, enemy):
    if player_hp <= 0:
        game_lose(player_hp, enemy["HP"])
    elif enemy["HP"] <= 0:
        game_win(player_hp, enemy["HP"])

def game_lose(player_hp, enemy_hp):
    print("\n" + "═" * 40)
    print("GAME OVER")
    print("────────────────────────────")
    print(f"Your HP: {player_hp}")
    time.sleep(3)
    print(f"Enemy HP: {enemy_hp}")   
    time.sleep(2) 
    print(f"The enemy defeated you!")
    time.sleep(1)
    print(f"😢 You Lost!")

def game_win(player_hp, enemy_hp):
    print("═" * 40)
    print("\n" + "═" * 40)
    print("GAME OVER")
    print("────────────────────────────")
    print(f"Your HP: {player_hp}")
    time.sleep(3)
    print(f"Enemy HP: {enemy_hp}")   
    time.sleep(2) 
    print(f"You defeated the enemy!")
    time.sleep(1)
    print(f"👑 You won!")
    print("═" * 40)

def player_heal(player_hp, max_hp):
    heal = random.randint(10, 20) #choose hp value
    print(f"\n🧙‍♂️ You are trying to cast a healing spell...")
    time.sleep(4) #wait
    print("\n✅ The spell worked!")
    time.sleep(1)
    print(f"🩹 You healed {heal} HP!") #heal hp    

    player_hp = min(max_hp , player_hp + heal)

    return player_hp 

def show_stat(enemy, player_hp):
    print("\nCurrent Stats -")
    time.sleep(1)
    print(f"👾 Enemy HP: {enemy['HP']}")
    print(f"🧪 Enemy Status: {enemy['Status']}")
    print(f"🤠 Your HP: {player_hp}")

def enemy_turn(enemy, player_hp): 
    chance = random.random() # gen no. from 0.0 to 1.0

    if enemy["HP"] < enemy["Max_HP"] * 0.4 and chance < 0.7: # check for health and chance for heal
        dmg = 0
        heal = random.randint(5,20) # choose enemy heal
        
        print("\n😈 Enemy is thinking...")
        time.sleep(4) # wait
        print("\n👾❤️‍🩹 Enemy is healing!")
        time.sleep(1.5) # wait
        print(f"💚 Enemy healed {heal} HP!")  
                
    else:
        heal = 0
        dmg = random.randint(5,20) # choose enemy atk
        print("\n😈 Enemy is thinking...")
        time.sleep(4) # wait
        print("\n👾⚔ Enemy is attacking!")
        time.sleep(1.5) # wait
        print(f"🩸 Enemy dealt {dmg} damage to you!")     
    
    enemy["HP"] = min(enemy["Max_HP"], enemy["HP"] + heal) # heal
    player_hp = max(0, player_hp - dmg) # deal dmg (use max to prevent negative hp)

    return player_hp, enemy

#welcome
print("\n" + "═" * 40)
print("🎮 Welcome to the RPG Game~")
print("═" * 40)

#player vars
Player_HP = 100
Player_Max_HP = 150
Player_choice = None

#enemy vars
enemy = {
        "HP": 80,
        "Max_HP": 80,
        "Rand_atk": 0,
        "Status": None,
        "Status_Turns": 0,
        "Poison_Dmg": 0
}

#loading vars
rand_loading_time = 0

#loading bar
load()

#Game Loop
while Player_HP > 0 and enemy["HP"] > 0:
    #asking action
    time.sleep(2.5) #wait
    print("\n🎯 Possible actions: \n💚 'Heal' - Heal HP!\n🔪 'Attack' - Attack the enemy!\n☠  'Poison' - Use poison spell to deal damage over time!")
    Player_choice = input("What would you like to do?: ").lower().strip() # ask the player

    if Player_choice == 'heal':
        # healing action
        Player_HP = player_heal(Player_HP, Player_Max_HP) # calling function to heal
        
        time.sleep(2) # wait  

        show_stat(enemy, Player_HP) #call show stat

    elif Player_choice == 'attack':
        #attack action 

        enemy = player_attack(enemy)# calling function to attack
        time.sleep(2) #wait
        show_stat(enemy, Player_HP) #call show stat

    elif Player_choice == 'poison':
        #poison action
        enemy = player_poison_atk(enemy)

    else:
        print('😠 Invalid action! Try again...') # invalid
        continue
    
    time.sleep(2)
    enemy = apply_status_effect(enemy)
    
    if enemy["HP"] > 0:
        Player_HP, enemy = enemy_turn(enemy, Player_HP)
        time.sleep(2) #wait
        show_stat(enemy, Player_HP) #call show stat

game_end(Player_HP, enemy)