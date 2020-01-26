import random 


health=50

difficulty=3   #1-easy, 2-medium, 3-hard

potion_health = int(random.randint(25,50)/difficulty)     #more difficulty, less health
                                                          #type casting from float to int
health = health + potion_health

print(health)
