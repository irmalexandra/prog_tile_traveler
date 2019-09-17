# def update_position():
#     position = current_position()
#     action  = player_action()
    
    

#     if action == ("n" or action == "N"):
        
#         position = position + 0.1
#         print (position)
#         return position
#     elif action == ("s" or action == "S"):
        
#         position = position -0.1
#         print (position)

#     elif action == ("e" or action == "E"):
        
#         position = position + 1
#         print (position)

#     elif action == ("w" or action == "W"):
        
#         position = position -1
#         print (position)

#     else:


#         print("Invalid Input")


# def player_action():

#     action = input("You can travel:")
#     return action
    
# def current_position():
#     start_pos = 1.1


#     win_condition = False

#     while win_condition == False:
        
#         updated_position = update_position()
#         return update_position

# def initialize_game():

#     current_position()

# initialize_game()

# vinctory_condition = False
# def starting_position():
#     starting_position = 1.1
#     return starting_position


# def player_action():

#      action = input("You can travel:")
#      return action

# def update_pos(x):

#     action = player_action()

#     if action == "n":
#         updated_pos = x + 0.1
#         return update_pos
    
#     print(update_pos)


# position = starting_position()

# while vinctory_condition != True:

    
    
#     updated_position = update_pos(player_action,position)

#     update_pos(player_action(), updated_position)

def player_action():
    action = input("input a action")
    return action

def update_position(action):

    current_action = action
    change = 0.0

    if current_action == ("n" or action == "N"):
        
        change = change + 0.1
        
    
    elif current_action == ("s" or action == "S"):
        
        change = change -0.1
        

    elif current_action == ("e" or action == "E"):
        
        change = change + 1
        

    elif current_action == ("w" or action == "W"):
        
        change = change -1
        

    else:

        print("Invalid Input")

    return change

def legal_moves(x): #takes in the current position
    
def start_game():
    position = 1.1
    victory_condition = False
    while victory_condition != True:
        action = player_action()
        position = position + update_position(action)
        print(position)

        if position == 3.1:
            victory_condition = True
        
start_game()