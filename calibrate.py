from codrone_edu.drone import Drone
import configparser
import keyboard
import emergency_stop
import time

class SetTrim:

    # iniファイルからトリム値を読み込む(初期化処理)
    def __init__(self):
        self.last_keypress_time = 0 # 最後にキーが押された時間を格納する変数
        try:
            self.config = configparser.ConfigParser()  # オブジェクトの生成
            self.config.read('config.ini')             # config.iniファイルの全体読み込み
            self.roll_trim = int(self.config['TRIM']['roll_trim'])   # roll_trimの読み込み
            self.pitch_trim = int(self.config['TRIM']['pitch_trim']) # pitch_trimの読み込み
        except (KeyError, ValueError): # 読み込めなかった場合0 0を返す
            self.roll_trim = 0
            self.pitch_trim = 0


    def _input_trim_key(self,drone: Drone):
        try:
            # チェンジのチェック
            trim_changed = False

            if time.time() - self.last_keypress_time < 0.05:  # 0.1秒ごとに入力を受け付けるように
                return True

            if keyboard.is_pressed('up'):  # 矢印↑を押すとピッチをプラス
                self.pitch_trim += 1
                trim_changed = True
            elif keyboard.is_pressed('down'):  # 矢印↓を押すとピッチをマイナス
                self.pitch_trim -= 1
                trim_changed = True
            elif keyboard.is_pressed('right'):  # 矢印→を押すとロールをプラス
                self.roll_trim += 1
                trim_changed = True
            elif keyboard.is_pressed('left'):  # 矢印←を押すとロールをマイナス
                self.roll_trim -= 1
                trim_changed = True
            elif keyboard.is_pressed('q'):
                print("Qが押されました　調整保存して終了します")
                self.save_trim_config()
                return False

            if trim_changed:  # トリム値が変更されたらその値を設定して表示
                self.last_keypress_time = time.time()
                drone.set_trim(self.roll_trim, self.pitch_trim)
                print(f"\nロール(左右)の現在のトリム値{self.roll_trim}")
                print(f"ピッチ(前後)の現在のトリム値{self.pitch_trim}")

            return True
        except KeyboardInterrupt:
            emergency_stop.emergency_stop(drone)
            return False



    # iniファイルのトリム値を返す
    def load_trim_config(self):
        return self.roll_trim,self.pitch_trim

    # iniファイルにトリム値を書き込む関数
    def save_trim_config(self):

        # トリム値を文字列として設定
        self.config['TRIM'] = {
            'roll_trim': str(self.roll_trim),
            'pitch_trim': str(self.pitch_trim),
        }

        # .iniファイルに書き込む configオブジェクトをファイルに反映させるイメージ
        try:
            with open('config.ini', 'w') as configfile: # ファイルを開いて書き込みモードを起動　開いたファイルをconfigfile変数として設定
                self.config.write(configfile)           # configオブジェクトに設定された値をconfig.iniに書き込み
            print(f"トリム値を {'config.ini'} に保存しました。")

        except IOError as e: # 書き込めなかった場合
            print(f"ファイルの保存中にエラーが発生しました: {e}")
            return None  # エラー時はNoneを返す

    # トリム値設定モードの初期化と起動
    def set_trim_start(self,drone: Drone,mode):
        try:
            drone.pair()

            print("↑:ピッチを増加 ↓:ピッチを減少 →:ロールを増加 ←:ロールを減少 q:終了")
            print(f"ロール(左右)の現在のトリム値{self.roll_trim}")
            print(f"ピッチ(前後)の現在のトリム値{self.pitch_trim}")
            # 最後にキーが押された時間
            self.last_keypress_time = 0

            drone.set_trim(self.roll_trim, self.pitch_trim)  # トリム値設定

            if mode == 5:
                self.set_trim_hover(drone)
            if mode == 6:
                self.set_trim_takeoff(drone)


        except KeyboardInterrupt:  # プログラムの停止ボタンを押したらドローンを緊急着陸
            emergency_stop.emergency_stop(drone)

        except TimeoutError:
            print("ドローンとの接続が失敗しました")


    # ホバーしながらリアルタイムでトリム値を変更する関数
    def set_trim_hover(self,drone: Drone):
        try:
            drone.takeoff()

            while self._input_trim_key(drone):
                drone.hover(0.2)
                self._input_trim_key(drone)

        finally:  # プログラム終了時に必ず実行する ドローン着陸　接続停止処理
            print("プログラムを終了します")
            drone.land()
            drone.close()

    def set_trim_takeoff(self,drone: Drone):
        print("スペースキーでテイクオフできます")

        try:
            while self._input_trim_key(drone):
                bottom_range = drone.get_bottom_range(unit="cm") # 床との距離を代入

                if keyboard.is_pressed('space') and bottom_range == 0:
                    drone.takeoff()
                    drone.hover(2)
                    drone.land()

        finally:
            print("プログラムを終了します")
            drone.land()
            drone.close()


