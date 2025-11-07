from codrone_edu.drone import Drone
import time

def move_test(drone: Drone):
    drone.takeoff()
    drone.hover(1)
    print("現在の高度：", drone.get_height(unit="cm"))

    drone.hover(1)
    print("現在の高度",drone.get_height(unit="cm"))