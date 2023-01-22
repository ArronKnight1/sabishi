#MODULES
import random
import time
import sys
from time import sleep

#SLOW PRINTING
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.08)
        
#PAUSE BETWEEN PRINTS
def s():
    time.sleep(1)

#ENEMY
class enemy:
    def __init__(self, species, health, max_health, attack1, attack2, attack1_power, attack2_power):
        self.species = species
        self.health = health
        self.max_health = max_health
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack1_power = attack1_power
        self.attack2_power = attack2_power
#types of enemys                          
weak_enemy = enemy("Bandit", 5, 5, "swipe", "jab", random.randint(1, 3), random.randint(3, 5))
normal_enemy = enemy("Corrupt Samurai", 10, 10, "kunai throw", "sushi slice", random.randint(5, 7), random.randint(7, 9))
strong_enemy = enemy("Skilled Ronin", 15, 15, "triple slash", "execute", random.randint(9, 11), random.randint(11, 13))

#PLAYER
class player:
    def __init__(self, name, health, max_health, attack_power, score):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.score = score
    
defult_player = player("", 10, 10, 5, 0)
#getting players name
slowprint("What is your name traveler?")
defult_player.name = input("")
slowprint("You have a curious power. The strong power to survive.")

#INTRO
slowprint("Are you ready?")
print(defult_player.name)
input("")
s()

print(r"""

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~


------------------------------
Welcome to Sabishi RPG ようこそ
------------------------------
""")

print("Welcome", defult_player.name + "!\n")
s()
print("Type 'help' for a list of commands")
s()

#BATTLE SYSTEM
def battle():
    battle_mode = True
#resetting enemys health (i could have reset ust the health but it was easier to copy paste this in)
    weak_enemy = enemy("Bandit", 5, 5, "swipe", "jab", random.randint(1, 3), random.randint(3, 5))
    normal_enemy = enemy("Corrupt Samurai", 10, 10, "kunai throw", "sushi slice", random.randint(5, 7), random.randint(7, 9))
    strong_enemy = enemy("Skilled Ronin", 15, 15, "triple slash", "execute", random.randint(9, 11), random.randint(11, 13))
#randomizing enemy
    randomize = random.randint(1, 6)
    if randomize == 1:
        encounterd_enemy = weak_enemy
    elif randomize == 2:
        encounterd_enemy = weak_enemy
    elif randomize == 3:
        encounterd_enemy = weak_enemy
    elif randomize == 4:
        encounterd_enemy = normal_enemy
    elif randomize == 5:
        encounterd_enemy = normal_enemy
    elif randomize == 6:
        encounterd_enemy = strong_enemy
    print("\n" + encounterd_enemy.species + ": 'Lets fight, traveler!'\n")
    time.sleep(1)
    print(encounterd_enemy.species , "has challenged you to a fight!")
    time.sleep(1)
#battle loop
    while battle_mode == True:
#enemy/player death
        if defult_player.health <= 0:
            death()
        elif encounterd_enemy.health <= 0:
            print("\nYou have eliminated the", encounterd_enemy.species + "\nYou now feel stronger!")
            if encounterd_enemy == weak_enemy:
                defult_player.max_health = defult_player.max_health + 1
                defult_player.score = defult_player.score + 1
                defult_player.attack_power = defult_player.attack_power + 1
            elif encounterd_enemy == normal_enemy:
                defult_player.max_health = defult_player.max_health + 2
                defult_player.score = defult_player.score + 2
                defult_player.attack_power = defult_player.attack_power + 2
            elif encounterd_enemy == strong_enemy:
                defult_player.max_health = defult_player.max_health + 3
                defult_player.score = defult_player.score + 3
                defult_player.attack_power = defult_player.attack_power + 3
            battle_mode = False
            break
#enemy turn
        attacks_list = [encounterd_enemy.attack1, encounterd_enemy.attack2]
        chosen_attack = (random.choice(attacks_list))
        print("The", encounterd_enemy.species, "used", chosen_attack)
        time.sleep(1)
        randomize_dodge = random.randint(1, 3)
        if randomize_dodge >= 2:
            if chosen_attack == encounterd_enemy.attack1:
                health_lost = encounterd_enemy.attack1_power
            elif chosen_attack == encounterd_enemy.attack2:
                health_lost = encounterd_enemy.attack2_power
            print("The", encounterd_enemy.species, "landed the attack, you lost", health_lost, "health!")
            time.sleep(1)
            defult_player.health = defult_player.health - health_lost
        elif randomize_dodge == 1:
            print("You dodged the", encounterd_enemy.species + "'s attack!")
            time.sleep(1)
#enemy/player death
        if defult_player.health <= 0:
            death()
        elif encounterd_enemy.health <= 0:
            print("\nYou have eliminated the", encounterd_enemy.species + "\nYou now feel stronger!")
            if encounterd_enemy == weak_enemy:
                defult_player.max_health = defult_player.max_health + 1
                defult_player.score = defult_player.score + 1
                defult_player.attack_power = defult_player.attack_power + 1
            elif encounterd_enemy == normal_enemy:
                defult_player.max_health = defult_player.max_health + 2
                defult_player.score = defult_player.score + 2
                defult_player.attack_power = defult_player.attack_power + 2
            elif encounterd_enemy == strong_enemy:
                defult_player.max_health = defult_player.max_health + 3
                defult_player.score = defult_player.score + 3
                defult_player.attack_power = defult_player.attack_power + 3
            battle_mode = False
            break
#player turn
        time.sleep(1)
        battle_choose = input("\nYour turn (fight/flee/stats): ").lower()
        if battle_choose == "fight":
            time.sleep(1)
            print("You attacked the enemy!")
            time.sleep(1)
            encounterd_enemy.health = encounterd_enemy.health - defult_player.attack_power
            print("The enemy now has", str(encounterd_enemy.health) + "/" + str(encounterd_enemy.max_health), "health")
        elif battle_choose == "flee":
            time.sleep(1)
            randomize_flee = random.randint(1, 3)
            if randomize_flee >= 2:
                print("You failed get away fast enough!")
            elif randomize_flee == 1:
                print("You escaped the enemy!")
                battle_mode = False
            #make stats option so the enemy doesnt attack you after you use it, maybe make it a seperate turn?
        elif battle_choose == "stats":
            print("\n" + str(defult_player.name) + "'s Stat Card:\nHealth:", str(defult_player.health) + "/" + str(defult_player.max_health) + "\nAttack Power:", str(defult_player.attack_power))
            print("\n" + str(encounterd_enemy.species) + "'s Stats:\nHealth:", str(encounterd_enemy.health) + "/" + str(encounterd_enemy.max_health) + "\nAttack 1:", str(encounterd_enemy.attack1), "(" + str(encounterd_enemy.attack1_power) + " dmg" + ")" + "\nAttack 2:", str(encounterd_enemy.attack2), "(" + str(encounterd_enemy.attack2_power) + " dmg" + ")\n")
            time.sleep(1)
        else:
            print("Incorrect input")

#DEATH
def death():
    slowprint("\nYou died.\nNobody will remember you.")
    print(r"""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |                  ||
          |                  ||
  *     * | *   **    * **   |**      **
   \))..,\,/.,(//,,..,,\||(,,.,\\,.((//

                       """)
    print("You score was", defult_player.score)
    time.sleep(2)
    print("Closing game")
    time.sleep(3)
    quit()

#WINNING GAME
def win():
    slowprint("\nWow you have a score of 100")
    slowprint("Your will to survive is greater than most beings on this earth. Well done")
        
#CHOOSING COMMANDS
def choose():
    s()
    choose = input("\nWhat now?: ").lower()
#help command
    if choose == "help":
        print("\nList of commands:\n-'explore'\n-'rest'\n-'stats'")
#stats command
    elif choose == "stats":
        print("")
        print(str(defult_player.name) + "'s Stat Card:\nHealth:", str(defult_player.health) + "/" + str(defult_player.max_health) + "\nAttack Power:", str(defult_player.attack_power) + "\nScore:", str(defult_player.score))
    elif choose == "explore":
#encounter boss or not
        boss_chance = random.randint(1, 15)
        if boss_chance == 15:
            boss()
        else:
#encounter enemy or not
            encounter = random.randint(1, 2)
            if encounter == 1:
                battle()
            elif encounter == 2:
#explore message
                explore_msg = random.randint(1, 6)
                if explore_msg == 1:
                    print(defult_player.name, "ventured along the road of life.")
                elif explore_msg == 2:
                    print(defult_player.name, "hikes up a mountain.")
                elif explore_msg == 3:
                    print(defult_player.name, "is alone.")
                elif explore_msg == 4:
                    print(defult_player.name, "hunts deer.")
                elif explore_msg == 5:
#health potion
                    print(defult_player.name, "finds a health potion and drinks it.")
                    s()
                    if defult_player.health == defult_player.max_health:
                        print("It had no effect!")
                    else:
                        defult.player.health == defult_player.max_health
                        print("It fully restored your health!")
                elif explore_msg == 6:
#npc
                    print(r"""
                                ,    _
                               /|   | |
                             _/_\_  >_<
                            .-\-/.   |
                           /  | | \_ |
                           \ \| |\__(/
                           /(`---')  |
                          / /     \  |
                       _.'  \'-'  /  |
                        `----'`=-='   ' 
                       """)
                    print(defult_player.name, "encounters a wise old man\n")
                    npc_msg = random.randint(1, 5)
                    if npc_msg == 1:
                        slowprint("Wise old man: 'The truth will set you freeeeeee!'")
                    elif npc_msg == 2:
                        slowprint("Wise old man: 'I have a riddle for you... Haha just kidding!'")
                    elif npc_msg == 3:
                        slowprint("Wise old man: 'Gosh you smell! You must be a redditor!'")
                    elif npc_msg == 4:
                        slowprint("Wise old man: 'Pffft you look like a discord mod! Touch some grass!'")
                    elif npc_msg == 5:
                        slowprint("Wise old man: 'Type the word", "'summon' to summon a dragon!'")
                        input("")
                        slowprint("Wise old man: 'HAHAHA NO WAY YOU BELIVED THAT'")
                        s()
                        print(r"""
                                                 __
                     _.-'.-'-.__
                  .-'.       '-.'-._ __.--._
           -..'\,-,/..-  _         .'   \   '----._
            ). /_ _\' ( ' '.         '-  '/'-----._'-.__
            '..'     '-r   _      .-.       '-._ \
            '.\. Y .).'       ( .'  .      .\          '\'.
            .-')'|'/'-.        \)    )      '',_      _.c_.\
              .<, ,>.          |   _/\        . ',   :   : \\
             .' \_/ '.        /  .'   |          '.     .'  \)
                             / .-'    '-.        : \   _;   ||
                            / /    _     \_      '.'\ ' /   ||
                           /.'   .'        \_      .|   \   \|
                          / /   /      __.---'      '._  ;  ||
                         /.'  _:-.____< ,_           '.\ \  ||
                        // .-'     '-.__  '-'-\_      '.\/_ \|
                       ( };====.===-==='        '.    .  \\: \
                        \\ '._        /          :   ,'   )\_ \
                         \\   '------/            \ .    /   )/
                          \|        _|             )Y    |   /
                           \\      \             .','   /  ,/
                            \\    _/            /     _/
                             \\   \           .'    .'
                              '| '1          /    .'
                                '. \        |:    /
                                  \ |       /', .'
                                   \(      ( ;z'
                                    \:      \ '(_
                                     \_,     '._ '-.___
                                                 '-' -.\
                       """)
                        slowprint("\nWise old man: 'OH WAIT WHAT'")
                        s()
                        print("The 'not so' wise old man fled")
                        s()
#rest
    elif choose == "rest":   
        randomize_rest = random.randint(1, 4)
        if randomize_rest <= 3:
            if defult_player.health != defult_player.max_health:
                print("You lay down to rest, you have gained +1 health!")
                defult_player.health = defult_player.health + 1
            elif defult_player.health == defult_player.max_health:
                print("You lay down to rest")
        elif randomize_rest == 4:
            print("You lay down to rest but were awoken!")
            time.sleep(1)
            battle()
#other
        else:
            print("Incorrect input")
        
#BOSS FIGHTS
def boss():
    boss_choose = random.randint(1, 2)
#boss1
    if boss_choose == 1:
        slowprint("Evil Yokai: Human. Lets play game.")
        s()
        print("\nAn evil Yokai wants to play a game!")
        s()
        print(r"""
                                                     ,--,  ,.-.
                       ,                   \,       '-,-`,'-.' | ._
                      /|           \    ,   |\         }  )/  / `-,',
                      [ ,          |\  /|   | |        /  \|  |/`  ,`
                      | |       ,.`  `,` `, | |  _,...(   (      .',
                      \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\
                       \  \_\,``,   ` , ,  /  |         )         _,/
                        \  '  `  ,_ _`_,-,<._.<        /         /
                         ', `>.,`  `  `   ,., |_      |         /
                           \/`  `,   `   ,`  | /__,.-`    _,   `\
                       -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                        \_,,.) /\    ` /  / ) (-,, ``    ,        |
                       ,` )  | \_\       '-`  |  `(               \
                      /  /```(   , --, ,' \   |`<`    ,            |
                     /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
               ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
              (-, \           ) \ ('_.-._)/ /,`    /
              | /  `          `/ \\ V   V, /`     /
           ,--\(        ,     <_/`\\     ||      /
          (   ,``-     \/|         \-A.A-`|     /
         ,>,_ )_,..(    )\          -,,_-`  _--`
        (_ \|`   _,/_  /  \_            ,--`
         \( `   <.,../`     `-.._   _,-`
                
        """)
        slowprint("\nEvil Yokai: 'Mortal! We will play a game of luck. ROCK, PAPER SCISSORS!!! You better not pick wrong. Mwhahaha!'")
        print("rock, paper or scissors?")
        player_choose = input("").lower()
        choices = ["rock", "paper", "scissors"]
        ai_choose = random.choice(choices)
        print("\nYou picked", player_choose + ".", "The Evil Yokai picked", ai_choose + "\n")
        time.sleep(1)
        if player_choose == ai_choose:
            slowprint("Evil Yokai: 'Huh it's a draw. I drew against a mortal?... I must flee-'")
            s()
            slowprint("The Evil Yokai fled")
        if player_choose == "rock":
            if ai_choose == "paper":
                slowprint("Evil Yokai: 'You loose. Not supprised weakling.'")
                s()
                print("The Evil Yokai swiped at you, you went flying!")
                s()
                print("You lost -5 health")
                s()
                defult_player.health = defult_player.health - 5
                if defult_player.health <= 0:
                    death()
            elif ai_choose == "scissors":
                slowprint("Evil Yokai: 'NO! But!- I-'")
                s()
                defult_player.max_health = defult_player.max_health + 5
                defult_player.score = defult_player.score + 5
                defult_player.attack_power = defult_player.attack_power + 5
                print("You are now stronger")
                insult_boss = input("Insult the Evil Yokai: ")
                insult_msg_random = random.randint(1, 3)
                if insult_msg_random == 1:
                    slowprint("Huh that's your best insult? Well i'm off now-")
                    s()
                    print("The Evil Yokai fled")
                elif insult_msg_random == 2:
                    slowprint("Evil Yokai: 'OH. That really hurt my feelings. HAHA JUST KIDDING. I'm off, noob!'")
                    s()
                    print("The Evil Yokai escaped")
                elif insult_msg_random == 3:
                    slowprint("Evil Yokai: *cries* 'I'm outa here!'")
                    s()
                    slowprint("The Evil Yokai vanished")
                    s()
        if player_choose == "paper":
            if ai_choose == "rock":
                slowprint("Evil Yokai: 'NO! But!- I-'")
                s()
                defult_player.max_health = defult_player.max_health + 5
                defult_player.score = defult_player.score + 5
                defult_player.attack_power = defult_player.attack_power + 5
                insult_boss = input("Insult the Evil Yokai: ")
                insult_msg_random = random.randint(1, 3)
                if insult_msg_random == 1:
                    slowprint("Evil Yokai: 'Huh that's your best insult? Well i'm off now-'")
                    s()
                    print("The Evil Yokai fled")
                    s()
                elif insult_msg_random == 2:
                    slowprint("Evil Yokai: OH. That really hurt my feelings. HAHA JUST KIDDING. I'm off, noob!")
                    s()
                    print("The Evil Yokai escaped")
                elif insult_msg_random == 3:
                    slowprint("Evil Yokai: *cries* 'I'm outa here!'")
                    s()
                    print("The Evil Yokai vanished")
            elif ai_choose == "scissors":
                slowprint("Evil Yokai: 'You loose haha!'")
                s()
                print("The Evil Yokai swiped at you, you went flying!")
                s()
                print("You lost -5 health")
                s()
                defult_player.health = defult_player.health - 5
                if defult_player.health <= 0:
                    death()
        if player_choose == "scissors":
            if ai_choose == "paper":
                slowprint("Evil Yokai: 'NO! But!- I- How did you win???'")
                s()
                defult_player.max_health = defult_player.max_health + 5
                defult_player.score = defult_player.score + 5
                defult_player.attack_power = defult_player.attack_power + 5
                insult_boss = input("Insult the Evil Yokai: ")
                s()
                insult_msg_random = random.randint(1, 3)
                if insult_msg_random == 1:
                    slowprint("Huh that's your best insult? Well i'm off now-")
                    s()
                    print("The Evil Yokai fled")
                    s()
                elif insult_msg_random == 2:
                    slowprint("Evil Yokai: OH. That really hurt my feelings. HAHA JUST KIDDING. I'm off, noob!")
                    s()
                    print("The Evil Yokai escaped")
                elif insult_msg_random == 3:
                    slowprint("Evil Yokai: *cries* I'm outa here!")
                    s()
                    print("The Evil Yokai vanished")
                    s()
            elif ai_choose == "rock":
                slowprint("Evil Yokai: 'You loose. Not supprised weakling.'")
                s()
                print("The Evil Yokai swiped at you, you went flying!")
                s()
                print("You lost -5 health")
                s()
                print("You ran away from the Evil Yokai.")
                s()
                defult_player.health = defult_player.health - 5
                if defult_player.health <= 0:
                    death()
        else:
            s()
            print("Incorrect input")
            s()
            slowprint("Evil Yokai: 'So you do not even want to play huh. Not supprised weakling.'")
            s()
            print("The Evil Yokai swiped at you, you went flying!")
            s()
            print("You lost -5 health")
            s()
            print("You ran away from the Evil Yokai.")
            s()
            defult_player.health = defult_player.health - 5
            if defult_player.health <= 0:
                death()


#boss2
    if boss_choose == 2:
        slowprint("???: 'A human... wooow'.\nA being not from this earth has spotted you!")
        time.sleep(2)
        print(r"""
        
            .-****-. 
           /        \     
          /_        _\   
         // \      / \\  
         |\__\    /__/|  
          \    ||    /  
           \        /    
            \  __  /     
             '.__.'     
              |  |      
              |  |        
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
        time.sleep(2)
        boss1_number = random.randint(1, 10)
        boss1_guess = None
        boss1_lifes = 3
        print("???: 'Welcome to my game", defult_player.name + ", you have", boss1_lifes, "guesses to guess the number I am thinking of (1-10)'.\n")
        time.sleep(2)
        boss1_fight = True
        while boss1_fight == True:
            slowprint("???: 'So! What's your guess, human?'")
            boss1_guess = input("").lower()
            s()
            boss1_guess = int(float(boss1_guess))
            if boss1_guess == boss1_number:
                slowprint("???: 'Huh, Well I guess I will let you go since you got the number right' *sigh*...")
                s()
                print("You now feel a bunch more stronger!\n")
                defult_player.max_health = defult_player.max_health + 5
                defult_player.score = defult_player.score + 5
                defult_player.attack_power = defult_player.attack_power + 5
                time.sleep(1)
                boss1_fight = False
            elif boss1_guess > boss1_number:
                print("???: 'Hey stupid! Here is a hint: guess lower!'")
                boss1_lifes = boss1_lifes - 1
                print("???: 'You only have", boss1_lifes, "guesses left!'")
            elif boss1_guess < boss1_number:
                print("???: 'Haha WRONG! Maybe try guessing higher!'")
                boss1_lifes = boss1_lifes - 1
                print("???: 'You only have", boss1_lifes, "guesses left!'")
            else:
                print("Incorrect Input")
        if boss1_lifes == 0:
            s()
            print("???: 'Game over", defult_player.name + "!\n")
            s()
            slowprint("???: 'Time to eat you!'")
            s()
            boss1_fight = False
            death()
        
#MAIN LOOP
while defult_player.health > 0:
    choose()

