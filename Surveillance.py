from djitellopy import tello
import keyPressModule as kp
import time
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon() #stream get turn on give all frames one by one and we can process them


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
        time.sleep(3)
    if kp.getKey("e"):#for takeoff
        me.takeoff()
    #for store an image when we press the button
    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)#for saving the image..and we have to save the image with different name everytime.If we will not do that it will overite the previous image
        time.sleep(0.3)

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))  # yae hmne rsize krke frame small krdiya
    cv2.imshow("image", img)
    cv2.waitKey(1)  # frame kae liye delay rkkha hai

