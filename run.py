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
