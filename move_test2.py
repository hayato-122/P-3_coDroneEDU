from codrone_edu.drone import Drone

def move_test(drone: Drone):

    drone.hover(3)

    # # 高度低
    drone.move_distance(0, 0, -0.4, 1)
    drone.hover(1)

    # # ドロップ
    # drone.move_distance(2.315, 0.4, 0, 1)# ...distance(前後/m, 左右/m, 上下/m, 距離m/s)
    # drone.hover(2)
    #
    # # 半円超してボール初期位置
    # drone.move_distance(0.3, 0.3, 0, 1)  # ...distance(前後/m, 左右/m, 上下/m, 距離m/s)
    # drone.hover(2)

    # ボール移動一回目
    drone.move_distance(0.2, 0, 0, 1)
    drone.hover(1)
    drone.move_distance(-0.2, 0, 0, 1)
    drone.hover(1)
    drone.move_distance(0.4, 0, 0, 1)
    drone.hover(1)
    drone.move_distance(-0.2, 0, 0, 1)
    drone.hover(1)
    drone.move_distance(1.5, 0, 0, 1)
    drone.hover(1)

    # # ドロップ
    # drone.move_distance(0, -0.5, 0, 1)
    # drone.hover(1)
    # drone.move_distance(0, 0.5, 0, 1)
    # drone.hover(1)
    #
    # # ボール移動二回目
    # drone.move_distance(1.3, 0.5, 0, 1)
    # drone.hover(1)
    # drone.move_distance(1.3, 0.5, 0, 1)
    # drone.hover(1)
    #
    # # 円手前に移動
    # drone.move_distance(-1.3, -1, 0, 1)
    # drone.hover(1)
    # drone.move_distance(-0.2, -0.5, 0, 1)
    # drone.hover(1)
    #
    # # 円貫通
    # drone.move_distance(1.3, 0, 0, 1)
    # drone.hover(1)
    #
    # # ランディングポイント上空
    # drone.move_distance(0, -0.5, 0, 1)
    # drone.hover(3)

    drone.land()