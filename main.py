import move_test3
import nakamura
import start
import emergency_stop
import move_test
import move_test2
import calibrate

from codrone_edu.drone import *

# オブジェクト変数を生成
drone=Drone()

print("モードを選択してください")

print("1:move_test 2:move_test2 3:move_test3 4:nakamura5:set_trim")
mode = input()

if mode == "5":
    calibrate.set_trim_config(drone)

else:
    try:
        start.start(drone) # ドローンを接続して離陸する
        if mode == "1":
            move_test.move_test(drone)  # ドローンを動かすテスト

        if mode == "2":
            move_test2.move_test(drone)

        if mode == "3":
            move_test3.move_test(drone)
        if mode == "4":
            nakamura.move_test(drone)


    except KeyboardInterrupt:# プログラムの停止ボタンを押したらドローンを緊急着陸
        emergency_stop.emergency_stop(drone)
    finally:
        print("プログラムを終了します")
        drone.close()


