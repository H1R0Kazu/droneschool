# coding: UTF-8
# 講習名： ドローンソフトウェアエンジニア
# 記載日：　2019/12/28
# 作成者：　宮田浩和
# ファイル名：　flyght_test_hm_03.py
# 内容　：　絶対座標で移動する

# 使用する関数、クラスを宣言する
from dronekit import connect, VehicleMode
# 標準ライブラリのtimeを使う宣言
import time


# 機体に接続する
# シミュレータに接続
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# アーミング可能かチェック
while not vehicle.is_armable:
    print "Waiting for vehicle to initialize"
    time.sleep(1)

# vehicle.home_locationに値がセットされるまで
# downloadを繰り返し実行する
while not vehicle.home_location:
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()

    if not vehicle.home_location:
        print "Waiting for home location ..."

# ホームロケーションの取得完了
print "\n Home location: %s " % vehicle.home_location

# アーミング実行
# フライトモードを”GUIDED”に変更し、armedにTrueを設定する。
print "Arming Moters"
vehicle.mode = vehicleMode("GUIDED")
vehicle.armd = True

while not vehicle.armed:
    print "Waiting for arming..."
    time.sleep(1)

# 目標高度を設定
targetAltitude = 20

# テイクオフの実行
# 20mの高さまで離陸する
print "Take Off!!"
vehicle.simple_takeoff(targetAltitude)

# 目標の高度に達するまで待つ
while True:
    print "Altitude: ", vehicle.location.global_relative_frame.alt 

    if vehicle.location.global_relative_frame.alt >= targetAltitude * 0.95:
        print "Reached target altitude"
        break

    time.sleep(1)
    

# 座標指定で移動
# 目標ロケーションの設定 北に移動
target1_location_lat = vehicle.location.global_relative_frame.lat + 0.00001
target1_location_lon = vehicle.location.global_relative_frame.lon
target1_location_alt = 30

aLocation = LocationGlobalRelative(target1_location_lat, target1_location_lon, target1_location_alt)

vehicle.simple_goto(aLocation)

# 目標のロケーションに達するまで待つ
while True:
    print "Altitude: ", vehicle.location.global_relative_frame.alt 
    # ロケーション情報の表示
    print "\n Current location: %s " % vehicle.location.global_relative_frame

    if vehicle.location.global_relative_frame.lat >= target1_location_lat  * 0.95:
        print "Reached target lat"
        break

    time.sleep(1)





# プログラム終わり
