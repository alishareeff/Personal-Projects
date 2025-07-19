import random
import sys
import os

def Welcome_message():
    print("Welcome to Avalon, This game consists of 5-10 players. You are either a Loyal Servant of Arther or Minion of Mordred")
    entered = False
    while not entered:
        any_key = input("Please press any key to continue")
        if any_key:
            entered = True

def get_number_of_players():
    valid = False  
    while not valid:
        try:
            str_num = int(input("Enter the number of players"))
            if str_num < 5 or str_num > 10:
                print("number of players must be between 5 and 10 (including 5 and 10)")
            else:
                valid = True
        except ValueError:
            print("you must enter a number in between 5 and 10. Please try again")

    return str_num

def make_cards(num):
    if num == 5:
        cards = ["Loyal Servant of Arther", "Merlin", "Percieval", "Assassin", "Minion of Mordred"]
    elif num == 6:
        cards = ["Loyal Servant of Arther", "Loyal Servant of Arther","Merlin", "Percieval", "Assassin", "Minion of Mordred"]
    elif num == 7:
        cards = ["Loyal Servant of Arther", "Loyal Servant of Arther","Merlin", "Percieval", "Assassin", "Morgana", "Minion of Mordred"]
    elif num == 8:
        cards = ["Loyal Servant of Arther", "Loyal Servant of Arther", "Loyal Servant of Arther","Merlin", "Percieval", "Assassin", "Morgana", "Minion of Mordred"]
    elif num == 9:
        cards = ["Loyal Servant of Arther", "Loyal Servant of Arther", "Loyal Servant of Arther","Loyal Servant of Arther","Merlin", "Percieval", "Assassin", "Morgana", "Minion of Mordred"]
    elif num == 10:
        cards = ["Loyal Servant of Arther", "Loyal Servant of Arther", "Loyal Servant of Arther","Loyal Servant of Arther","Merlin", "Percieval", "Assassin", "Morgana", "Minion of Mordred", "Minon of Mordred"]
    return cards

def assign_role(num, cards):
    random.shuffle(cards)
    if num == 5:
        roles = {'Player 1': cards[0], 'Player 2': cards[1], 'Player 3': cards[2], 'Player 4': cards[3], 'Player 5': cards[4] }
    elif num == 6:
        roles = {'Player 1': cards[0], 'Player 2': cards[1], 'Player 3': cards[2], 'Player 4': cards[3], 'Player 5': cards[4], 'Player 6': cards[5] }
    elif num == 7:
        roles = {'Player 1': cards[0], 'Player 2': cards[1], 'Player 3': cards[2], 'Player 4': cards[3], 'Player 5': cards[4], 'Player 6': cards[5], 'Player 7': cards[6] }
    elif num == 8:
        roles = {'Player 1': cards[0], 'Player 2': cards[1], 'Player 3': cards[2], 'Player 4': cards[3], 'Player 5': cards[4], 'Player 6': cards[5], 'Player 7': cards[6], 'Player 8': cards[7] }
    elif num == 9:
        roles = {'Player 1': cards[0], 'Player 2': cards[1], 'Player 3': cards[2], 'Player 4': cards[3], 'Player 5': cards[4], 'Player 6': cards[5], 'Player 7': cards[6], 'Player 8': cards[7], 'Player 9': cards[8] }
    elif num == 10:
        roles = {'Player 1': cards[0], 'Player 2': cards[1], 'Player 3': cards[2], 'Player 4': cards[3], 'Player 5': cards[4], 'Player 6': cards[5], 'Player 7': cards[6], 'Player 8': cards[7], 'Player 9': cards[8], 'Player 10': cards[9] }
    return roles

def game_start_instructions(num, roles):
    print("Your roles have been assigned, you must now choose who will be player 1 through " + str(num) + " After choosing, pass the laptop to player 1 and press c to continue")
    entered = False
    while not entered:
        any_key = input("Please press any key to continue")
        if any_key:
            entered = True
    for i in range(1,num+1):
        entered0 = False
        while not entered0:
            any_key0 = input("Your role is being revealed. Press any key to continue")
            if any_key0:
                entered0 = True
        print("Player " + str(i) + " your role is " + roles.get("Player " + str(i))) 
        entered1 = False
        while not entered1:
            any_key1 = input("Please press any key to continue before passing device to next player")
            if any_key1:
                entered1 = True
        os.system('cls' if os.name == 'nt' else 'clear')

    print("Everyone must now close their eyes and put your hands out in a fist and narrator will read out the following steps")
    entered2 = False
    while not entered2:
        any_key2 = input("Please press any key to continue")
        if any_key2:
            entered2 = True

    print("Minions of mordred open your eyes and look around so you can see all other evil agents")
    entered3 = False
    while not entered3:
        any_key3 = input("Please press any key to continue")
        if any_key3:
            entered3 = True
    
    print("Minions of mordred close your eyes and put your thumbs up")
    entered4 = False
    while not entered4:
        any_key4 = input("Please press any key to continue")
        if any_key4:
            entered4 = True
    
    print("Merlin open you eyes and take a look at all the minions of mordred")
    entered5 = False
    while not entered5:
        any_key5 = input("Please press any key to continue")
        if any_key5:
            entered5 = True

    print("Merlin close your eyes")
    entered6 = False
    while not entered6:
        any_key6 = input("Please press any key to continue")
        if any_key6:
            entered6 = True

    if num >= 6:
        print("Merlin and Morgana put your thumbs up")
        entered7 = False
        while not entered7:
            any_key7 = input("Please press any key to continue")
            if any_key7:
                entered7 = True

        print("Merlin and Morgana put your thumbs down and after 5 seconds everyone wake up")
        entered8 = False
        while not entered8:
            any_key8 = input("Please press any key to continue")
            if any_key8:
                entered8 = True

def AcceptRejectTeam():
    print("Decide as a group if you accept or reject the chosen team. Take a vote")
    choice = input("if you accept, enter 'accept', if you reject, enter 'regect'")
    if choice == 'accept':
        return True
    elif choice == 'reject':
        return False

def Quest1and2(num,player,questnum):
    if questnum == 1:
        print("Starting Quest 1")
    elif questnum == 2:
        print("Starting Quest 2")
    reject_count = 0
    over = False
    while not over:
        if num == 5 or num == 6 or num == 7:
            print("Player " + str(player) + " you will now choose your group. Choose 2 players. Make sure to reveal to everyone else who you chose")
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) 
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) 
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            if questnum == 2:
                while True:
                    try:
                        chosen3 = int(input("enter number of third player"))
                        if 1 <= chosen3 <= num:
                            if chosen3 != chosen1 and chosen3 != chosen2:
                                break
                            else:
                                print("you already chose that player. Choose a different player")
                        else:
                            print("please enter a number between 1 and " + num)
                    except ValueError:
                        print("please enter a number")

            choice = AcceptRejectTeam()
            card3 = None
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                if questnum == 2:
                    card3 = ""
                    while card3 != "success" and card3 != "fail":
                        card3 = input("player " + str(chosen3) + ", enter success or fail (all lowercase)")
                        if card3 != "success" or card3 != "fail":
                            print("please enter either success or fail")
                        os.system('cls' if os.name == 'nt' else 'clear') 

                if card3 == None:
                    print("the cards will now be shuffled and printed in random")
                    cards = [card1, card2]  
                    random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                    for card in cards:
                        print(card)
                    if card1 == "success" and card2 == "success":
                        return 1, player
                    else:
                        return 0, player
                else:
                    print("the cards will now be shuffled and printed in random")
                    cards = [card1, card2,card3]  
                    random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                    for card in cards:
                        print(card)
                    if card1 == "success" and card2 == "success" and card3 == "success":
                        return 1, player
                    else:
                        return 0, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1
            if reject_count == 5:
                over = True
                return 2, player
        else:
            
            print("Player " + str(player) + " you will now choose your group. Choose 3 players. Make sure to reveal to everyone else who you chose")
            
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            while True:
                try:
                    chosen3 = int(input("enter number of third player")) 
                    if 1 <= chosen3 <= num:
                        if chosen3 != chosen1 and chosen3 != chosen2:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            if questnum == 2:
                while True:
                    try:
                        chosen4 = int(input("enter number of fourth player"))
                        if 1 <= chosen4 <= num:
                            if chosen4 != chosen1 and chosen4 != chosen2 and chosen4 != chosen3:
                                break
                            else:
                                print("you already chose that player. Choose a different player")
                        else:
                            print("please enter a number between 1 and " + num)
                    except ValueError:
                        print("please enter a number")

            card4 = None
            choice = AcceptRejectTeam()
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card3 = ""
                while card3 != "success" and card3 != "fail":
                    card3 = input("player " + str(chosen3) + ", enter success or fail (all lowercase)")
                    if card3 != "success" or card3 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                if questnum == 2:
                    while card4 != "success" and card4 != "fail":
                        card4 = input("player " + str(chosen4) + ", enter success or fail (all lowercase)")
                        if card4 != "success" or card4 != "fail":
                            print("please enter either success or fail")
                        os.system('cls' if os.name == 'nt' else 'clear')

                if card4 == None:
                    print("the cards will now be shuffled and printed in random")
                    cards = [card1, card2,card3]  
                    random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                    for card in cards:
                        print(card)
                    if card1 == "success" and card2 == "success" and card3 == "success":
                        return 1, player
                    else:
                        return 0, player
                else:
                    print("the cards will now be shuffled and printed in random")
                    cards = [card1, card2,card3,card4]  
                    random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                    for card in cards:
                        print(card)
                    if card1 == "success" and card2 == "success" and card3 == "success" and card4 == "success":
                        return 1, player
                    else:
                        return 0, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1
            
        if reject_count == 5:
                over = True
                return 2, player
        
def Quest3(num,player,questnum):
    print("starting Quest 3")
    reject_count = 0
    over = False
    while not over:
        if num == 5:
            print("Player " + str(player) + " you will now choose your group. Choose 2 players. Make sure to reveal to everyone else who you chose")
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) 
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) 
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            choice = AcceptRejectTeam()
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                
                print("the cards will now be shuffled and printed in random")
                cards = [card1, card2]  
                random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                for card in cards:
                    print(card)
                if card1 == "success" and card2 == "success":
                    return 1, player
                else:
                    return 0, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1

        elif num == 7:
            print("Player " + str(player) + " you will now choose your group. Choose 3 players. Make sure to reveal to everyone else who you chose")
            
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            while True:
                try:
                    chosen3 = int(input("enter number of third player")) 
                    if 1 <= chosen3 <= num:
                        if chosen3 != chosen1 and chosen3 != chosen2:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            choice = AcceptRejectTeam()
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card3 = ""
                while card3 != "success" and card3 != "fail":
                    card3 = input("player " + str(chosen3) + ", enter success or fail (all lowercase)")
                    if card3 != "success" or card3 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                print("the cards will now be shuffled and printed in random")
                cards = [card1, card2, card3]  
                random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                for card in cards:
                    print(card)
                if card1 == "success" and card2 == "success" and card3 == "success":
                    return 1, player
                else:
                    return 0, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1
        elif num == 6 or num == 8 or num == 9 or num == 10:
            print("Player " + str(player) + " you will now choose your group. Choose 4 players. Make sure to reveal to everyone else who you chose")
            
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            while True:
                try:
                    chosen3 = int(input("enter number of third player")) 
                    if 1 <= chosen3 <= num:
                        if chosen3 != chosen1 and chosen3 != chosen2:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            while True:
                try:
                    chosen4 = int(input("enter number of fourth player"))
                    if 1 <= chosen4 <= num:
                        if chosen4 != chosen1 and chosen4 != chosen2 and chosen4 != chosen3:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            choice = AcceptRejectTeam()
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card3 = ""
                while card3 != "success" and card3 != "fail":
                    card3 = input("player " + str(chosen3) + ", enter success or fail (all lowercase)")
                    if card3 != "success" or card3 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card4 = ""
                while card4 != "success" and card4 != "fail":
                    card4 = input("player " + str(chosen4) + ", enter success or fail (all lowercase)")
                    if card4 != "success" or card4 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')

                print("the cards will now be shuffled in random order")
                cards = [card1, card2, card3, card4]
                random.shuffle(cards)
                for card in cards:
                    print(card)

                if card1 == "success" and card2 == "success" and card3 == "success" and card4 == "success":
                    return 1, player
                else:
                    return 0, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1

        if reject_count == 5:
                over = True
                return 2, player
        
def Quest4and5(num,player,questnum):
    #these 2 quests are almost identical except that in quest 4, evil needs 2 false cards to win (must be at least 7 players though)
    if questnum == 4:
        print("Starting Quest 4")
    elif questnum == 5:
        print("Starting Quest 5")
    reject_count = 0
    over = False
    while not over:
        if num == 5:
            print("Player " + str(player) + " you will now choose your group. Choose 3 players. Make sure to reveal to everyone else who you chose")
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) 
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) 
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            while True:
                try:
                    chosen3 = int(input("enter number of third player")) 
                    if 1 <= chosen3 <= num:
                        if chosen3 != chosen1 and chosen3 != chosen2:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            choice = AcceptRejectTeam()
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                
                card3 = ""
                while card3 != "success" and card3 != "fail":
                    card3 = input("player " + str(chosen3) + ", enter success or fail (all lowercase)")
                    if card3 != "success" or card3 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear') 

                print("the cards will now be shuffled and printed in random")
                cards = [card1, card2,card3]  
                random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                for card in cards:
                    print(card)
                if card1 == "success" and card2 == "success" and card3 == "success":
                    return 1, player
                else:
                    return 0, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1
            if reject_count == 5:
                over = True
                return 2, player
        
        elif num == 6:
            print("Player " + str(player) + " you will now choose your group. Choose 3 players. Make sure to reveal to everyone else who you chose")
            
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) 
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) 
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            while True:
                try:
                    chosen3 = int(input("enter number of third player")) 
                    if 1 <= chosen3 <= num:
                        if chosen3 != chosen1 and chosen3 != chosen2:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            if questnum == 5:
                while True:
                    try:
                        chosen4 = int(input("enter number of fourth player"))
                        if 1 <= chosen4 <= num:
                            if chosen4 != chosen1 and chosen4 != chosen2 and chosen4 != chosen3:
                                break
                            else:
                                print("you already chose that player. Choose a different player")
                        else:
                            print("please enter a number between 1 and " + num)
                    except ValueError:
                        print("please enter a number")

            card4 = None
            choice = AcceptRejectTeam()
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card3 = ""
                while card3 != "success" and card3 != "fail":
                    card3 = input("player " + str(chosen3) + ", enter success or fail (all lowercase)")
                    if card3 != "success" or card3 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                if questnum == 5:
                    while card4 != "success" and card4 != "fail":
                        card4 = input("player " + str(chosen4) + ", enter success or fail (all lowercase)")
                        if card4 != "success" or card4 != "fail":
                            print("please enter either success or fail")
                        os.system('cls' if os.name == 'nt' else 'clear')

                if card4 == None:
                    print("the cards will now be shuffled and printed in random")
                    cards = [card1, card2,card3]  
                    random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                    for card in cards:
                        print(card)
                    if card1 == "success" and card2 == "success" and card3 == "success":
                        return 1, player
                    else:
                        return 0, player
                else:
                    print("the cards will now be shuffled and printed in random")
                    cards = [card1, card2,card3,card4]  
                    random.shuffle(cards)   #printed in random so players don't know who inputted success and fail
                    for card in cards:
                        print(card)
                    if card1 == "success" and card2 == "success" and card3 == "success" and card4 == "success":
                        return 1, player
                    else:
                        return 0, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1
        
        elif num == 7:
            print("Player " + str(player) + " you will now choose your group. Choose 4 players. Make sure to reveal to everyone else who you chose")
            
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            while True:
                try:
                    chosen3 = int(input("enter number of third player")) 
                    if 1 <= chosen3 <= num:
                        if chosen3 != chosen1 and chosen3 != chosen2:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            while True:
                try:
                    chosen4 = int(input("enter number of fourth player"))
                    if 1 <= chosen4 <= num:
                        if chosen4 != chosen1 and chosen4 != chosen2 and chosen4 != chosen3:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            choice = AcceptRejectTeam()
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card3 = ""
                while card3 != "success" and card3 != "fail":
                    card3 = input("player " + str(chosen3) + ", enter success or fail (all lowercase)")
                    if card3 != "success" or card3 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card4 = ""
                while card4 != "success" and card4 != "fail":
                    card4 = input("player " + str(chosen4) + ", enter success or fail (all lowercase)")
                    if card4 != "success" or card4 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')

                print("the cards will now be shuffled in random order")
                cards = [card1, card2, card3, card4]
                random.shuffle(cards)
                for card in cards:
                    print(card)
                fail_count = 0
                for card in cards:
                    if card == "fail":
                        fail_count = fail_count + 1
        
                if questnum == 4:
                    if fail_count >= 2:
                        return 0, player
                    else:
                        return 1, player
                elif questnum == 5:
                    if fail_count >= 1:
                        return 0, player
                    else:
                        return 1, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1
            
        elif num == 8 or num == 9 or num ==10:
            print("Player " + str(player) + " you will now choose your group. Choose 5 players. Make sure to reveal to everyone else who you chose")
            
            while True:
                try:
                    chosen1 = int(input("enter number of first player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen1 <= num:
                        break
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            while True:
                try:
                    chosen2 = int(input("enter number of second player")) #need to do error handling. User input must be a number between 1 and number of players AND user cannot choose himself
                    if 1 <= chosen2 <= num:
                        if chosen2 != chosen1:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")
            
            while True:
                try:
                    chosen3 = int(input("enter number of third player")) 
                    if 1 <= chosen3 <= num:
                        if chosen3 != chosen1 and chosen3 != chosen2:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")

            while True:
                try:
                    chosen4 = int(input("enter number of fourth player"))
                    if 1 <= chosen4 <= num:
                        if chosen4 != chosen1 and chosen4 != chosen2 and chosen4 != chosen3:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number")  
            
            while True:
                try:
                    chosen5 = int(input("enter number of fourth player"))
                    if 1 <= chosen5 <= num:
                        if chosen5 != chosen1 and chosen5 != chosen2 and chosen5 != chosen3 and chosen5 != chosen4:
                            break
                        else:
                            print("you already chose that player. Choose a different player")
                    else:
                        print("please enter a number between 1 and " + num)
                except ValueError:
                    print("please enter a number") 

            choice = AcceptRejectTeam()
            if choice == True:
                card1 = ""
                while card1 != "success" and card1 != "fail":
                    card1 = input("player " + str(chosen1) + ", enter success or fail (all lowercase)")
                    if card1 != "sucess" or card1 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card2 = ""
                while card2 != "success" and card2 != "fail":
                    card2 = input("player " + str(chosen2) + ", enter success or fail (all lowercase)")
                    if card2 != "success" or card2 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card3 = ""
                while card3 != "success" and card3 != "fail":
                    card3 = input("player " + str(chosen3) + ", enter success or fail (all lowercase)")
                    if card3 != "success" or card3 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card4 = ""
                while card4 != "success" and card4 != "fail":
                    card4 = input("player " + str(chosen4) + ", enter success or fail (all lowercase)")
                    if card4 != "success" or card4 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                card5 = ""
                while card5 != "success" and card5 != "fail":
                    card5 = input("player " + str(chosen5) + ", enter success or fail (all lowercase)")
                    if card5 != "success" or card5 != "fail":
                        print("please enter either success or fail")
                    os.system('cls' if os.name == 'nt' else 'clear')

                print("the cards will now be shuffled in random order")
                cards = [card1, card2, card3, card4, card5]
                random.shuffle(cards)
                for card in cards:
                    print(card)
                fail_count = 0
                for card in cards:
                    if card == "fail":
                        fail_count = fail_count + 1
        
                if questnum == 4:
                    if fail_count >= 2:
                        return 0, player
                    else:
                        return 1, player
                elif questnum == 5:
                    if fail_count >= 1:
                        return 0, player
                    else:
                        return 1, player
            else:
                print("increasing rejecting count")
                reject_count = reject_count + 1
                if player == num:
                    print("setting player number back to 1")
                    player = 1
                else:
                    print("increasing player number count")
                    player = player + 1 
        if reject_count == 5:
                over = True
                return 2, player
        
def updatedata(roundwinner, good_points, bad_points, player, num, roles): # creating a function to encapsulate code in main that updates good/bad points and player num
    if roundwinner == 0:
        bad_points = bad_points + 1
        print("Quest failed")
    elif roundwinner == 1:
        good_points = good_points + 1
        print("Quest succeeded")
    else:
        print("team has been rejected 5 times")
        print("game over, Minions of Mordered have won")
        sys.exit()
    if player == num:
        player = 1
    else:
        player = player + 1
    
    if good_points >= 3:
        print("Loyal Servants of Arthur have passed 3 quests")
        Assassins_guess(roles) #this is where you would add function to prompt assassin to guess merlin. Make sure sys.exit is at end of this function
    if bad_points >= 3:
        print("game over, Minions of Mordered have won")
        sys.exit()
    return good_points, bad_points, player

def Assassins_guess(roles):
    assassin_player = next((k for k, v in roles.items() if v == "Assassin"), None)
    merlin_player = next((k for k, v in roles.items() if v == "Merlin"), None)
    print("Minions of Mordred still have one more chance to win. The assassin must correctly guess who merlin was")
    print("the assassin was " + assassin_player)

    while True:
        try:
            guess_num = int(input(assassin_player + ", enter the number of the player you think is merlin. MAKE SURE YOU ENTER THE RIGHT NUMBER BECAUSE ONCE YOU PRESS ENTER YOU CANNOT GO BACK"))
            break
        except ValueError:
            print("please enter a number")
    
    guess_num_str = "Player " + str(guess_num)
    if guess_num_str == merlin_player:
        print("guess was correct. Minions of Mordred have won")
        sys.exit()
    else:
        print("guess was incorrect. Loyal servants of Arthur prevail")
        sys.exit()

def main():
    good_points = 0
    bad_points = 0
    Welcome_message()
    num = get_number_of_players()
    cards = make_cards(num)
    roles = assign_role(num, cards)
    game_start_instructions(num, roles)
    player = random.randint(1,num)

    #first quest 
    questnum = 1
    round1Winner, player = Quest1and2(num, player, questnum)
    good_points, bad_points, player = updatedata(round1Winner, good_points, bad_points, player, num, roles)

    #second quest
    questnum = 2
    round2Winner, player = Quest1and2(num, player,questnum) 
    good_points, bad_points, player = updatedata(round2Winner, good_points, bad_points, player, num, roles)

    #third quest
    questnum = 3
    round3Winner, player = Quest3(num, player, questnum)
    good_points, bad_points, player = updatedata(round3Winner, good_points, bad_points, player, num, roles)
    
    #fourth quest
    questnum = 4
    round4Winner, player = Quest4and5(num,player,questnum)
    good_points, bad_points, player = updatedata(round4Winner, good_points, bad_points, player, num, roles)
    
    #fifth quest
    questnum = 5
    round5Winner, player = Quest4and5(num,player,questnum)
    good_points, bad_points, player = updatedata(round5Winner, good_points, bad_points, player, num, roles)

#good team wins the game if they win 3 quests out of 5. but evil team still has a chance to win if they guess merlin
#    
    
  
main()
    




