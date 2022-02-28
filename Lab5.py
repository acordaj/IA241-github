"""
lab5
"""

#3.1

alien_color = 'green' 

if alien_color == 'green':
    print("the player just earned 5 points")
    
#3.2 

alien_color= 'blue'
if alien_color == 'green':
    print("the player just earned 5 points")
else:
    print("the player just earned 10 points")
    
#3.3

favorite_fruit  = ("apple", "peach", "watermelon")
if "peach" in favorite_fruit:
    print("yay, I love peaches")

favorite_fruit  = ("apple", "peach", "watermelon")
if "apple" in favorite_fruit:
    print("yay, I love apples")

favorite_fruit  = ("apple", "peach", "watermelon")
if "watermelon" in favorite_fruit:
    print("yay, I love watermelon")

#3.4

age = 67
if age < 10:
    print("this is a kid")

elif age >= 10 and age <20:
    print("this is a teenager")
    
if age >= 65:
    print("this is an elder")
        
else:
    print("this is an adult")
    
    