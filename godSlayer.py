import random

# This function gets the player's name
def player_name():
    print('*An ominous voice calls*')
    print("What is your name human?")
    name = input('Enter your name: ')
    print('---------------------------------------------------------')
    print(f'{name}, A CELESTIAL BEING has challenged you to a battle to the death! ')
    print('_________________________________________________________')
    return name


GAME_OVER = 'YOU HAVE BEEN DEFEATED, GAME OVER!'

# List of the enemy attacks
BOSS_MOVES = ['UNHOLY SWORD', 'UNHOLY FIREBALL', 'UNHOLY BITE']

# Phase 2 boss moves
BOSS_MOVES_2 = ['CELESTIAL BEING: What are we doing man, this is crazy, let\'s stop this?',
                "CELESTIAL BEING: Argh, I dropped one of my contact lenses, think it's "
                "there behind you, mind picking it up for me?",
                ]

# Enemy responses for when you heal
BOSS_MOVES_3 = ['*CELESTIAL BEING laughs at and taunts your weakness*',
                '*CELESTIAL BEING smirks* CELESTIAL BEING recovers some health',
                'CELESTIAL BEING uses some eye drops... it has no noticeable effect',
                '*CELESTIAL BEING laughs at and taunts your weakness*',
                ]

# Your attacks
SWORD_ATTACKS = ['Your attack missed...',
                 'You landed your attack',
                 'You both landed a hit',
                 'You both landed a hit',
                 'You both landed a hit',
                 'Your attack missed...',
                 ]

ROCKET_ATTACKS = ['You landed a critical hit! CELESTIAL BEING stumbles a bit',
                  'You landed a critical hit! CELESTIAL BEING stumbles a bit',
                  'Your attack missed...',
                  'Your attack missed...',
                  'Your attack missed...',
                  'You landed a critical hit! CELESTIAL BEING stumbles a bit',
                  ]

PUNCH_ATTACKS = ['Your attack missed...',
                 'Your attack missed...',
                 'You landed your attack',
                 'You landed your attack',
                 'You landed a critical hit! CELESTIAL BEING stumbles a bit',
                 'Your attack missed...',
                 ]


def death_battle():
    intro()
    fight()


def intro():
    answer = ""
    name = player_name()
    while answer != 1 and answer != 2:
        print('')
        print('------------------------------------------------------------------------')
        answer = int(input('Do you accept the challenge? PRESS(1)."I accept!" PRESS(2)."No thanks..."'))
        print('------------------------------------------------------------------------')
        print('')
    if answer == 1:
        print('**************************************')
        print(f'''
        *CELESTIAL BEING laughs*
        CELESTIAL BEING: Good, good, fight me to the death!
        No one else but me and you! Leave it all here, make me feel alive!! Prepare yourself {name}!
        ''')
        print('**************************************')
    elif answer == 2:
        print('**************************************')
        print(f'''
        *CELESTIAL BEING laughs hysterically*
        "CELESTIAL BEING: Dread it, run from it, destiny arrives all the same {name}!
        Make me feel alive!!!
        ''')
        print('**************************************')
    return answer


def fight():
    my_hp = 30
    boss_hp = 15
    while boss_hp > 10 and my_hp > 0:
        move = your_move()
        if move == 1:
            sw_result = SWORD_ATTACKS[random.randint(0, len(SWORD_ATTACKS) - 1)]
            print(sw_result)
            if sw_result == 'Your attack missed...':
                my_hp = my_hp - 10
                print('CELESTIAL BEING landed a critical hit. You have ' + str(my_hp) + ' Health left.')
                print('*CELESTIAL BEING begins singing*')
                if my_hp <= 0:
                    print(GAME_OVER)
                    break
            elif sw_result == 'You both landed a hit':
                my_hp = my_hp - 5
                boss_hp = boss_hp - 5
                print('You have ' + str(my_hp) + ' Health left')
                if my_hp <= 0:
                    print(GAME_OVER)
                    break
            elif sw_result == 'You landed a critical hit! CELESTIAL BEING stumbles a bit':
                boss_hp = boss_hp - 10
                print('You took no damage. You have ' + str(my_hp) + ' Health left.')
            elif sw_result == 'You landed your attack':
                boss_hp = boss_hp - 5
                print('You took no damage. You have ' + str(my_hp) + ' Health left.')
        elif int(move) == 2:
            r_result = ROCKET_ATTACKS[random.randint(0, len(ROCKET_ATTACKS) - 1)]
            print(r_result)
            if r_result == 'Your attack missed...':
                my_hp = my_hp - 10
                print('CELESTIAL BEING landed a critical hit. You have ' + str(my_hp) + ' Health left.')
                if my_hp <= 0:
                    print(GAME_OVER)
                    break
            elif r_result == 'You both landed a hit':
                my_hp = my_hp - 5
                boss_hp = boss_hp - 5
                print('You have ' + str(my_hp) + ' Health left')
                if my_hp <= 0:
                    print(GAME_OVER)
                    break
            elif r_result == 'You landed a critical hit! CELESTIAL BEING stumbles a bit':
                boss_hp = boss_hp - 10
                print('You took no damage. You have ' + str(my_hp) + ' Health left.')
            elif r_result == 'You landed your attack':
                boss_hp = boss_hp - 5
                print('You took no damage. You have ' + str(my_hp) + ' Health left.')
        elif int(move) == 3:
            p_result = PUNCH_ATTACKS[random.randint(0, len(PUNCH_ATTACKS) - 1)]
            print(p_result)
            if p_result == 'Your attack missed...':
                my_hp = my_hp - 10
                print('CELESTIAL BEING landed a critical hit. You have ' + str(my_hp) + ' Health left.')
                if my_hp <= 0:
                    print(GAME_OVER)
                    break
            elif p_result == 'You both landed a hit':
                my_hp = my_hp - 5
                boss_hp = boss_hp - 5
                print('You have ' + str(my_hp) + ' Health left')
                if my_hp <= 0:
                    print(GAME_OVER)
                    break
            elif p_result == 'You landed a critical hit! CELESTIAL BEING stumbles a bit':
                boss_hp = boss_hp - 10
                print('You took no damage. You have ' + str(my_hp) + ' Health left.')
            elif p_result == 'You landed your attack':
                boss_hp = boss_hp - 5
                print('You took no damage. You have ' + str(my_hp) + ' Health left.')
                if my_hp <= 0:
                    print(GAME_OVER)
                    break
        elif int(move) == 4:
            my_hp = my_hp + 5
            print('***** You healed some of your wounds ' + str(my_hp) + ' Health left *****')
            boss_move = BOSS_MOVES_3[random.randint(0, len(BOSS_MOVES_3) - 1)]
            print(boss_move)
            if boss_move == '*CELESTIAL BEING smirks* CELESTIAL BEING recovers some health':
                boss_hp = boss_hp + 10
        if my_hp <= 0:
            print(GAME_OVER)
            break
        if boss_hp <= 10:
            phase_2()


def phase_2():

    print('-----------------------------------')
    print('CELESTIAL BEING is looking weak...')
    print('---------------------------')
    print('CELESTIAL BEING would like to speak with you, will you listen?')
    response = int(input('PRESS(1). Yes PRESS(2). No'))
    if response == 1:
        print('')
        print('CELESTIAL BEING: *cough, cough* What was your name again... John was it..?')
        print(BOSS_MOVES_2[random.randint(0, len(BOSS_MOVES_2) - 1)])
        response_2 = int(input('PRESS(1). Cool with me! PRESS(2). *laugh* time to accept your fate!'))
        if response_2 == 1:
            print('')
            print(f'CELESTIAL BEING: You know, I\'m not really a bad guy...')
            print('*CELESTIAL BEING summons a sword from the ground*')
            print('')
            print('CELESTIAL BEING uses ULTIMATE UNHOLY ATTACK! It is a critical hit on you! Your head rolls off...')
            print('You have 0 Health left.')
            print('CELESTIAL BEING: THIS WORLD BELONGS TO MEEEE!')
            print(GAME_OVER)
        elif response_2 == 2:
            print('')
            print('You deliver the final blow to CELESTIAL BEING! CELESTIAL BEING\'s head rolls off')
            print(f'CELESTIAL BEING: NOOOOOOOoooooooo!!!!!!')
            endings()
    elif response == 2:
        print('')
        print('CELESTIAL BEING: No wait, I\'m scared to die, please stop...')
        print('You deliver the final blow to CELESTIAL BEING! CELESTIAL BEING\'s head rolls off')
        print(f'CELESTIAL BEING: NOOOOoooo!!!')
        endings()


def endings():
    print('')
    print('********** Congratulations! You are now the Ruler of The World **********')
    decision = int(input('''How will you rule?
    PRESS(1). LAW     PRESS(2). NEUTRAL     PRESS(3). CHAOS'''))
    if decision == 1:
        print('')
        print('''
        As a LAW ruler, you rule with order and peace.You like to promote order and safety, 
        but when taken to an extreme, it leads to dictatorship and elitism.
        ''')
        print('')
        print('$$$$$$$$ THANK YOU FOR PLAYING!!! $$$$$$$$')
    elif decision == 2:
        print('''
        As a NEUTRAL ruler, you reject the concept of relying on Lawful or Chaotic 
        powers and focus instead on personal empowerment, refinement, individuality and the inherent strength of mankind.
        humans however could become neglectful of the world around them, leading to a gradual period of decay and 
        languishing for the world.''')
        print('')
        print('$$$$$$$$ THANK YOU FOR PLAYING!!! $$$$$$$$')
    elif decision == 3:
        print('''
        As a CHAOS ruler, you associate with freedom and war. You promote freedom of choice, thought and action 
        above all else in stark contrast to the controlling nature of the Law alignment. However, this freedom can lead 
        to a vast amount of suffering and anarchy, leading the world into a primal state of unsuppressed vice and 
        survival of the fittest. 
        ''')
        print('')
        print('$$$$$$$$ THANK YOU FOR PLAYING!!! $$$$$$$$')


def your_move():
    move = ''
    attack = BOSS_MOVES[random.randint(0, len(BOSS_MOVES) - 1)]
    print('----> CELESTIAL BEING is about to use ' + attack + '. What will you do?')
    while move != 1 and move != 2 and move != 3 and move != 4:
        move = int(input('''
        PRESS(1). Sword attack          PRESS(2). Rocket launcher
        PRESS(3). Super punch           PRESS(4). Heal
        '''))
    return move


print(death_battle())
