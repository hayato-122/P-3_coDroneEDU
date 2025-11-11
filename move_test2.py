from codrone_edu.drone import Drone

def move_test(drone: Drone):
    drone.set_controller_LED(255, 0, 0, 100)
    drone.set_drone_LED(255, 0, 0, 100)

    drone.hover(2)

    # ドロップ
    drone.move_distance(1.8, -0.45, 0, 0.75)# ...distance(前後/m, 左右/m, 上下/m, 距離m/s)
    drone.hover(3)
    print("動作1：ドロップ上に移動")
    drone.move_distance(0, 0, -0.25, 1)
    drone.hover(3)
    print("動作2：下降")
    drone.move_distance(0.2, 0, 0, 1)
    drone.hover(2)
    print("動作3：少し前に行って停止")

    #半円超してボール初期位置
    drone.move_distance(0.2, -0.4, 0, 0.8)  # ...distance(前後/m, 左右/m, 上下/m, 距離m/s)
    drone.hover(1)
    print("動作4：L字初期位置")
    drone.move_distance(0, 0, -0.2, 0.8)
    drone.hover(1)
    print("動作5：少し下降")
    # ボール移動一回目
    drone.move_distance(0.2, 0, 0, 0.8)
    drone.hover(1)
    print("動作6：少し前進")
    drone.move_distance(-0.2, 0, 0, 0.8)
    drone.hover(1)
    print("動作7：少し後退")
    # drone.move_distance(0.4, 0, 0, 1)
    # drone.hover(1)
    # drone.move_distance(-0.2, 0, 0, 1)
    # drone.hover(1)
    drone.move_forward(distance = 100, units = "cm", speed = 0.5)
    drone.hover(1)
    print("動作8")

    # ドロップ
    drone.move_distance(0,0,0.6,1)
    drone.hover(1)
    print("動作9")
    drone.move_distance(0, 1.3, 0, 1)
    drone.hover(1)
    print("動作10")
    drone.move_distance(0, 0, 0.3, 1)
    drone.hover(4)
    print("動作11")
    drone.move_distance(0, 1.3, -0.2, 1)
    drone.hover(1)
    print("動作12")

    # ボール移動二回目
    drone.move_distance(2, 0, 0, 1)
    drone.hover(2)
    print("動作13")
    drone.move_distance(0, 0.5, 0, 1)
    drone.hover(1)
    print("動作14")

    # 円手前に移動
    drone.move_distance(-1.3, 0.5, 0, 1)
    drone.hover(1)
    print("動作15")
    drone.move_distance(-0.3, 0.3, 0, 1)
    drone.hover(1)
    print("動作16")

    # 円貫通
    drone.move_distance(1, 0, 0, 1)
    drone.hover(1)
    print("動作17")

    # ランディングポイント上空
    drone.move_distance(0, 0.5, 0, 1)
    drone.hover(3)
    print("動作18")

    drone.land()