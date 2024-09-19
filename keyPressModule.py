#we will make this script such that other script can also use its functions
import pygame
def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))


#if the key is pressed then it will return true otherwise false
def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    print('K_{}'.format(keyName))

    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

#Main function
def main():
    if getKey("LEFT"):
        print("Left key pressed")

    if getKey("RIGHT"):
        print("Right key Pressed")

#if i want to run this file as amain file then use it
if __name__ == "__main__":
    init()
    while True:
        main()

