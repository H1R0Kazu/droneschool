# coding: UTF-8
# 講習名： ドローンソフトウェアエンジニア
# 記載日：　2019/11/25
# 作成者：　宮田浩和
# ファイル名：　flyght_test_hm_02.py
# 内容　：　離陸後にちょっとだけ移動する。 テキストの 移動１ の部分
#


# 使用する関数、クラスを宣言する
from dronekit import connect, VehicleMode
# 標準ライブラリのtimeを使う宣言
import time


# 機体に接続する
# シミュレータに接続する場合
vehicle = connect('127.0.0.1:14550', wait_ready=True)
# UbuntuでUSB経由で接続する場合
# vehicle = connect('/dev/ttyACM0,115200', wait_ready=True)


# アーミング可能かチェック
while not vehicle.is_armable:
    print "Waiting for vehicle to initializ)e…"
    time.sleep(1)    


# vehicle.home_locationに値がセットされるまで
# downloadを繰り返し実行する。
while not vehicle.home_location:
    cmds = vehicle.commands
    cmds = download()
    cmds = wait_ready()

    if not vehicle.home_location:
        print "Waiting for home location ...."

# ホームロケーションの取得完了
print "\n Home location: %s " % vehicle.home_location


# アーミングの実行
# フライトモードをGUIDEDモードに変更し、armedにTrueを設定する
print "Arming moters"
vehicle.mode = VehicleMode('GUIDED')
vehicle.armed = True


# アーミングが完了するまで待機
while not vehicle.armed:
    print "Waiting for arming..."
    time.sleep(1)


# 目標の緯度・経度・高度を設定する
aLocation = LocationGlobalRelative(35.8787491, 140.3393722, 30)


# 目標高度を設定
targetAltitude = 20


# テイクオフ実行
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


# simele_goto を実行する
vehicle.simple_goto


# ここでプログラム終了
