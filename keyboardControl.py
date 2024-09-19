from djitellopy import tello
import keyPressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed
    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("a"):#rotate in left basically ywk motion
        yv = -speed
    elif kp.getKey("d"):#rotate in right
        yv = speed
    if kp.getKey("q"):#for land
        me.land()
        sleep(3)
    if kp.getKey("e"):#for takeoff
        me.takeoff()
    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)