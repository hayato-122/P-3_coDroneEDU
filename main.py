import move_test3
import nakamura
import start
import emergency_stop
import move_test2
import calibrate

from codrone_edu.drone import *

# インスタンスの作成
drone=Drone()
set_trim=calibrate.SetTrim()

# モード選択ループ
while True:
    print("モードを選択してください")
    print("1:move_test 2:move_test2 3:move_test3 4:nakamura 5:hover_trim 6:takeoff_trim")
    try:
        mode_input = input()   # 入力
        mode = int(mode_input) # 整数に変換
    except ValueError: # 入力値が不正な場合のmodeの値を0にする
        mode = 0

    if 1<= mode <= 6: # modeが範囲内ならループから出る
        break
    else:             # 不正な値の場合ループ
        print("不正な値が入力されました。再度入力してください。")


if mode >= 5: # トリム値設定モード起動
    set_trim.set_trim_start(drone,mode)
else:
    try:
        start.start(drone,set_trim)     # ドローンを接続して離陸する

        if mode == 1:
            move_test.move_test(drone)  # ドローンを動かすテスト
        if mode == 2:
            move_test2.move_test(drone)
        if mode == 3:
            move_test3.move_test(drone)
        if mode == 4:
            nakamura.move_test(drone)

    except KeyboardInterrupt:# プログラムの停止ボタンを押したらドローンを緊急着陸
        emergency_stop.emergency_stop(drone)

    finally:
        print("プログラムを終了します")
        drone.close()
