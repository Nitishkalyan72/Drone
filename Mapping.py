#how we will. map our drone ..this si also known as odometry .Idea here is that we will use velocity to calculate our distance and we will also use the angular speed to find how much angle robot has and based on these information we will get x  and y cordinates and by taking distance and agle  we will convert into cartesian coordinates so we can convert it into a graph
from djitellopy import tello
import keyPressModule as kp
import numpy as np
from time import sleep
import cv2
import math

#===========================Parameters==============================
#we need spped and angular speed by which we can calculate distance
fspeed = 117/10 # (cm/s)actually when the testing is done of drone it travel 117 distance in 10 sec ----Actual speed here given is (15cm/s)
aspeed = 360/10 # in manaual testing drone rotate 360 degree in 10second (50d/s)
interval = 0.25 #in Example we took the frame for 1 sec here we reduce it for more accurate calculation
dInterval = fspeed * interval
aInterval = aspeed * interval
#=====================================================================
x, y = 500, 500
a = 0# angle will be continue
yaw = 0
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
points = [(0, 0), (0, 0)]


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    global x, y, yaw, a
    d = 0 # because we have to reset distance everytime
    if kp.getKey("LEFT"):

        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180
    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270
    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("a"):#rotate in left basically ywk motion
        yv = -aspeed
        yaw -= aInterval
    elif kp.getKey("d"):#rotate in right
        yv = aspeed
        yaw += aInterval
    if kp.getKey("q"):#for land
        me.land()
        sleep(3)
    if kp.getKey("e"):#for takeoff
        me.takeoff()

    sleep(interval)
    a += yaw
    x +=int (d*math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]


def drawPoints(img,points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)#incv2 we have colour bgr - blue green red
    cv2.circle(img, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500) / 100},{(points[-1][1] - 500) / 100})m',(points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1,(255, 0, 255), 1)

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    #we want to create an image so we will create black image.Image is basically an matrix of pixels so we have to use numpy library here
    img = np.zeros((1000,100,3),np.uint8) #we want a matrix of zeroes ,size = 1000*1000 , 3 is here channels as we want colured image so thatswhy we have rgb channels,and 2^8 = 256 means values range 0-255
    if points[-1][0] != vals[4] or points[-1][1] != vals[5]:
        points.append((vals[4], vals[5]))
    drawPoints(img,points)
    cv2.imshow("Output",img)
    cv2.waitKey(1)