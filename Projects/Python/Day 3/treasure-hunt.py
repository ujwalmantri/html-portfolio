<<<<<<< HEAD
print(r'''
 _                        
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
               [bug] .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

left_or_right = input("Type 'right' or 'left'\n").lower()
if left_or_right == "left":
    print("You've come to a lake. "
          "There is an island in the middle of the lake.")
    swim_or_not=input("Type 'wait' to wait for a boat. "
                      "Type 'swim' to swim across.\n").lower()
    if swim_or_not == "wait":
        print("You arrive at the island unharmed. "
              "There is a house with 3 doors.")
        which_color=input("One red, one yellow and one blue. "
                          "Which one do you choose?\n").lower()
        if which_color == "yellow":
            print("You found the treasure! You Win!")
        elif which_color == "red":
            print("It's a room full of fire. Game Over!")
        elif which_color == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose the room that doesn't exist. Game Over!")
    else:
        print("Attacked by trout. Game Over!")
else:
=======
print(r'''
 _                        
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
               [bug] .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

left_or_right = input("Type 'right' or 'left'\n").lower()
if left_or_right == "left":
    print("You've come to a lake. "
          "There is an island in the middle of the lake.")
    swim_or_not=input("Type 'wait' to wait for a boat. "
                      "Type 'swim' to swim across.\n").lower()
    if swim_or_not == "wait":
        print("You arrive at the island unharmed. "
              "There is a house with 3 doors.")
        which_color=input("One red, one yellow and one blue. "
                          "Which one do you choose?\n").lower()
        if which_color == "yellow":
            print("You found the treasure! You Win!")
        elif which_color == "red":
            print("It's a room full of fire. Game Over!")
        elif which_color == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose the room that doesn't exist. Game Over!")
    else:
        print("Attacked by trout. Game Over!")
else:
>>>>>>> a9bc62e36c5ec236c2ca38a046bf31e6759214bc
    print("You fall into a river. Game Over!")