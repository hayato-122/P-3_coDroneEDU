import calibrate

def start(drone,set_trim):
    try:
        # ドローンとPCを接続する
        drone.pair()
        # トリム値を設定
        roll_trim,pitch_trim = set_trim.load_trim_config() # config.iniファイルのトリム値を代入
        drone.set_trim(roll_trim,pitch_trim) # トリム値を設定
        # 離陸する
        drone.takeoff()
        # 1秒ホバリング(空中で止まる)
        drone.hover(1)
    except TimeoutError:
        print("ドローンとの接続が失敗しました")