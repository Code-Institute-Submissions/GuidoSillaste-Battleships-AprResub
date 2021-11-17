from random import randrange
import random

def check_ok(boat,ship_position):
    """
    Checks if it is taken,if it is in the grid and returns it if ok
    """
    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        if num in ship_position:
            boat = [-1]
            break            
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat)-1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break 
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break

    return boat

def get_ship(long,ship_position):
    """
    Shows the length of the ship you need to set and asks for its spot while checking if ok later.If not ok it repeats untill the current length is ok and then stores itin ship_position
    """
    ok = True
    while ok:      
        ship = []
        #ask the user to enter numbers
        print("\nPlace your ships\n")
        print("enter your ship of length ",long)
        for i in range(long):
            boat_num = input("\nplease enter a number")
            ship.append(int(boat_num))       
        #check that ship
        ship = check_ok(ship,ship_position)
        if ship[0] != -1:
            ship_position = ship_position + ship
            break
        else:
           print("error - please try again") 
        
    return ship,ship_position

def create_ships(ship_position,battleships):
    """
    gives the length of ships from battleships
    """
    ships = []
    
    for boat in battleships:
        ship,ship_position = get_ship(boat,ship_position)
        ships.append(ship)
        
    return ships,ship_position

def check_boat(b,start,dirn,ship_position):
    """
    sets a random direction for boats
    """
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
    boat = check_ok(boat,ship_position)           
    return boat  

def create_boats(ship_position,battleships):
    """
    creates a random boat whit random direction
    """
    ships = []
    for b in battleships:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            boat = check_boat(b,boat_start,boat_direction,ship_position)
        ships.append(boat)
        ship_position = ship_position + boat
    
    return ships,ship_position

def show_board_c(ai_ship_position):
    print("\n-----------battleships-----------\n")
    print("     0  1  2  3  4  5  6  7  8  9")
    """
    shows the board you made
    """
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in ai_ship_position:
                ch = " o "   
            row = row + ch
            place = place + 1
            
        print(x," ",row)

def get_shot_comp(guesses,tactics):
    """
    gives a random shot for ai
    """
    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except:
            print("incorrect entry - please enter again")
            
    return shot,guesses  

def show_board(hit,miss,comp):
    print("\n-----------battleships-----------\n")
    print("     0  1  2  3  4  5  6  7  8  9")
    """
    hidden board for you and computer
    """
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x " 
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "   
            row = row + ch
            place = place + 1
            
        print(x," ",row)

def check_shot(shot,ships,hit,miss,comp):
    """
    checks if you missed or hit a boat or destroyed one
    """
    missed = 0
    for i in range(len(ships)):      
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                comp.append(shot)
                missed = 2                              
    if missed == 0:
        miss.append(shot)
                
    return ships,hit,miss,comp,missed    

def calc_tactics(shot,tactics,guesses,hit):
    
    """
    increased computer difficulty playsa bit smarter
    """
    temp = []
    if len(tactics) < 1:
        temp = [shot-1,shot+1,shot-10,shot+10]
    else:
        if shot-1 in hit:
            temp = [shot+1]
            for num in [2,3,4,5,6,7,8]:
                if shot-num not in hit:
                    temp.append(shot-num) 
                    break 
        elif shot+1 in hit:
            temp = [shot-1]
            for num in [2,3,4,5,6,7,8]:
                if shot+num not in hit:
                    temp.append(shot+num) 
                    break
        if shot-10 in hit:
            temp = [shot+10]
            for num in [20,30,40,50,60,70,80]:
                if shot-num not in hit:
                    temp.append(shot-num) 
                    break 
        elif shot+10 in hit:
            temp = [shot-10]
            for num in [20,30,40,50,60,70,80]:
                if shot+num not in hit:
                    temp.append(shot+num) 
                    break
    
    computer_shot =[]
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            computer_shot.append(temp[i])
    random.shuffle(computer_shot)
    
    return computer_shot   

def get_shot(guesses):
    """
    gets your shot and checks if correct
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("\nplease enter your guess")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number, shot is outside the board")
            elif shot in guesses:
                print("incorrect number, used before")                
            else:
                ok = "y"
                break
        except:
            print("incorrect entry - please enter again")
            
    return shot

def check_if_empty_2(list_of_lists):
    """
    checks if player has no ships left and computer won
    """
    return all([not elem for elem in list_of_lists ])

#before game
def startgame():
    """
    main  variables
    """
    player_hit = []
    player_miss = []
    ships_sunk= []
    player_shots_fired = []  
    missed1 = 0
    tactics1 = []
    ship_position = []
    ship_position_ai = []
    ai_hit = []
    ai_miss = []
    ai_ships_sunk = []
    ai_shots_fired = []  
    missed2 = 0
    tactics2 = []

    battleships = [5,4,3,3,2,2]
    # game amount of ships
    #computer creates a board for player 1
    ships1,ship_position = create_boats(ship_position,battleships)
    #user creates the board for player 2 - show board
    ships2,ship_position_ai = create_ships(ship_position_ai,battleships)
    show_board_c(ship_position_ai)

    #loop
    for i in range(80):

    #player shoots
        player_shots_fired = player_hit + player_miss + ships_sunk
        shot1 = get_shot(player_shots_fired)
        ships1,player_hit,player_miss,ships_sunk,missed1 = check_shot(shot1,ships1,player_hit,player_miss,ships_sunk)
        show_board(player_hit,player_miss,ships_sunk)
    #repeat until ships empty
        if check_if_empty_2(ships1):
            print("end of game - winner in",i)
            break    
    #computer shoots
    
        shot2,ai_shots_fired = get_shot_comp(ai_shots_fired,tactics2)
        ships2,ai_hit,ai_miss,ai_ships_sunk,missed2 = check_shot(shot2,ships2,ai_hit,ai_miss,ai_ships_sunk)
        show_board(ai_hit,ai_miss,ai_ships_sunk)
        
        if missed2 == 1:
            tactics2 = calc_tactics(shot2,tactics2,ai_shots_fired,ai_hit)
        elif missed2 == 2:
            tactics2 = []
        elif len(tactics2) > 0:
            tactics2.pop(0)

        if check_if_empty_2(ships2):
            print("end of game - computer wins",i)
            break
        

startgame()        