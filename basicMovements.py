from djitellopy import tello

# we want to add delays between each command that why time needed
from time import sleep

# to connect to our tello is very simple with creating a tello object
me = tello.Tello()
me.connect() # it will take the care of all the IP adreses and LL THE COMMUNICATION PART FOR YOU
print(me.get_battery())#give me battery of my drone
#drone can move in 3 direction and rotate in 1 direction so we want to control that
me.takeoff()
# left_right_velocity: -100~100 (left/right)forward_backward_velocity: -100~100 (forward/backward)up_down_velocity: -100~100 (up/down)yaw_velocity: -100~100 (yaw)
me.send_rc_control(0,50,0,0)#means move forward with velocity 50
sleep(2)#for 2 sec
me.send_rc_control(0,0,0,0)#isse hmara drone phle completely rukega than land
me.land()
