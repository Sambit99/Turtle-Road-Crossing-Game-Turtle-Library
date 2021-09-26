SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

PLAYER_STARTING_POSITION = (0,(SCREEN_HEIGHT//2*-1)+20)
PLAYER_FINISHING_POSITION = (SCREEN_HEIGHT//2)-30    #(0,(SCREEN_HEIGHT//2)-30)

COLOURS = ['red','green','yellow','blue','black','orange','purple','grey']

CARS_MOVING_SPEED = 5
SPEED_INCREMENT = 10

FONT = ('Courier',15,'normal')


def getPosition():
    temp = []
    for i in range((SCREEN_HEIGHT//2*-1)+50,(SCREEN_HEIGHT//2)-50,20):
        temp.append(i)

    return temp

BORDER_POSITIONS = getPosition()