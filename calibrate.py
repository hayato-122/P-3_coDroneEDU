from codrone_edu.drone import Drone
import configparser
import time

class SetTrim:

    # iniファイルからトリム値を読み込む(初期化処理)
    def __init__(self):
        self.config_file = 'config.ini'
        self.config = configparser.ConfigParser() # オブジェクトの生成
        self.config.read(self.config_file) # config.iniファイルの全体読み込み
        try:
            self.roll_trim = int(self.config['TRIM']['roll_trim'])   # roll_trimの読み込み
            self.pitch_trim = int(self.config['TRIM']['pitch_trim']) # pitch_trimの読み込み
        except (KeyError, ValueError): # 読み込めなかった場合0 0を返す
            self.roll_trim = 0
            self.pitch_trim = 0

    def load_trim_config(self):
        return self.roll_trim,self.pitch_trim

    # iniファイルにトリム値を書き込む関数
    def save_trim_config(self):

        # TRIMセクションが存在していない場合作成
        if not self.config.has_section('TRIM'):
            self.config.add_section('TRIM')

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
    def set_trim_start(self,drone):
        while True:
            print(f"現在の設定ロール(左右)(-100~100)の{self.roll_trim}\n　　　　　ピッチ(前後)(-100~100)の現在のトリム値{self.pitch_trim}\n")
            print("流れている方向の逆にトリム値を調整(例：右に流れている場合はロールトリム値を-30に\n")
            print("  r-30 : ロール(左右)を -30 に設定")
            print("  p10  : ピッチ(前後)を +10 に設定")
            print("スペース、エンターでドローンをテイクオフ qで終了")

            bottom_range = drone.get_bottom_range(unit="cm")  # 床との距離を代入

            input_trim = input("値を入力してください：")

            if input_trim.strip() == "":
                if bottom_range == 0:
                    drone.set_trim(self.roll_trim, self.pitch_trim)
                    time.sleep(1)
                    drone.takeoff()
                    drone.hover(3)
                    drone.land()
                else:
                    print("ドローンが空中にいるためテイクオフできません")

            elif input_trim == "q":
                    print("qが押されました　調整を保存して終了します")
                    self.save_trim_config()
                    return False
            else:
                try:
                    input_trim_head = input_trim[0]
                    input_trim = int(input_trim[1:])

                    if -100 <= input_trim <= 100:
                        if input_trim_head == 'r':
                            self.roll_trim = input_trim
                        elif input_trim_head == 'p':
                            self.pitch_trim = input_trim

                except ValueError:
                    # 数字以外が入力された場合のエラー対策
                    print("エラー: 正しい形式（例: r-30）で入力してください")



drone=Drone()
set_trim = SetTrim()

try:
    # ドローンとPCを接続する
    drone.pair()
    # トリム値を設定
    roll_trim,pitch_trim = set_trim.load_trim_config() # config.iniファイルのトリム値を代入
    drone.set_trim(roll_trim,pitch_trim) # トリム値を設定

    set_trim.set_trim_start(drone)
except TimeoutError:
    print("ドローンとの接続が失敗しました")
finally:
    print("プログラムを終了します")
    drone.land()
    drone.close()



