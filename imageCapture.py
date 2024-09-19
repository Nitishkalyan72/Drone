from djitellopy import tello
import cv2

# to connect to our tello is very simple with creating a tello object
me = tello.Tello()
me.connect() # it will take the care of all the IP adreses and LL THE COMMUNICATION PART FOR YOU
print(me.get_battery())#give me battery of my drone

me.streamon() #stream get turn on give all frames one by one and we can process them

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img,(360,240))# yae hmne rsize krke frame small krdiya
    cv2.imshow("image",img)
    cv2.waitKey(1)#frame kae liye delay rkkha hai