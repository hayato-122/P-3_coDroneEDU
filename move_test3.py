from codrone_edu.drone import Drone
import time

PIPE_LONG = 1.524
PIPE_SHORT = 0.2

DROP_POLE = -0.275

#　処理
def move_test(drone: Drone):


    drone.hover(1)
    time.sleep(1)
    print("現在の高度：", drone.get_height())
    #drone.move_distance(0, 0, DROP_POLE,1)  # xが奥行き,yが横移動(正の数が左,負の数が右),ｚが高さ,veloctiyが速度
    #drone.hover(1)

    #drone.move_distance(0, 0, 0.275, 1)
    #drone.hover(1)
    #print("現在の高度",drone.get_height(2)) #引数を間違えているためバグが生じている　get_height(unit="cm")にすると治る
    # drone.move_distance(0.5, 0.5, 0,1)



